# List of failed jenkins jobs

Python script which prints the url of SD failed jenkins jobs.

## Requirements

* python3
* requests
* dotenv

## Usage

Set the environment variables USERNAME and API_TOKEN in .env file, then run the script

`python3 failed-jenkins-jobs.py`

OR

`USERNAME=<user> API_TOKEN=<token> python3 failed-jenkins-jobs.py`

## Docker

A docker image of the script is available in [fagostini/failed-jenkins-jobs](https://hub.docker.com/r/fagostini/failed-jenkins-jobs/tags).  
Run it with

`docker run --env-file .env fagostini/failed-jenkins-jobs`
