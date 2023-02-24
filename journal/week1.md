# Week 1 — App Containerization

## Required Homework

### Containarize Backend
#### Run Python

Thought that python is already installed so I can run flask directly but I got below error saying that no module named flask.

![](/_docs/assets/Week1/Run-flask-before-installing-requirements.png)

flask should be installed first then I can use run command so I used pip install command to install libraries from requirements.txt which contains flask and flask-cors

![](/_docs/assets/Week1/Run-flask-directly.png)

got error 404 because of end point

![](/_docs/assets/Week1/404-error.png)

Then got JSON response back when I used the correct endpoint for /api/activities/home

![](/_docs/assets/Week1/JSON-result-back-api-activities-home.png)

and also got the JSON back when I tried to use /api/message_groups

![](/_docs/assets/Week1/JSON-result-back-api-message_groups.png)

#### Add Dockerfile
#### Build Container
#### Run Container
