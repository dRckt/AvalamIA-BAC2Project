import socket
import json
import time

port = 3001
s = socket.socket()
s.connect((socket.gethostname(), port))

matricules = ["19190", "20200"]
name = "Ave Cesar"

msg = {"matricules": matricules,
       "port": 3040,
       "name": name}

def sendJSON(socket, data):
	msg = json.dumps(data).encode('utf8')
	total = 0
	while total < len(msg):
		sent = socket.send(msg[total:])
		total += sent
def recvJSON(socket):
	finished = False
	msg = ''
	while not finished:
		msg += socket.recv(4096).decode('utf8')
		try:
			data = json.loads(msg)
			finished = True
		except json.JSONDecodeError:
			pass
	return data

sendJSON(s, msg)
print(recvJSON(s))


time.sleep(3)