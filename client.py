import socket
import sys
from M2Crypto import X509
import random

p = 587
g = 23
x = random.randint(9,p)

def genPubKey():
#       p = 6700417
#       g = 524287
        y = (pow(g,x))%p

        print 'public key =',y

        return y

def genShrdKey(serv_pub_key):
        shrd_key = (pow(clnt_pub_key,x))%p
        print "shared key =",shrd_key

def validateCertificate():
        server_cert = ("certificates/server-certificate.crt")
        CA_cert = ("certificates/ashkan-certificate.crt")
        print ("Validating certificate")
        lserv_cert = X509.load_cert(server_cert)
        lCA_cert = X509.load_cert(CA_cert)
        key = lCA_cert.get_pubkey()

        if lserv_cert.verify(key) == 1:
                print ("valid")
        else:
                print ("invalid")


s = socket.socket()

port = 1123

f = open('fromserver.crt','wa')
s.connect(('',port))

while True:
        data = s.recv(1024)
        print data
        f.write(data)
        if not data:
                break
f.close()
print "Received Certificate"
validateCertificate()
pub_key = genPubKey()

serv_pub_key = (s.recv(10))
print serv_pub_key
s.send(str(pub_key))

genShrdKey(int(serv_pub_key))

s.close()
