import random
import socket
import threading


SERVER = "localhost", 12345


class Server:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM - TCP сокет
        self.sock.bind(("localhost", 12345))
        self.clients = {}
        print("Start Server")

    def serve(self):
        while True:
            data, addres = self.sock.recvfrom(1024)
            print(addres[0], addres[1])

            if addres not in self.clients:
                self.register(addres, data)

            self.change_alias(data, addres)

            if self.disconnect(data, addres):
                alias = self.clients[addres]
                self.clients.pop(addres)
                self.send_to_client(addres, "You have been disconected.".encode("utf-8"))
                self.send_all_clients_besides(addres, f"User {alias} has been disconected.".encode('utf-8'))


            print(f"{addres} | {self.clients[addres]} | {data}")
            self.send_all_clients_besides(addres, data)

    def disconnect(self, data: bytes, addres):
        if not data.decode('utf-8').startswith('/CLOSE'):
            self.


    def register(self, addres, data: bytes):
        self.clients[addres] = data.decode('utf-8')

    def send_to_client(self, addres, data):
        self.sock.sendto(data, addres)

    def send_all_clients_besides(self, besides_addres, data):
        for client in self.clients:
            if client == besides_addres:
                continue
            threading.Thread(target=self.send_to_client, args=(client, data)).start()

    def change_alias(self, data: bytes, addres):
        if not data.decode('utf-8').startswith('/CHANGE_ALIAS'):
            return

        message = data.decode('utf-8')

        new_alias = message[14:]
        old_alias = self.clients[addres]

        if len(new_alias) > 0:
            self.clients[addres] = new_alias

        self.send_all_clients_besides(addres, f"Member {old_alias} changed alias to {new_alias}".encode('utf-8'))

        return True


class Client:
    def read_sok(sor):
        while True:
            data = sor.recv(1024)
            print(data.decode("utf-8"))

    def __init__(self, alias: str, server: (str, int)):
        self.alias = alias or random.randint(0, 10000)
        self.server = server

        self.connect()

    def connect(self):
        self.sor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM - TCP сокет
        self.sor.bind(("", 0))
        self.sor.sendto((self.alias).encode("utf-8"), self.server)

        potok = threading.Thread(target=Client.read_sok(self.sor))
        potok.start()

    def send(self, msg: str):
        self.sor.sendto(msg.encode("utf-8"), self.server)

    def disconnect(self):
        self.sor.sendto("/CLOSE".encode("utf-8"), self.server)

    def change_alias(self, new_alias: str):
        self.alias = new_alias
        self.sor.sendto((f"/CHANGE_ALIAS {new_alias}").encode("utf-8"), self.server)
