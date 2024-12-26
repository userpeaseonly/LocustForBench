from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(1, 3)  # User will wait between 1 to 3 seconds between tasks

    # Simulate a user making a GET request to the root endpoint
    @task
    def index(self):
        self.client.get("/")  # Replace with your FastAPI root URL
