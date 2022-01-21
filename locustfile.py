import datetime
import os
import json
import urllib
import requests
from locust import HttpUser, task, constant

REQUESTS_FILE_PATH = os.environ.get('REQUESTS_FILE_PATH', 'crm_requests.txt')

def handle_empty_data(data):
    try:
        output = json.loads(data)
    except Exception as e:
        output = {}
    return output

class QuickstartUser(HttpUser):
    wait_time = constant(1)

    @task
    def start_sending_requests(self):
        requests_file = urllib.request.urlopen(REQUESTS_FILE_PATH)
        # requests_file = open(REQUESTS_FILE_PATH,'r')
        reqests_data = requests_file.readlines()
        for request_data in reqests_data:
            request_data = request_data.decode("utf-8").strip().split(":@")
            # request_data = request_data.strip().split(":@")
            if request_data[0] == "GET":
                self.client.get(request_data[1],headers = handle_empty_data(request_data[2]))
            elif request_data[0] == "POST":
                response = self.client.post(request_data[1], json=handle_empty_data(request_data[2]),headers = handle_empty_data(request_data[3]))
            elif request_data[0] == "DELETE":
                self.client.delete(request_data[1],headers = handle_empty_data(request_data[2]))
            elif request_data[0] == "PUT":
                self.client.put(request_data[1], json=handle_empty_data(request_data[2]),headers = handle_empty_data(request_data[3]))
            elif request_data[0] == "PATCH":
                self.client.patch(request_data[1], json=handle_empty_data(request_data[2]),headers = handle_empty_data(request_data[3]))
            else:
                print("unknown request type")