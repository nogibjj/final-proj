from locust import FastHttpUser, between, task
import csv
import random

# Load the messages from the CSV file into a list
with open('ham_spam_test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    MESSAGES = [row['Text'] for row in reader]

# Define a user class to simulate requests
class MyUser1(FastHttpUser):
    # Set the wait time between requests
    wait_time = between(0.004, 0.006)
    

    # Define a task that sends a POST request to the API endpoint with a message from the CSV file
    @task
    def send_message(self):
        # Choose a random message from the list
        message = random.choice(MESSAGES)
        # Send a POST request to the API endpoint with the selected message
        self.client.post('/predict', json={'message': message})

class MyUser2(FastHttpUser):
    # Set the wait time between requests
    wait_time = between(0.004, 0.006)
    
    # Define a task that sends a POST request to the API endpoint with a message from the CSV file
    @task
    def send_message(self):
        # Choose a random message from the list
        message = random.choice(MESSAGES)
        # Send a POST request to the API endpoint with the selected message
        self.client.post('/predict', json={'message': message})