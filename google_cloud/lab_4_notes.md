### Recommendations ML with Dataproc
In this lab you use Dataproc to train the recommendations machine learning model based on users’ previous ratings. You then apply that model to create a list of recommendations for every user in the database.

#### Create Assets
Download repository from GitHub.
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
cd training-data-analyst/CPB100/lab3a
```

In the GCP Console, on the Navigation menu, click Storage. Click Create bucket.

For Name, enter your Project ID. Select Set object-level and bucket-level permissions under Access control model, then click Create. To find your Project ID, click the project in the top menu of the GCP Console and copy the value under ID for your selected project.

Finally, stage the table definition and data files into Cloud Storage, so that you can later import them into Cloud SQL from Cloud Shell within the lab3a directory by typing the following, replacing <BUCKET-NAME> with the name of the bucket you just created:

```
gsutil cp cloudsql/* gs://qwiklabs-gcp-af8b52a33fa33327/sql/
```

___
#### Create Cloud SQL instance

To create Cloud SQL instance:

In the GCP Console, on the Navigation menu, click SQL (in the Storage section).

Click Create Instance.

Choose MySQL. Click Next if required.

For Instance ID, type rentals.

Scroll down and specify a root password. Before you forget, note down the root password (please don't do this in real-life!).

For Zone select us-central1-a.

Scroll down and click Set Connectivity or Click Show configuration options first (if required), then click Authorize networks > +Add network.

In Cloud Shell, make sure you're in the lab3a directory and find your IP address by typing:
```
bash ./find_my_ip.sh
```

Click Create to create the instance. It will take a minute or so for your Cloud SQL instance to be provisioned.

Note down the Public IP address of your Cloud SQL instance (35.188.199.53).

___
#### Create and populate tables

To import table definitions from Cloud Storage:

Click rentals to view details about your Cloud SQL instance.

Click Import.

Click Browse. This will bring up a list of buckets. Click on the bucket you created, then navigate into sql, click `table_creation.sql`, then click Select.

Click Import.

Next, to import CSV files from Cloud Storage, click Import.

Click Browse, navigate into sql, click accommodation.csv, then click Select.

Fill out the rest of the dialog as follows:

For Database, select recommendation_spark

For Table, type Accommodation

Click Import.

Repeat the Import process (steps 5 - 8) for rating.csv, but for Table, type Rating.

Click Check my progress to verify the objective.

___
#### Launch Dataproc

To launch Dataproc and configure it so that each of the machines in the cluster can access Cloud SQL:

In the GCP Console, on the Navigation menu, click SQL and note the region of your Cloud SQL instance.

In the GCP Console, on the Navigation menu, click Dataproc and click Enable API if prompted. Once enabled, click Create cluster.

Leave the Region as it is i.e. global and change the Zone to us-central1-a (in the same zone as your Cloud SQL instance: us-central1-a). This will minimize network latency between the cluster and the database.

For Master node, for Machine type, select 2 vCPU (n1-standard-2).

For Worker nodes, for Machine type, select 2 vCPU (n1-standard-2).

Leave all other values with their default and click Create. It will take 1-2 minutes to provision your cluster.

Note the Name, Zone and Total worker nodes in your cluster.
* Name: cluster-51d7
* Region: us-central1
* Zone: us-central1-a
* Total worker nodes: 2

In Cloud Shell, navigate to the folder corresponding to this lab and authorize all the Dataproc nodes to be able to access your Cloud SQL instance, replacing <Cluster-Name>, <Zone>, and <Total-Worker-Nodes> with the values you noted in the previous step:

```bash
cd ~/training-data-analyst/CPB100/lab3b
bash authorize_dataproc.sh cluster-51d7 us-central1-a 2
```

Outputs:
```
Machines to authorize: cluster-51d7-m cluster-51d7-w-0 cluster-51d7-w-1 in us-central1-a ... finding their IP addresses
IP address of cluster-51d7-m is 35.222.155.134/32
IP address of cluster-51d7-w-0 is 35.224.249.225/32
IP address of cluster-51d7-w-1 is 35.238.31.114/32
Authorizing [35.222.155.134/32,35.224.249.225/32,35.238.31.114/32] to access cloudsql=rentals
When adding a new IP address to authorized networks, make sure to also
 include any IP addresses that have already been authorized.
Otherwise, they will be overwritten and de-authorized.
```
___
#### Run ML model

To create a trained model and apply it to all the users in the system:

Edit the model training file using `nano`:
```
nano sparkml/train_and_apply.py
```

Change the fields marked #CHANGE at the top of the file (scroll down using the down arrow key) to match your Cloud SQL setup (see earlier parts of this lab where you noted these down), and save the file using `Ctrl+O` then press `Enter`, and then press `Ctrl+X` to exit from the file.

Copy this file to your Cloud Storage bucket using:
```
gsutil cp sparkml/tr*.py gs://qwiklabs-gcp-af8b52a33fa33327/
```

In the `Dataproc` console, click `Jobs`. Click `Submit Job`.

For `Job type`, select `PySpark` and for `Main python file`, specify the location of the Python file you uploaded to your bucket.
```
gs://qwiklabs-gcp-af8b52a33fa33327/train_and_apply.py
```

Click Submit and wait for the job Status to change from `Running` (this will take up to 5 minutes) to `Succeeded`.

___
#### Explore inserted rows

In the GCP Console, on the Navigation menu,  click SQL (in the Storage section).

Click `rentals` to view details related to your Cloud SQL instance.

Under `Connect to this instance` section, click `Connect using Cloud Shell`. This will start new Cloudshell tab. In Cloudshell tab press `Enter`.

It will take few minutes to whitelist your IP for incoming connection.

When prompted, type the root password you configured, then `Enter`.

At the mysql prompt, type:

```
use recommendation_spark;
```

This sets the database in the mysql session.

Find the recommendations for some user:

```
select r.userid, r.accoid, r.prediction, a.title, a.location, a.price, a.rooms, a.rating, a.type from Recommendation as r, Accommodation as a where r.accoid = a.id and r.userid = 10;
```

These are the five accommodations that we would recommend to her. Note that the quality of the recommendations are not great because our dataset was so small (note that the predicted ratings are not very high). Still, this lab illustrates the process you'd go through to create product recommendations.
