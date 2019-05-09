### Create a Compute Engine Instance v1.3

#### Create Compute Engine instance with the necessary API access
To create a Compute Engine instance:

1. In the GCP Console, on the Navigation menu (8ab244f9cffa6198.png), click Compute Engine.

2. Click Create and wait for a form to load. You will need to change some options on the form that comes up.

3. For Name, leave the default value, for Region, select us-central1, and for Zone, select us-central1-a.

4. For Identity and API access, in Access scopes, select Allow full access to all Cloud APIs:

5. Click Create.

___
#### SSH into the instance
When the instance is created, you can remotely access your Compute Engine instance using Secure Shell (SSH):

When the instance you just created is available, click SSH.

**Note**: SSH keys are automatically transferred - allowing you to ssh directly from the browser - with no extra software needed.

To view information about the Compute Engine instance you just launched, type the following into your SSH terminal:
```
cat /proc/cpuinfo
```

___
#### Install software
In the SSH terminal, type the following:
```
sudo apt-get update
sudo apt-get -y -qq install git
```

Verify that git is now installed:
```
git --version
```

Exit from the session by typing:
```
exit
```
