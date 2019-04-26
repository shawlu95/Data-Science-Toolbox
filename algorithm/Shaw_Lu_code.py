class LoginLimiter(object):
    # use an array to keep track of most recent 10 requests
    def __init__(self):
        self.rctCalls = []

    # receive timestamp of a call attempt
    # return true if call is allowed
    def isAllowed(self, ts):
        if len(self.rctCalls) < 10:
            # when client has made less than 10 requests, always pass request
            self.rctCalls.append(ts)
            print("Call API at timestamp %s" % ts)
            return True
        else:
            # when client has made at least 10 requests, pass request only when
            # new request is made less than 60 seconds after 10th most recent legal call
            if ts - self.rctCalls[0] < 60:
                # deny call
                print("Exceeding call limit at timestamp %s. Call denied" % ts)
                return False
            else:
                # pass call and update cache
                self.rctCalls.pop(0)
                self.rctCalls.append(ts)
                print("Call API at timestamp %s" % ts)
                return True

# test limiter functionality
print("\nTest basic limiter functionality:")
solver = LoginLimiter()
timestamps = [i * 5 for i in range(100)]
for ts in timestamps:
    solver.isAllowed(ts)

print("\nTest multiple clients:")
# apply limiter to multiple client IDs
clientID = ["A", "B"]
clients = {ID: LoginLimiter() for ID in clientID}

# let multiple clients call API simultaneously
timestamps = [i for i in range(15)]
for ts in timestamps:
    for ID in clients:
        limiter = clients[ID]
        print("client ID: %s" % ID, end=' ')
        limiter.isAllowed(ts)