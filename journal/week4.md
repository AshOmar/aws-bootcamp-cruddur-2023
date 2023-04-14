# Week 4 — Postgres and RDS

## Create RDS Postgres Instance
Used below AWS CLI command to create RDS Postgres Instance:

aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version  14.6 \
  --master-username cruddurroot \
  --master-user-password ******* \
  --allocated-storage 20 \
  --availability-zone ca-central-1a \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection

## Create Schema for Postgres
schema.sql script used to create the DB schema and seed.sql used to seed some data to the DB

![](/_docs/assets/Week4/schema.png)

![](/_docs/assets/Week4/seed.png)

## Bash scripting for common database actions
created many Bash scripts for different db actions and modified the db-drop script to skip failure and consider success if DB does not exist.

![](/_docs/assets/Week4/DB-Scripts.png)

## Install Postgres driver in backend application
added connection_url in docker-compose file and psycopg binary & pool to requirements.txt

![](/_docs/assets/Week4/install-postgres-driver.png)

## Connect Gitpod to RDS instance
We have to add Gitpod IP to RDS security group rule every time we initiate a new environment so below steps should be considered:
1- Modify gitpod.yml file to get Gitpod IP
2- Call bash script to modify AWS ec2 security group rule to allow connetions from Gitpod IP

![](/_docs/assets/Week4/gitpod.png)

![](/_docs/assets/Week4/SG.png)

## Create AWS Cognito trigger to insert user into database
Created Lambda funtion to be called by AWS Cognito post confirmation

![](/_docs/assets/Week4/Lambda-Function.png)

![](/_docs/assets/Week4/cognito-post-confirmation-lambda-trigger.png)

## Create new activities with a database insert
Managed to insert new activities to the DB but with hardcoded user_handle as ashrafomar for now which will be changed in later stage

![](/_docs/assets/Week4/create-activities.png)

![](/_docs/assets/Week4/hardcoded-handle.png)
