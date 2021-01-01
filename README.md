### What
In this repository, a complete CI/CD pipeline for deploying a flask application
to AWS ECS has been provided.

### Technologies
**Flask**: The framework for defining a web app.<br />
**Gunicorn**: Used for presenting the app.<br />
**Nginx**: Used as a reverse proxy.<br />

### How to use the project
1. Create an `env.encrypted` file using 
[jet](https://docs.cloudbees.com/docs/cloudbees-codeship/latest/pro-jet-cli/encrypt) 
from CodeShip which includes the credentials for an `AWS IAM user` who has 
`AmazonECS_FullAccess` and `EC2InstanceProfileForImageBuilderECRContainerBuilds` 
policies attached to it.
The file which is used to create the `env.encrypted`file should include the following 
environment variables based on the [CodeShip Deploying to AWS](https://docs.cloudbees.com/docs/cloudbees-codeship/latest/pro-continuous-deployment/aws).
- `AWS_ACCESS_KEY_ID` <br />
- `AWS_SECRET_ACCESS_KEY`<br />

2. Create an `prod_db_url.encrypted` file using [jet](https://docs.cloudbees.com/docs/cloudbees-codeship/latest/pro-jet-cli/encrypt) 
which has `DATABASE` in it which is the `AWS RDS` instance endpoint. The content of 
the file to create an encrypted file from should be like the following script. <br />
`DATABASE=postgresql://postgres:1234@my_database.cvgmzutc9w8.eu-west-1.rds.amazonaws.com/postgres`

3. Create two image repositories in your `AWS account` and name them `nginx` and `flaskapp`.
Then, copy the repositories's urls from `AWS` in the `Push app image to ECR`
steps in the `codeship-steps.yml` file under the `registery` and `image_name` keys.

4. You should also put the `ECR` repositories url in the `ECS_PRACTING_TASK.json` file 
under the keys `image` for the `nginx` and `app` containers. 

5. Create an `EC2 AWS` cluster and define a service in it. Put the `service's name` and 
the `cluster's name` after `--cluster` and `--service` under the `command` key in the 
`Update service` step in the `command` section in the `codeship-steps.yml` file.

6. For being able to run `migrations`, we provide the `alembic's` infrastructure 
by looking at the [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) tutorial.
In the `alembic.ini` file, we change the `sqlalchemy.url` to `%db%`.
`sqlalchemy.url = %db%`
In order to create new migration files, we run the `alembic revision -m "Create new table"`.
Then, we put the scripts in the new created migration file in the `alembic/versions` directory.

