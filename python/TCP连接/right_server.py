from socket import *
from time import ctime
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('localhost', 21567))
tcpSerSock.listen(5)
while True:
    print 'waiting for connection.....'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...conneced from:', addr
    while True:
        data = tcpCliSock.recv(1024)
        if not data:
            break
        if data=='asd':
            tcpCliSock.send('[%s] %s' % (ctime(), 'qwe'))
        else:
            tcpCliSock.send('[%s] %s' % (ctime(), data))
    tcpCliSock.close()
tcpSerSock.close()
