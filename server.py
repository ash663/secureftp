import os
import socket
import re
import hashlib
import time

def incoming_connection(conn):
    #Send certificate
    conn.send(certificate)
    while True:
        #Receiving from client
        request = conn.recv(1024)
        #Note: Below, may be you can check type of request, then decide download or upload
        '''Check if request is upload/download
        If download:
            check if fileName exists
            if doesn't exist, break out of loop, send 404 error
            if exists, encrypt the file and send it.
        If upload:
            accept file, and store after doing necessary decryption'''
        if re.search('download', request):
            fileName=request.split(':')[1]
            #add code to check if file exists
            if os.path.isfile(fileName):
                #File exists. Now encrypt the file.
                #Encryption algo: Hash Timestamp. XOR with File. But, in blocks.
                hashedTimeStamp = hmac.new(secret, msg=time.time(), digestmod=hashlib.sha1).hexdigest()
                #msg is epoch time
                with open(fileName, 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        encryptedFile = encryptedFile + (data ^ hashedTimeStamp)
                encryptedFile = m.hexdigest()

        elif re.search('upload', request):
            fileName=request.split(':')[1]
        conn.sendall(reply)

    #came out of loop
    conn.close()

#Used for hashing and encrypting
BUF_SIZE = 65536
sha1 = hashlib.sha1() #Probably gotta change this, as not needed. Better to be done file-wise
secret = 'abcdefghijkl' #Use shared secret key later
#For opening a connection with client. Can make it work for multiple clients by select or threading
PORT=4999
PORT=PORT+1
HOST=""
#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #Bind socket to port
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
s.listen(10)

while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(incoming_connection ,(conn,))
