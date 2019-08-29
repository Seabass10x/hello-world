# Exercise 12.5
import socket

url = input('Enter URL: ')
urlcomponents = url.split('/')
try:
    host = urlcomponents[2]
except:
    print('URL not formatted properly')
    quit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((host, 80))
except:
    print('URL invalid or does not exist')
    quit()
cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()
mysock.send(cmd)

full = []
while True:
    data = mysock.recv(512)
    if not data: break
    full.append(data.decode())
mysock.close()

full = "".join(full)
body = full.partition('\r\n\r\n')[2]
print(body)
