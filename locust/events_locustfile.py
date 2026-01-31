from locust import HttpUser, task, between

class EventsUser(HttpUser):
    # wait_time = between(1, 2) # Before Optimization 
    wait_time = between(0.1, 0.3) # After Optimization  # smaller think time

    @task
    def view_events(self):
        self.client.get("/events?user=locust_user")
