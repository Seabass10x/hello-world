# Exercise 12.1
import socket

url = input('Enter URL: ')
urlcomponents = url.split('/')
#print(urlcomponents)
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

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
