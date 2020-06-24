from app import *

@app.route('/')
def mainpage():
    if run == True:
        state = 'ON'
    if run == False:
        state = 'OFF'
    return render_template('index.html', connection=connection, purge=purge, IP = IP, state=state, pump_time = pump_time, temp = temp, sparging = duty_cycle, OD = optical_density, setpoint_T = setpoint_T, setpoint_OD = setpoint_OD, duty_cycle = duty_cycle, pH = pH)

@app.route('/index')
def index():
    if run == True:
        state = 'ON'
    if run == False:
        state = 'OFF'
    return redirect('/')

@app.route('/graph')
def graph():
    
    return render_template('graph.html', IP = IP, pump_time = pump_time, temp = temp, sparging = duty_cycle, OD = optical_density, setpoint_T = setpoint_T, setpoint_OD = setpoint_OD, duty_cycle = duty_cycle)

@app.route('/refresher', methods = ['POST', 'GET'])
def refresher():
#    global temp, optical_density, pump_time, duty_cycle
#    tuple1 = (temp, optical_density, duty_cycle, pump_time)
#    return tuple1
    return redirect('/')

@socketio.on("connect")
def connection():
    global connection
    connection = "connected"

def refreshing():
    while True:
        refresh()
        time.sleep(3)
        print("here")
        
def refresh():
    global connection, run
    if run:
        state = "ON"
    else:
        state = "OFF"
    #while True:# Get current variable to send back
    if connection == 'connected':
        global temp, optical_density, pump_time, duty_cycle
        print("here too")
        socketio.emit("temp", temp, broadcast=True)
        socketio.emit("OD", optical_density, broadcast=True)
        socketio.emit("sparging", duty_cycle, broadcast=True)
        socketio.emit("media_pump", pump_time, broadcast=True)
        socketio.emit("state", state, broadcast=True)
        socketio.emit("connection", connection, broadcast=True)
        #time.sleep(3)
    

@app.route('/change_temp', methods = ['POST'])
def change_temp():
    global setpoint_T
    value = request.form['SP_T']
    setpoint_T = float(value)
#    print ("The new temp setpoint is: " , setpoint_T)
    return redirect('/')

@app.route('/change_OD', methods = ['POST'])
def change_OD():
    global setpoint_OD
    value = request.form['SP_OD']
    setpoint_OD = float(value)
#    print ("The new OD setpoint is: " , setpoint_OD)
    return redirect('/')

@app.route('/change_sparge', methods = ['POST'])
def change_sparge():
    global duty_cycle
    value = request.form['SP_sparge']
    duty_cycle = int(value)
#    print ("The new sparging percentage is: " , duty_cycle)
    return redirect('/')

@app.route('/media_time', methods = ['POST'])
def media_time():
    global pump_time
    value = request.form['time_media']
    pump_time = int(value)      
    return redirect('/')

@app.route('/primeOD', methods = ['POST'])
def primeOD():
    value = request.form['time_OD']
    wait = int(value)
    prime_pumps(wait ,'od')
    return redirect('/')
           
@app.route('/primeIN', methods = ['POST'])
def primeIN():
    value = request.form['time_IN']
    wait = int(value)
    prime_pumps(wait ,'IN')

    return redirect('/')
           
@app.route('/primeOUT', methods = ['POST'])
def primeOUT():
    value = request.form['time_OUT']
    wait = int(value)
    prime_pumps(wait ,'OUT')       
    return redirect('/')
           
@app.route('/start_run', methods = ['POST'])
def start_run():
    global run
    run = True
    return redirect('/')

@app.route('/finish', methods = ['POST'])
def finish():
    return render_template('verify.html')

@app.route('/end_run', methods = ['POST'])
def end_run():
    global run
    run = False
    #response = request.form['answer']
    #print (response)
    #if response == 'yes':
    #    return render_template('email.html')
    #if response == 'no':
    return redirect('/')

@app.route('/powerOFF', methods=['POST'])
def powerOFF():
    call("sudo shutdown --poweroff", shell=True)
    return redirect('/')

@app.route('/email', methods = ['POST'])
def email():
    global sendto
    global run
    sendto = request.form['email']
#     print (emailto)
    run = False
    return redirect('/')
#     return render_template('goodbye.html')
 