dataset: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

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
curl -X POST -H "Content-Type: application/json" -d '{"message": "<email-content>"}' http://localhost:<port>/predict
```

after deployed in EKS, use the specific endpoint url to replace the url
