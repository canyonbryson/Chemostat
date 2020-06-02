import time
time.sleep(60 * 3) # stall 2 minutes for startup - to connect to wifi first

from gevent.pywsgi import WSGIServer
from app import app, IP

http_server = WSGIServer((IP, 5000), app) #run the app on the IP address port 5000  
http_server.serve_forever() 