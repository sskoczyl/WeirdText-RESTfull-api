# WeirdText-RESTfull-api

Simple web API written in Django, that allows WeirdText encoding and decoding.  
Deployment is done using **Heroku**, for CI/CD **CircleCI** is used.

# Usage
To install dependencies (it is recommended to do this in virtual environment):  
```
pip -r requirements.txt
```
In order to run server, in root folder (where manage.py is), execute:
```
gunicorn weird_text_api.wsgi:application
```
Or run Django test server:
```
python manage.py runserver
```
API provided by server is described in section below.

# Heroku deployment
Deployment on Heroku has two endpoints that could be used. In order to use  
any of this endpoints `PUT` request must be sent with JSON body:
* [`weird-text-api-szymos.herokuapp.com/v1/encode`](https://weird-text-api-szymos.herokuapp.com/v1/encode)  
```
{"text": "This ia a long looong test sentence, \nwith some big (biiiig) words!"}
```  
* [`weird-text-api-szymos.herokuapp.com/v1/decode`](https://weird-text-api-szymos.herokuapp.com/v1/decode)  
```
{"text": "\n-weird-\nTihs ia a lnog loonog tset stnceene, \nwtih smoe big (biiiig) wrdos!\n-weird-\n
        long looong sentence some test This with words"}
```  

You will get JSON response with key `encode` or `decode`, corresponding to each endpoint.  
Value for these keys will be encoded/ decoded text. Example response from `v1/encode`:  
```
{"encoded": "\n-weird-\nTihs ia a lnog lonoog tset snectnee, \nwtih smoe big (biiiig) wdros!\n-weird-\nlong looong sentence some test This with words"}
```

# Example
To test endpoints mentioned in section above following **bash** commands can be used:
```
curl -X PUT https://weird-text-api-szymos.herokuapp.com/v1/encode -H "Content-Type: application/json" -d '{"text": "This ia a long looong test sentence, \nwith some big (biiiig) words!"}'
```
```
curl -X PUT https://weird-text-api-szymos.herokuapp.com/v1/decode -H "Content-Type: application/json" -d '{"text": "\n-weird-\nTihs ia a lnog loonog tset stnceene, \nwtih smoe big (biiiig) wrdos!\n-weird-\nlong looong sentence some test This with words"}'
```
It is quicker and more convenient to use [`POSTMAN`](https://www.postman.com/) rather than curl.
