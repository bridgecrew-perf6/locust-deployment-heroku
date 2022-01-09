from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/posts")

    @task(3)
    def view_items(self):
        for item_id in range(3):
            self.client.get(f"/posts/{item_id}", name="/post")