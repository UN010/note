#Ӧ��ʵ���ķ�������
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #����Socket����
sock.bind(('localhost', 8001)) #������IP��˿ں�
sock.listen(5) #��ʼ����
while True:
    connection, address = sock.accept() #
    try:
        connection.settimeout(5) #��5�������������
        buf = connection.recv(1024)
        if buf == '1':
            connection.send('lkafds')
        else:
            connection.send('false')
    except socket.timeout:
        print 'time out'
    connection.close()
sock.close()