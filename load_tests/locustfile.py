from locust import HttpUser, task, between


class OrderServiceTestUser(HttpUser):

    wait_time = between(0.5, 3.0)

    def on_start(self) -> None:
        pass

    def on_stop(self):
        pass

    @task(1)
    def get_orders(self):
        self.client.get("http://localhost:8000/api/v1/orders")
