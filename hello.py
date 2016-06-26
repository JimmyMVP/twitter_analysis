#create an INET, STREAMing socket
import socket
import json

address = "pysocket"

try:
    
    s = socket.socket(
    socket.AF_UNIX, socket.SOCK_STREAM)

except socket.error:
    print ('Failed to create socket. Error code: ' + socket.error + ' , Error message : ' + socket.error)
    sys.exit();

try:
    s.bind(address)
except socket.error:
    print("Bind failed " + str(socket.error))


s.listen(1000)
print("Listening on addr : " + str(address))
while(True):
    try:
        conn, addr = s.accept()
        print("Connected: " + addr)
        s.send(json.dumps({"msg" : "Hello from Python"}))
    except Exception:
        pass