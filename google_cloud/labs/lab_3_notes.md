### What you learn

In this lab, you will:
1. Create Cloud SQL instance
2. Create database tables by importing .sql files from Cloud Storage
3. Populate the tables by importing .csv files from Cloud Storage
4. Allow access to Cloud SQL
5. Explore the rentals data using SQL statements from CloudShell

___
#### Google Cloud Shell
The Cloud Shell is a virtual machine loaded with all the development tools you’ll need. It offers a persistent 5GB home directory, and runs on the Google Cloud, greatly enhancing network performance and authentication.
* Check authentication
```
gcloud auth list
gcloud config list project
```

___
#### Load Lab code
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
cd training-data-analyst/CPB100/lab3a
```
See code that creates SQL table: `less cloudsql/table_creation.sql`.
See first few lines for each file: `head cloudsql/*.csv`.

___
#### Create bucket
In the GCP Console, on the Navigation menu.

Click Storage.

Click Create Bucket.

For Name, enter your Project ID. Select Set object-level and bucket-level permissions under Access control model, then click Create. To find your Project ID, click the project in the top menu of the GCP Console and copy the value under ID for your selected project.

Note the name of your bucket. In the remainder of the lab, replace <BUCKET-NAME> with your unique bucket name.

___
#### Stage .sql and .csv files into Cloud Storage
From Cloud Shell within the lab3a directory, type:
```
gsutil cp cloudsql/* gs://qwiklabs-gcp-e9d3ad3146fe6832/sql/
```

___
#### Create Cloud SQL instance
In the GCP console, click SQL (in the Storage section).

Click Create instance.

Choose MySQL. Click Next if required.

For Instance ID, type rentals.

Scroll down and specify a root password. Before you forget, note down the root password.

Click Create to create the instance. It will take a minute or so for your Cloud SQL instance to be provisioned.

Click Check my progress to verify the objective.

___
#### Create tables
In Cloud SQL, click rentals to view instance information.

Click Import(on the top menu bar).

Click Browse. This will bring up a list of buckets. Click on the bucket you created, then navigate into sql and click table_creation.sql.

Click Select, then click Import.

___
#### Populate tables
To import CSV files from Cloud Storage, from the GCP console page with the Cloud SQL instance details, click Import (top menu).

Click Browse, browse in the bucket you created to sql, then click accommodation.csv. Click Select.

For Database, select recommendation_spark (specified in `table_creation.sql`)

For Table, type Accommodation.

Click Import.

Repeat the Import (steps 1 - 5) for rating.csv, but for Table, type Rating.

___
#### Explore Cloud SQL
To explore Cloud SQL, you can use the mysql CLI. In Cloud Shell, type the following:
```
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy
```

In the GCP Console, find the SQL Instance connection name in the Overview tab and copy it. In the command below, replace <INSTANCE_CONNECTION_NAME> with this value and run it.
```
./cloud_sql_proxy -instances=qwiklabs-gcp-e9d3ad3146fe6832:us-central1:rentals=tcp:3306 &
```

Connect to the Cloud SQL instance using mysql:
```
mysql -u root -p --host 127.0.0.1
```

MySQL will prompt you for the root password. Enter the password when prompted.

In Cloud Shell, at the mysql prompt, type:
This sets the database in the mysql session.
```
MySQL [recommendation_spark]> show tables;
+--------------------------------+
| Tables_in_recommendation_spark |
+--------------------------------+
| Accommodation                  |
| Rating                         |
| Recommendation                 |
+--------------------------------+
3 rows in set (0.05 sec)
```

View the list of tables you created. This will be helpful to prevent any typos in your query in step 4.
```
show tables;
```

Let's verify that the data was loaded.
```
MySQL [recommendation_spark]> select * from Rating limit 10;
+--------+--------+--------+
| userId | accoId | rating |
+--------+--------+--------+
| 10     | 1      |      1 |
| 13     | 1      |      1 |
| 18     | 1      |      2 |
| 12     | 10     |      3 |
| 18     | 10     |      1 |
| 21     | 10     |      2 |
| 4      | 10     |      1 |
| 1      | 11     |      1 |
| 10     | 11     |      1 |
| 11     | 11     |      1 |
+--------+--------+--------+
10 rows in set (0.05 sec)
```

Let's see if there is a great deal out there somewhere.
```
MySQL [recommendation_spark]> select * from Accommodation where type = 'castle' and price < 1500;
+----+--------------------------+--------------+-------+-------+--------+--------+
| id | title                    | location     | price | rooms | rating | type   |
+----+--------------------------+--------------+-------+-------+--------+--------+
| 14 | Colossal Peaceful Palace | Melbourne    |  1200 |    21 |    1.5 | castle |
| 15 | Vast Private Fort        | London       |  1300 |    18 |    2.6 | castle |
| 26 | Enormous Peaceful Palace | Paris        |  1300 |    18 |    1.1 | castle |
| 31 | Colossal Private Castle  | Buenos Aires |  1400 |    15 |    3.3 | castle |
| 45 | Vast Quiet Chateau       | Tokyo        |  1100 |    19 |    2.3 | castle |
+----+--------------------------+--------------+-------+-------+--------+--------+
5 rows in set (0.04 sec)
```

You may exit the mysql prompt by typing `exit`.
