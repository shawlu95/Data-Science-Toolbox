#### Activate Google Cloud Shell
Once connected to the cloud shell, you'll see that you are already authenticated and the project is set to your PROJECT_ID:
```
gcloud auth list
```

Outputs:
```
Credentialed accounts:
 - <myaccount>@<mydomain>.com (active)
```

Note: gcloud is the powerful and unified command-line tool for Google Cloud Platform. Full documentation is available on Google Cloud gcloud Overview. It comes pre-installed on Cloud Shell and supports tab-completion.

```
gcloud config list project
```

Outputs:
```
[core]
project = <PROJECT_ID>
```

___
#### Launch Cloud Datalab
To launch Cloud Datalab, In Cloud Shell, type:
```
datalab create bdmlvm --zone us-central1-a
```
Datalab will take about 5 minutes to start.

![alt-text](figs/datalab_cheatsheet.png)
