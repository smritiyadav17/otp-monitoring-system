from locust import HttpUser, task, between
import random


class OTPUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def trigger_arrival(self):
        rider_id = f"r{random.randint(1, 10000)}"
        customer_id = f"c{random.randint(1, 10000)}"
        payload = {"rider_id": rider_id, "customer_id": customer_id}
        self.client.post("/send", json=payload)
