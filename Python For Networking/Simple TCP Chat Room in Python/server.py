import threading
import socket

HOST = 'localhost'
PORT = 13377

clients = []
addresses = []


SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))
SERVER.listen()





def broadcast(message):
    for client in clients:
        client.send(message)
    
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            address = addresses[index]
            broadcast(f"{address} left the chat!".encode())
            addresses.remove(address)
            break

def receive():
    while True:
        client, address = SERVER.accept()
        print(f"Connected with {str(address)}")

        clients.append(client)
        addresses.append(address)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()