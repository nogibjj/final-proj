from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def predict(self):
        payload = {'message': 'Hello world'}
        self.client.post('/predict', json=payload)
