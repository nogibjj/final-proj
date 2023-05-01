# Final Project: Spam Detector

dataset: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

training a spam classification model using a bag-of-words approach with Naive Bayes.

build image
```
docker build -t spam-api .
```

run container
```
docker run -p <port>:8888 spam-api
```


http request (test locally)
```
curl -X POST -H "Content-Type: application/json" -d '{"message": "<email-content>"}' http://localhost:80/predict
```

Deployed on eks cluster with two replicas

Access urls:
- http://44.201.253.122:31479/predict
- http://3.237.60.191:31479/predict


## Loadtest

To run the loadtest:

```
locust -f locustfile.py
```

<img src="loadtest_result.png" width="100%">

<img src="loadtest_chart.png" width="100%">
