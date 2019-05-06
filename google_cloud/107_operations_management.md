### Operations and Management

#### Google Stackdriver (Global)
* Family of services for monitoring, logging, and diagnosing apps on GCP and AWS.
* Basic tier for GCP only; premium tier for GCP and AWS.

#### Stackdriver Monitoring (Global)
* Gives visibility into performance, uptime, overall health of cloud apps.
* ~ CloudWatch Metrics & Dashboards, Datadog, collectd.
* Cross cloud: GCP and AWS.

#### Stackdriver Logging (Global)
* Store, search, analyze, monitor and alert on log data and events.
* ~CloudWatch Logs, Splunk.
* Help debug issues quickly.
* Send real-time log data to BigQuery for SQL querying.
* Export to GCS to store archives.

#### Stackdriver Error Reporting (Global)
* Counts, analyzes, aggregates and track crashes in helpful centralized interface.
* Smartly aggregates errors into meaningful groups tailored to language & framework.
* Instantly alerts when a new app error cannot be grouped with existing ones.
* Link from notification to error details: time chart, occurrences, affected users, first/last seen dates.
* Parsers know Java, Python, JavaScript, Ruby, C#, PHP, Ruby.

#### Stackdriver Trace (Global)
* Tracks and display call tree and timing across distributed systems to debug performance.
* Automatically captures traces from Google App Engine.
* Daily auto report or on-demand.
* Detect app latency shift over time.
* ~ AWS X-Ray, Zipkin.

#### Stackdriver Debugger (Global)
* Grab program states (callback, variables, expressions) in live deploys at low impact.
* Source view supports Cloud Source Repository, GitHub, Bitbucket, local & upload.
* Automatically enabled for Google App Engine apps; agents available for others.
* Share debugging sessions with others by URL.

#### Cloud Deployment Manager (Global)
* Create/manage resource via declarative templates (infrastructure as code).
* Templates written in YAML, Python, Jinja2.
* Free.

#### Cloud Billing API (Global)
* Programmatically manage billing for GCP projects and get GCP pricing.
