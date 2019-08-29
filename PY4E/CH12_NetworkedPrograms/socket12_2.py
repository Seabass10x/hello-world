# Exercise 12.2
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

count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:break
    prcount = 3000 - count
    count = count + len(data)
    if count <= 3000:
        print(data.decode(),end='')
    elif prcount <= 0:
        continue
    else:
        print(data.decode()[:prcount],end='\r\n')
print(count)

mysock.close()
