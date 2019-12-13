import os
from bottle import Bottle, request, route, run  
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration  
  
sentry_sdk.init(dsn="https://8aa1f6b87bcc4d7496a6c7703a52a3a2@sentry.io/1855537", integrations=[BottleIntegration()])  
  
app = Bottle()  

@app.route('/success') 
def success():
    return    

@app.route('/fail') 
def fail():    
    raise RuntimeError("There is an error!")
    
if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080)