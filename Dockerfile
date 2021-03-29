FROM python:3.7-alpine

ADD failed-jenkins-jobs.py /
ADD .env /

RUN pip install requests
RUN pip install python-dotenv

CMD [ "python", "./failed-jenkins-jobs.py" ]