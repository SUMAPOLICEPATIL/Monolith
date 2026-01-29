from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    # Optimized wait time
    wait_time = between(0.5, 1)

    def on_start(self):
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "locust-test"
        }

    @task
    def view_my_events(self):
        self.client.get(
            "/my-events",
            params={"user": "locust_user"},
            headers=self.headers,
            name="/my-events"
        )