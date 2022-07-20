import socket

listner=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listner.setsockopt(socket.SOL_SOCKET,socket.SO_RUSEADDR,1)
listner.bind("192.168.1.14",4444)
listner.listen(0)