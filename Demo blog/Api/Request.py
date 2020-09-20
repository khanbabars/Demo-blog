'''
Created on Sep 6, 2020

@author: shazib
'''
import requests 
import json


class Request:
    reply_status = 404  #custom code instead of exception handling
    items = 'No data found in the given endpoints'

    def __init__(self, endpoints):
        self.endpoints = endpoints

    def get_api(self):
        response = requests.get(self.endpoints)
        Request.reply_status = response.status_code 
        if Request.reply_status == 200:
            dumps = json.dumps(response.json())
            items = json.loads(dumps)
        else:
            items = Request.items     
        return items, Request.reply_status



