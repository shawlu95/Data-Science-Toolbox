### Lab 2: Interact with Google Cloud Storage v1.3

#### Ingesting Data
To view information about the Compute Engine instance you just launched, type the following into your SSH terminal: `cat /proc/cpuinfo`.

Install Git:
```
sudo apt-get update
sudo apt-get -y -qq install git
```
Verify Git is installed: `git --version`.

Download code repo from Github:
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

Enter folder `cd CPB100/lab2b`
Download data: `bash ingest.sh`.

Check first few lines: `head earthquakes.csv`.

___
#### Transform
Install necessary python packages: `bash install_missing.sh`.

Transformation: `python3 transform.py`.

Notice a new image file in the directory: `ls -l`.

___
#### Create bucket
In the GCP Console, on the Navigation menu.

Click Storage.

Click Create Bucket.

For Name, enter your Project ID. Select Set object-level and bucket-level permissions under Access control model, then click Create. To find your Project ID, click the project in the top menu of the GCP Console and copy the value under ID for your selected project.

Note the name of your bucket. In the remainder of the lab, replace <BUCKET-NAME> with your unique bucket name.

___
#### Store Data
In your SSH terminal, type the following, replacing <YOUR-BUCKET> with the name of the bucket you created in the previous task. Notice the .* includes any files starting with "earthquakes".
```
gsutil cp earthquakes.* gs://qwiklabs-gcp-1749c362ce7899e8/earthquakes/
```

___
#### Publish Cloud Storage files to web
Notice the * characters publishes every file in `earthquakes` directory.
```
gsutil acl ch -u AllUsers:R gs://qwiklabs-gcp-1749c362ce7899e8/earthquakes/*
```

Outputs:
```
Updated ACL on gs://qwiklabs-gcp-1749c362ce7899e8/earthquakes/earthquakes.csv
Updated ACL on gs://qwiklabs-gcp-1749c362ce7899e8/earthquakes/earthquakes.htm
Updated ACL on gs://qwiklabs-gcp-1749c362ce7899e8/earthquakes/earthquakes.png
```

Public links:
https://storage.googleapis.com/qwiklabs-gcp-1749c362ce7899e8/earthquakes/earthquakes.csv
https://storage.googleapis.com/qwiklabs-gcp-1749c362ce7899e8/earthquakes/earthquakes.htm
https://storage.googleapis.com/qwiklabs-gcp-1749c362ce7899e8/earthquakes/earthquakes.png

![alt-text](figs/published.png)
