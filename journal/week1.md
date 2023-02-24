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

Docker assigns a unique ID to each container. The full container ID is a hexadecimal string of 64 characters. However, in most cases, the short version of this container ID is sufficient. The short container ID represents the first 12 characters of the full container ID.

#### Build Container
#### Run Container
