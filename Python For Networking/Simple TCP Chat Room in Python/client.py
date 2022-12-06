import threading
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 13377))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(input('Enter your nickname: ').encode())
            else:
                print(message)
        except:
            print('An error occured!')
            client.close()
            break

def write():
    while True:
        message = f'{input(">> ")}'
        client.send(message.encode())
        


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
