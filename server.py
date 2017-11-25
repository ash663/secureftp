import os
import socket
import re
import hashlib
import time

def genPublicKey():
#       p = 6700417
#       g = 524287
	publicKey = (pow(g, randomNumber)) % p
	#print 'Public key =',y
	return publicKey

def genSharedKey(clientPublicKey):
	sharedKey = (pow(clientPublicKey, randomNumber)) % p
	#print "shared key =",shrd_key

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
                timeStamp=str(time.time())
                hashedTimeStamp = hmac.new(secret, msg=timeStamp, digestmod=hashlib.sha1).hexdigest()
                #msg is epoch time
                with open(fileName, 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        encryptedFile = encryptedFile + (data ^ hashedTimeStamp)
                #encryptedFile = m.hexdigest()
                macOfFile = hmac.new(secret.reverse(), encryptedFile+timeStamp, digestmod=hashlib.sha1).hexdigest()
                fileToSend = encryptedFile+timeStamp+macOfFile
                #Write code to send file
        elif re.search('upload', request):
            fileName=request.split(':')[1]
        #conn.sendall(reply)

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

#For DH
p = 587
g = 23
randomNumber = random.randint(9, p)

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
    publicKey = genPublicKey()
    conn.send(publicKey)
    clientPublicKey = (conn.recv(1024))
    genSharedKey(int(clientPublicKey))
    start_new_thread(incoming_connection ,(conn,))
