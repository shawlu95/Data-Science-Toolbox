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

Note: `gcloud` is the powerful and unified command-line tool for Google Cloud Platform. Full documentation is available on Google Cloud gcloud Overview. It comes pre-installed on Cloud Shell and supports tab-completion.

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

___
#### Checkout notebook into Cloud Datalab

Note: If necessary, wait for Datalab to finish launching. Datalab is ready when you see a message prompting you to do a "Web Preview".

Click on the `Web Preview` icon on the top-right corner of the Cloud Shell ribbon. Click on `Change port`. Switch to port `8081` using the `Change Preview` Port dialog box, and then click on `Change and Preview`.

Note: The connection to your Datalab instance remains open for as long as the datalab command is active. If the **cloud shell** used for running the datalab command is closed or interrupted, the connection to your Cloud Datalab VM will terminate. If that happens, you may be able to reconnect using the command `datalab connect bdmlvm `in your new Cloud Shell.

In Datalab, click on the icon for Open ungit in the top-right ribbon. In the Ungit window, select the text that reads `/content/datalab/notebooks` and remove the notebooks so that it reads `/content/datalab`, then hit Enter.

In the panel that comes up, type the following as the GitHub repository to Clone from:
```
https://github.com/GoogleCloudPlatform/training-data-analyst
```

Click Clone repository.

___
#### Open a Datalab notebook
In the Datalab browser, navigate to training-data-analyst > CPB100 > lab4a > demandforecast.ipynb.

Read the commentary, Click Clear | Clear all Cells, then run the Python snippets (Use Shift+Enter to run each piece of code) in the cell, step by step.

When you reach the section Machine Learning with Tensorflow, please stop -- that is the next lab.
