from socketserver import TCPServer, BaseRequestHandler
from time import sleep
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class TCPEchoHandler(BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        self.request.send(self.data)


def start_server():
    server = TCPServer(('localhost', 12345), TCPEchoHandler)
    server.serve_forever()


def send_msg(id):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 12345))
    s.send(str(id).encode())
    print(s.recv(1024).strip())


if __name__ == "__main__":
    Thread(target=start_server).start()

    sleep(0.3)

    while True:
        for t in range(10):
            Thread(target=send_msg, args=(str(t))).start()

        sleep(1)
