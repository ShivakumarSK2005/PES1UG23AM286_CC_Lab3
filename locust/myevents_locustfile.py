from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    # wait_time = between(1, 2) # Before Optimization 
    wait_time = between(0, 0.2) # After Optimization

    @task
    def view_my_events(self):
        self.client.get("/my-events?user=locust_user")
    