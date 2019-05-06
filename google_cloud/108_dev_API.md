### Development & APIs
#### Cloud Source Repositories (Global)
* Hosted private Git repositories, with integrations with GCP and other hosted repos.
* ~ AWS CodeCommit, GitHub.
* Support standard Git functionality.
* No enhanced workflow support e.g. pull requests.
* Pay by monthly active users and storage and egress.

#### Container Builder (Global)
* Turns source code into build artifacts packaged as a `Docker image.`
* ~ Amazon CodeBuild, Travis CI, Jenkins.
* Runs several builds in parallel.
* Pay per minutes of build time.

#### Container Registry (Regional, Multi-Regional)
* Fast, private Docker image storage (based on GCS) with Docker V2 Registry API.
* ~ Amazon ECR (Elastic Container Registry), Docker Hub.
* Creates and manages a multi-regional GCS bucket and translates GCR calls to GCS.
* IAM integration simplifies builds and deployments within GCP.
* Quick deploys because of GCP networking to GCS.
* Directly compatible with standard Docker CLI; native Docker Login support.
* UX integrated with Container Builder & Stackdriver logs.
* UI to manage tags and search for images.

___
#### Cloud Endpoints (Global)
* Handles authorization, monitoring. logging, API keys for APIs backed by GCP.
* ~ Amazon API Gateway, NGINX.
* Proxy instances are distributed and hoked into Cloud Load Balancer.
* Very fast, < 1ms / call.
* Integrates with Stackdriver Logging and Stackdriver Trace.
* API needs to be resource-oriented (RESTful).

#### Apigee API Platform (Global)
* Full-featured * enterprise scale API management platform for whole API lifecycle.
* ~= Amazon API Gateway + AWS Shield, CA API Gateway.
* Transform calls among different protocols (SOAP, REST, XML, binary, custom).
* Sense and alerts suspicious API behaviors.
* Expensive. "Contact for price."

#### Test Lab for Android (Global)
* Cloud infrastructure for running test matrix across variety of real Android devices.
* ~ AWS Device Farm / Xamarin Test Cloud / Sauce Labs Mobile Testing.
* Production-grade devices flashed with Android version and locale.
* Capture log files, saves annotated screenshots * videos to show steps.
* Automatic by default, but supports custom script too.
