import os
import socket

def incoming_connection(conn):
    #Send certificate
    conn.send(certificate)
    while True:
        #Receiving from client
        request = conn.recv(1024)
        '''Check if request is upload/download
        If download:
            check if fileName exists
            if doesn't exist, break out of loop, send 404 error
            if exists, encrypt the file and send it.
        If upload:
            accept file, and store after doing necessary decryption'''

        conn.sendall(reply)

    #came out of loop
    conn.close()

PORT=4999
PORT=PORT+1
HOST=""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
s.listen(10)

while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(incoming_connection ,(conn,))
