import os
from locust import HttpUser, task, between



class FileUploadUser(HttpUser):
    wait_time = between(1, 3)  # Simulate user wait time between requests

    @task
    def upload_file(self):
        file_path = "uploads/50MB.zip"
        # Ensure a test file exists
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("This is a test file for benchmarking FastAPI file upload speed.")

        with open(file_path, "rb") as file:
            files = {"file": (file_path, file, "text/plain")}
            self.client.post("/upload/", files=files)
