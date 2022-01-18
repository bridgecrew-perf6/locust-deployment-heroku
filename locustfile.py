import datetime
import os
import json
import urllib
import requests
from locust import HttpUser, task, constant
# IS_AUTH_NEEDED = os.environ.get('IS_AUTH_NEEDED', 'False')
REQUESTS_FILE_PATH = os.environ.get('REQUESTS_FILE_PATH', 'requests_testing.txt')
class QuickstartUser(HttpUser):
    wait_time = constant(1)

    @task
    def start_sending_requests(self):
        requests_file = urllib.request.urlopen(REQUESTS_FILE_PATH)
        reqests_data = requests_file.readlines()
        for request_data in reqests_data:
            request_data = request_data.decode("utf-8").strip().split(":@")
            if request_data[0] == "GET":
                self.client.get(request_data[1])
            elif request_data[0] == "POST":
                response = self.client.post(request_data[1], json=json.loads(request_data[2]))
            elif request_data[0] == "DELETE":
                self.client.delete(request_data[1])
            elif request_data[0] == "PUT":
                self.client.put(request_data[1], json=json.loads(request_data[2]))
            elif request_data[0] == "PATCH":
                print("patch request to " + request_data[1])
            else:
                print("unknown request type")

    # @task
    # def hello_world2(self):
    #     print("/post/[?id] -->",datetime.datetime.now().strftime("%H:%M:%S"))

    # @task
    # def hello_world3(self):
    #     print("todos -->",datetime.datetime.now().strftime("%H:%M:%S"))
        