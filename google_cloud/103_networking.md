### Networking
#### Google Domains
* **Global**.
* ~ AWS Route53, Godaddy.

#### Cloud DNS:
* **Global**.
* ~ AWS Route53, Dyn.
* 100% uptime guarantee. Low latency in lookups.
* Supports DNSSEC

#### Cloud Load Balancing (CLB)
* **Regional, Global**.
* ~ Elastic Load Balancing, H-A Proxy, NGINX.
* Handle spikes without pre-warming; no instance or devices. **Low latency**.
* Built into Google networking fabric. Direct traffic to region closest to users.

#### Cloud CDN
* **Global**.
* Low latency, content delivery based on HTTP(S) CLB & integrated w/ GCE & GCS.
* ~ AWS CloudFront, Akamai, CloudFlare.
* Caches data, or "cache fill" egress charges if cache misses.
* A single checkbox away if using CLB.

#### Virtual Private Cloud (VPC)
* **Global**, IPv4 unicast software-defined network (SDN) for GCP resources.
* ~ AWS VPC, OpenFlow.
* Subnets are regional, not zonal.

#### Cloud Interconnect
* Regional, Multi-regional
* Connect external network to Google networks.

### Cloud VPN
* regional
* IPsec VPN to connect to VPC via public internet for low-volume data connections.
* Persistent, static connections between gateways.

### Dedicated Interconnect
* Regional, multi-regional
* Direct physical link between VPC and on-prem for high-volume data connections.

#### Cloud Router
* Regional
* Linking GCP VPCs to external networks.

#### CDN Interconnect
* Regional, multi-Regional
* For external CDN, not Google Cloud CDN.
* Supports Akamai, CloudFlare, Fastly.
