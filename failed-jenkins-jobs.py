#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests.auth import AuthBase
from base64 import b64encode
import sys
import os
from dotenv import load_dotenv
load_dotenv()

class BasicAuthToken(requests.auth.AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        authstr = 'Basic ' + b64encode(self.token.encode('utf-8')).decode('utf-8')
        r.headers['Authorization'] = authstr
        return r

def main():

    url =  'https://ci.cloud.cnaf.infn.it/view/Failed/api/json' 
    query = {'pretty': 'true'}
    jenkins_user = os.environ.get('USERNAME')
    jenkins_api_token = os.environ.get('API_TOKEN')
    credentials = jenkins_user+':'+jenkins_api_token

    response = requests.get(url, params=query, auth=BasicAuthToken(credentials))

    if response.status_code == 200:

        data = response.json()['jobs']

        print('List of failed jenkins jobs:')

        for i in range(len(data)):
            print(i+1, data[i]['url'])

    elif response.status_code == 401:
        print('Unauthorized user')

    else :
        print('Exit with HTTP response status code',response.status_code)

if __name__ == '__main__':
    main()