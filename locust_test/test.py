from locust import HttpLocust, TaskSet

def ping(l):
    l.client.get("/ping")

class UserBehavior(TaskSet):
    tasks = {ping: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000