# WeirdText-RESTfull-api

Simple web API that allows WeirdText encoding and decoding.

# Usage
To install dependencies (it is recommended to do this in virtual enviroment):  
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
Deployment on Heroku has two endpoints that could be used and to use  
any of this endpoints PUT request must be send with JSON body:
* `https://weird-text-api-szymos.herokuapp.com/v1/encode`  
```
{"text": "This ia a long looong test sentence, \nwith some big (biiiig) words!"}
```  
* `https://weird-text-api-szymos.herokuapp.com/v1/decode`  
```
{"text": "\n-weird-\nTihs ia a lnog loonog tset stnceene, \nwtih smoe big (biiiig) wrdos!\n-weird-\n
        long looong sentence some test This with words"}
```  

You will get JSON response with key `encode` or `decode`, corresponding to each endpoint.  
Value for these keys will be encoded/ decoded text.
