#应用实例的服务器端
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #生成Socket对像
sock.bind(('localhost', 8001)) #绑定主机IP与端口号
sock.listen(5) #开始监听
while True:
    connection, address = sock.accept() #
    try:
        connection.settimeout(5) #在5秒后调用这个函数
        buf = connection.recv(1024)
        if buf == '1':
            connection.send('lkafds')
        else:
            connection.send('false')
    except socket.timeout:
        print 'time out'
    connection.close()
sock.close()