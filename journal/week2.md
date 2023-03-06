# Week 2 — Distributed Tracing

## Required Homework

### Instrument Honeycomb with OTEL

#### Below are the needed dependancies added to requirements.txt

![](/_docs/assets/Week2/Honeycomb/OTel-requirement.png)

#### I've Managed to Instrument both Home Activities and Notification

![](/_docs/assets/Week2/Honeycomb/Home-Notifications.png)

#### Also added some parameters 

![](/_docs/assets/Week2/Honeycomb/app-parameters.png)

#### and got some errors while doing changes which I found in Honeycomb

![](/_docs/assets/Week2/Honeycomb/Traces_Error.png)

#### Finally I saved some quieries in Honeycomb to be used later once needed

![](/_docs/assets/Week2/Honeycomb/Saved-Queries.png)

### Instrument AWS X-Ray

#### Below are the needed dependencies added to requirements.txt

![](/_docs/assets/Week2/XRay/XRay-Requirements.png)

#### Created XRay Group

![](/_docs/assets/Week2/XRay/XRay-Groups.png)

#### Added XRay Sampling Rules

![](/_docs/assets/Week2/XRay/XRay-Sampling-Rules.png)

#### Used @xray_recorder.capture("user_activities") to create the user_activities segment

![](/_docs/assets/Week2/XRay/XRay-Segment.png)

#### Managed to get some traces in XRay showing same created segment

![](/_docs/assets/Week2/XRay/XRay-Traces.png)

### Instrument AWS X-Ray Subsegments 

#### Created Subsegment moc-data under user_activities segment and implemented Metadata and Annotations

![](/_docs/assets/Week2/XRay/XRay-Subsegment-Metadata_Annotation.png)

#### Showing moc-data Subsegments under user_activites segment in XRay

![](/_docs/assets/Week2/XRay/XRay-moc-data.png)

#### Showing Metadata from AWS XRay

![](/_docs/assets/Week2/XRay/XRay-Metadata.png)

#### Showing Annotations from AWS XRay

![](/_docs/assets/Week2/XRay/XRay-Annotations.png)

### Configure custom logger to send to CloudWatch Logs

I used [watchtower](https://pypi.org/project/watchtower) to send logs to CloudWatch

#### Import needed libraries in app.py

```python
#CloudWatch ---------------
import watchtower
import logging
from time import strftime
#
```

#### Add below code to write logs in app.py:

Logging level will be debug and log group will be cruddur

```python
#CloudWatch ----------------------------------------------

# Configuring Logger to Use CloudWatch
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
LOGGER.addHandler(console_handler)
LOGGER.addHandler(cw_handler)
LOGGER.info("App.py")
# --------------------------------------------------------
```

Group will be created as mentioned in log_group='cruddur'

![](/_docs/assets/Week2/CloudWatch/CloudWatch-Group.png)

#### Pass LOGGER to HomeActivities:

```python
@app.route("/api/activities/home", methods=['GET'])
def data_home():
  # CloudWatch --------------------------------
  # Passing logger to HomeActivities 
  data = HomeActivities.run(logger = LOGGER)
  ###data = HomeActivities.run()
  # -------------------------------------------
  return data, 200
```

#### Catch errors after any request

```python
@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response
```

#### Use LOGGER in HomeActivities class:

```python
class HomeActivities:
  #CloudWatch ---------
  def run(logger): #CloudWatch getting logger parameter in run function
  # -------------------
  ###def run():
    #CloudWatch -----------------------------
    logger.info("Home.Activities")
    #
```

#### Add Environment variables to docker-compose file:

```yaml
#CloudWatch ---------------------------------------
      AWS_DEFAULT_REGION: "${AWS_DEFAULT_REGION}"
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
# -------------------------------------------------
```


#### Logs from CloudWatch
![](/_docs/assets/Week2/CloudWatch/CloudWatch-Logs.png)

### Integrate Rollbar and capture an error

#### Created new project named Cruddur and Instruments some data (Info, Warrning & Errors)

![](/_docs/assets/Week2/Rollbar/Rollbar.png)

#### Created and Error and catched in Rollbar

![](/_docs/assets/Week2/Rollbar/Rollbar-Error.png)



