#socket 小实例 客户端代码
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8001))
time.sleep(2)
sock.send('1')
print sock.recv(1024)
sock.close()