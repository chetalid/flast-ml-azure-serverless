from locust import HttpUser, task
import json
import time
import random

url = "https://flask-ml-service-webapp.azurewebsites.net"

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get(url)
    
    def on_start(self):
        payload={
    "CHAS":{"0":random.randint(1,9)},
    "RM":{"0":random.randint(1,9)},
    "TAX":{"0":random.randint(9,999)},
    "PTRATIO":{"0":random.randint(1,99)},
    "B":{"0":random.randint(9,999)},
    "LSTAT":{"0":random.randint(1,9)}
    }
        self.client.post("/predict", json=payload, headers={'Content-Type': 'application/json'})