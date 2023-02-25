# Week 1 — App Containerization

## Required Homework

### Containarize Backend
#### Run Python

Thought that python is already installed so I can run flask directly but I got below error saying that no module named flask.

![Run Flask Directly](/_docs/assets/Week1/Run-flask-before-installing-requirements.png "Run flask before installing requirements")

Flask should be installed first then I can use run command so I used pip install command to install libraries from requirements.txt which contains flask and flask-cors

![Run Flask After Intalling Requirements](/_docs/assets/Week1/Run-flask-directly.png "Run flask after installing requirements")

Got error 404 because of end point

![Error 404](/_docs/assets/Week1/404-error.png "Error 404")

Then got JSON response back when I used the correct endpoint for /api/activities/home

![JSON Response /api/activities/home](/_docs/assets/Week1/JSON-result-back-api-activities-home.png "JSON Response /api/activities/home")

And also got the JSON back when I tried to use /api/message_groups

![JSON Response /api/message_groups](/_docs/assets/Week1/JSON-result-back-api-message_groups.png "JSON Response /api/message_groups")

#### Add Dockerfile

Added Dockerfile with comments explaining each line

![](/_docs/assets/Week1/Add-Docker-File.png)

#### Build Container using docker build command

![](/_docs/assets/Week1/Docker-build.png)

#### Run Container using docker run with -e option to provide all needed Env Vars

![](/_docs/assets/Week1/Docker-run.png)

#### Container ID

Docker assigns a unique ID to each container. The full container ID is a hexadecimal string of 64 characters. However, in most cases, the short version of this container ID is sufficient. The short container ID represents the first 12 characters of the full container ID.

Get long and short container IDs using docker ps --no-trunc (default behaviour is to trunc) and also getting Container Images

![](/_docs/assets/Week1/Container-Short-Long-IDs.png)

Return container ID as Env Vars 

![](/_docs/assets/Week1/Get-container-id.png)

#### cURL GET request

Send cURL /api/activites/home to test the server

![](/_docs/assets/Week1/Curl-api-activities-home.png)

Send cURL /api/message_groups to test the server

![](/_docs/assets/Week1/Curl-api-message_groups.png)

#### Gain Access to a Container

![](/_docs/assets/Week1/attach-shell.png)

#### Check Container Logs

![](/_docs/assets/Week1/Container-logs.png)

#### Stop Container

![](/_docs/assets/Week1/Docker-stop.png)

#### Delete Image

![](/_docs/assets/Week1/docker-image-rm.png)

### Containerize Frontend

#### Run NPM Install

![](/_docs/assets/Week1/frontend/npm-install.png)

### Build Container

![](/_docs/assets/Week1/frontend/frontend-docker-build.png)

### Run Container

![](/_docs/assets/Week1/frontend/frontend-docker-run.png)

### Understand GitPod Env Vars and how to use them to generate URL

![](/_docs/assets/Week1/frontend/Using-GITPOD-EnvVars-to-generate-URL.png)

### Docker compose up

![](/_docs/assets/Week1/frontend/docker-compose-up.png)

### Frontend & Backend Talking to each other

![](/_docs/assets/Week1/frontend/backend-frontend-talking.png)

### Change to Cloud is very fun

![](/_docs/assets/Week1/frontend/cloud-is-very-fun.png)

### Create dynamodb Table

![](/_docs/assets/Week1/frontend/create-dynamodb-table.png)

### Insert and list to/from dynamodb table

![](/_docs/assets/Week1/frontend/insert-and-list-dynamodb.png)

### Add Postgres Client through GitPod init

![](/_docs/assets/Week1/frontend/add-postgress-client.png)

### Postgres connection using VSCode

![](/_docs/assets/Week1/frontend/postgres-connection-vscode.png)

### Use PSQL with --host option

![](/_docs/assets/Week1/frontend/using-psql-terminal.png)

### Document the Notification Endpoint for the OpenAI Document

![](/_docs/assets/Week1/frontend/add-notification-openapi.png)

### Write a Flask Backend Endpoint for Notifications

I got below error because I forget to import notifications_activities

![](/_docs/assets/Week1/frontend/NotificationsActivities-is-not-defined.png)

Imported notifications_activities

![](/_docs/assets/Week1/frontend/import-notifications-activities.png)

### Write a React Page for Notifications

![](/_docs/assets/Week1/frontend/add-notifications-frontend.png)

### Notifications Page

![](/_docs/assets/Week1/frontend/notifications-frontend.png)
