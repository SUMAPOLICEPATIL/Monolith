from locust import HttpUser, task, between

class EventsUser(HttpUser):
    # Optimized: smaller wait to increase throughput
    wait_time = between(0.5, 1)

    def on_start(self):
        # Optimized: reuse headers instead of recreating each time
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "locust-test"
        }

    @task
    def view_events(self):
        # Optimized: named request for better Locust stats grouping
        self.client.get(
            "/events",
            params={"user": "locust_user"},
            headers=self.headers,
            name="/events"
        )