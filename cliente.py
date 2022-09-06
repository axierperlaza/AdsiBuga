host = '172.18.12.184'
port = 3306
import socket

obj = socket.socket()

obj.connect((host, port))
print("Conectado al servidor")

while True:

    mens = input("Mensaje desde Cliente a Servidor : ")

    obj.send(mens.encode('ascii'))
    
    recibido = obj.recv(1024)
    print(recibido)

    
    

    print("Conexión cerrada")

obj.close()