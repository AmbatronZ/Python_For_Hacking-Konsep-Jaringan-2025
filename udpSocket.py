import socket

target_host = "192.168.18.110"
target_port = 9997

client = socket.socket (socket.AF_INET, socket.SOCK_DGRAM) #udp
#untuk mengirim data
client.sendto(b"Test aja kok bang",(target_host, target_port))

#untuk menerima data
data, addr = client.recvfrom(4096)
print("Pesan dari server: \"{}\"".format(data.decode()))

client.close()
