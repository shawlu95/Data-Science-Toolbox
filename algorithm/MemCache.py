simple_data = [
    "0   req     set     -       user_1",
    "0   resp    set     ok      -",
    "1   req     get     -       user_1",
    "3   req     get     -       user_2",
    "1   resp    get     ok      -",
    "3   resp    get     ok      -",
    "2   req     get     -       listing_1",
    "2   resp    get     nokey   -",

    "1   req     getkq   -       user_1",
    "1   req     getkq   -       listing_2",
    "1   req     noop    -       -",
    "1   resp    getkq   ok      user_1",
    "1   resp    noop    ok      -"
]


# Expected output
# user_1 -> 2 hits
# user_2 -> 1 hits
# listing_1 -> 1 miss
# listing_2 -> 1 miss

# from collections import defaultdict

# decalre dicitonary of list, idx 0 : request, idx 1: response
class Connection:
    def __init__(self, idx):
        self.idx = idx
        self.keys = set()
        self.nRequests = {}
        self.nResponses = {}
        self.rctKey = None

    def addKey(self, newKey):
        self.keys.append(newKey)
        self.nRequests[newKey] = 0
        self.nResponses[newKey] = 0


connections = {}
for log in simple_data:

    line = log.split()

    idx = line[0]
    typ = line[1]
    cmd = line[2]
    key = line[-1]

    con = None
    if idx in connections:
        # connection is opened
        print("%s connection exists" % idx)
        con = connections[idx]

        # add key to the keys set of the connection
        # save as most recent key for future reference
        if key != "-":
            con.keys.add(key)
            con.rctKey = key
    else:
        # create new connection
        print("Create econnection %s" % idx)

        con = Connection(idx)
        connections[idx] = con
        con.keys.add(key)
        con.rctKey = key

    # count the numebr of requests and responses
    if typ == "req" and cmd not in ["set", "noop"]:
        con.nRequests[con.rctKey] = con.nRequests.get(con.rctKey, 0) + 1
    elif typ == "resp" and cmd not in ["set", "noop"]:
        con.nResponses[con.rctKey] = con.nResponses.get(con.rctKey, 0) + 1

# count the number of requests and responses for each key, aggregated across all connections
responses = {}
requests = {}
for key, con in connections.items():
    for key in con.keys:
        requests[key] = requests.get(key, 0) + con.nRequests[key]
        responses[key] = responses.get(key, 0) + con.nResponses[key]
print(requests, responses)

# Memcached is an open source, high-performance, distributed memory object caching system.

# At Airbnb, many applications use Memcached, but we suspect they are not using it efficiently. This means that there may be some keys or groups of keys that have very low cache hit rates.

# We’d like to do some analysis to find these groups of keys and their hit rates.

# Instructions

# Based on the provided data file, calculate the hit rates per key or group of key.

# * The standard input of your program will be the data file.
# * The standard output of your program will be a set of lines with <key>\t<hit rate> pairs.

# Definitions

# * cache hit: the requested key exists in the cache. The associated value is returned to the client.
# * cache miss: the requested key does NOT exist in the cache.
# * hit rate:
#     * the percentage of get requests that result in cache hits.
#     * in the example traffic dump below, the user key group has a 100% hit rate (2 of 2), while the listing key group has a 0% hit rate (0 of 2).

# FILE FORMAT EXPLAINED

# conn_id    magic    opcode    status    key        comment
# 0          req      set       -         user_1     set("user_1")
# 0          resp     set       ok        -          ok
# 1          req      get       -         user_1     get("user_1")
# 1          resp     get       ok        -          hit
# 2          req      get       -         listing_1  get("listing_1")
# 2          resp     get       nokey     -          miss
# 1          req      getkq     -         user_1     get_multi("user_1", "listing_2")
# 1          req      getkq     -         listing_2  continued
# 1          req      noop      -         -          end of multi request
# 1          resp     getkq     ok        user_1     "user_1" hit
# 1          resp     noop      ok        -          end of multi response (implicit "listing_2" miss)

# * Each line is tab-delimited with columns as described below.
# * There may be whitespaces at the beginning and the end of each line.
# * Column Definitions:
#     * conn_id:
#         * an integer identifying the connection the request/response was sent/received on.
#     * magic:
#         * a string identifying whether this is a request or response.
#         * possible values: req and resp.
#     * opcode:
#         * a string identifying the operation
#         * possible values:
#             * set, a set operation
#             * get, a get operation
#             * getkq, a multi-get operation. The client sends a number of getkq operations specifying what keys to retrieve. The server does not initially respond. Upon the next noop request, the server returns all the queued responses.
#             * noop, signal the end of a multi-get request.
#     * status:
#         * a string set only on responses
#         * possible values:
#             * ok for a successful set or a cache hit on get
#             * nokey for a cache miss on get.
#     * key:
#         * a string representing the cache key. A key group is a set of keys sharing the same prefix. Eg., listing_1 and listing_2 are both part of the listing key group.