### What

In this repository, a complete CI/CD pipeline for deploying a flask application
to AWS ECS has been provided.

### Technologies
Flask: The framework for defining a web app.
Gunicorn: Used for presenting the app.
Nginx: Used as a reverse proxy.

### How to use the project
[Google](https://www.google.com)
1. Create an env.encrypted file using 
[jet](https://docs.cloudbees.com/docs/cloudbees-codeship/latest/pro-jet-cli/encrypt) 
from CodeShip which includes the credentials for an AWS IAM user who has 
AmazonECS_FullAccess and EC2InstanceProfileForImageBuilderECRContainerBuilds 
policies attached to it.


