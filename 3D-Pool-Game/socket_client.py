import socket
HOST = '192.168.56.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    try:
        msg = input("Please input msg:")
        s.send(msg.encode('utf-8'))
        data = s.recv(1024).decode("utf-8") 
        print(data)
    except Exception as inst:
        print('error:',inst)
#s.close()
