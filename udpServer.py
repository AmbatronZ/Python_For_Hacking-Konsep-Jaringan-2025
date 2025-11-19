import socket

localIp = "192.168.18.110"
localPort = 9997
buffer = 1024

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((localIp, localPort)) #untuk menyalakan server UDP

print("Server Up")

#listening
while(True):
    data = serverSocket.recvfrom(buffer)
    pesan = data[0]
    ip_addr = data[1]

    print ("Pesan dari client: \"{}\"".format(pesan))
    print ("Ip Client: \"{}\"".format(ip_addr))

    serverSocket.sendto(b"Selamat datang di UDP server", ip_addr)

