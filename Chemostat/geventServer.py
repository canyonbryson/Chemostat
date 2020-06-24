import time
#time.sleep(60 * 3) # stall 2 minutes for startup - to connect to wifi first

from eventlet import wsgi
import eventlet
from app import app, IP

wsgi.server(eventlet.listen((IP, 5000)), app) #run the app on the IP address port 5000  
