
FROM python:3.10-slim-buster

# Make a new folder inside contianer.
WORKDIR /backend-flask

# Outside Container --> Inside Container.
# This contians all libraries needed to install so we can run the app.
COPY requirements.txt requirements.txt

# Inside Container.
# Install the python libraries used for the app.
RUN pip3 install -r requirements.txt

# Outside Container --> Inside Container.
# . means everything in the current directory.
# first period . -/backend-flask (outside container).
# second period . -/backend-flask (inside container).
COPY . .

# set Environment Variables (Env Vars).
# Inside Container.
ENV FLASK_ENV=development
ENV PYTHONUNBUFFERED=1

EXPOSE ${PORT}
# python3 -m flask run --host=0.0.0.0 --port=4567
# -m module
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

# Difference between RUN & CMD:
# RUN: is part of the setup process in which we build the image so it will
# create one layer.
# CMD: is the command which will be executed by the container 
# when it is running.