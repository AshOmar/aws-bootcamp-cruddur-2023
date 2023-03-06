# Week 2 — Distributed Tracing

## Required Homework

### Instrument Honeycomb with OTEL

Below are the needed dependancies added to requirements.txt

![](/_docs/assets/Week2/Honeycomb/OTel-requirement.png)

I've Managed to Instrument both Home Activities and Notification

![](/_docs/assets/Week2/Honeycomb/Home-Notifications.png)

Also added some parameters 

![](/_docs/assets/Week2/Honeycomb/app-parameters.png)

and got some errors while doing changes which I found in Honeycomb

![](/_docs/assets/Week2/Honeycomb/Traces_Error.png)

Finally I saved some quieries in Honeycomb to be used later once needed

![](/_docs/assets/Week2/Honeycomb/Saved-Queries.png)

### Instrument AWS X-Ray

Below are the needed dependencies added to requirements.txt

![](/_docs/assets/Week2/XRay/XRay-Requirements.png)

Created XRay Group

![](/_docs/assets/Week2/XRay/XRay-Groups.png)

Added XRay Sampling Rules

![](/_docs/assets/Week2/XRay/XRay-Sampling-Rules.png)

Used @xray_recorder.capture("user_activities") to create the user_activities segment

![](/_docs/assets/Week2/XRay/XRay-Segment.png)

Managed to get some traces in XRay showing same created segment

![](/_docs/assets/Week2/XRay/XRay-Traces.png)

### Instrument AWS X-Ray Subsegments 

Created Subsegment moc-data under user_activities segment and implemented Metadata and Annotations

![](/_docs/assets/Week2/XRay/XRay-Subsegment-Metadata_Annotation.png)

Showing moc-data Subsegments under user_activites segment in XRay

![](/_docs/assets/Week2/XRay/XRay-moc-data.png)

Showing Metadata from AWS XRay

![](/_docs/assets/Week2/XRay/XRay-Metadata.png)

Showing Annotations from AWS XRay

![](/_docs/assets/Week2/XRay/XRay-Annotations.png)

### Configure custom logger to send to CloudWatch Logs

### Integrate Rollbar and capture an error
