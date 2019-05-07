### Google Cloud Platform Services
#### Compute
* Compute Engine (GCE):
    - virtual machine rent on demand.
    - IaaS, ~= AWS EC2. Pricing is simpler.
* Kubernetes Engine (GKE):
    - was called Google Container Engine).
    - based on internal tool "borg."
    - ~ AWS EC2 Container Service (ECS & EKS).
* App Engine (GAE):
    - platform as a service (PaaS) that takes your code and runs it.
    - started in 2008. Auto-scale. **Server-less** Just kills.
    - ~ AWS Elastic Beanstalk, Heroku.
    - used to require app to be in Java. "Didn't get the right stepping stones into the cloud."
    - Now support Java, Python Flask, PHP, go, or any container (`Docker container`).
* Cloud Functions (GCF):
    - runs node.js code in response to an event.
    - "FaaS" or "Server-less" ~ AWS Lambdas.

**Preemptiple**: get machine at steep discount, but willing to give up the machine if someone else comes along and is willing to pay full price. Preemptiple machines are cheap and can be bought in batch and used quickly. It makes heavy-duty computation task runs faster and even cheaper.
