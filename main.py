import socket
from threading import Thread

# HOST = 'nearbyfuture.com'  # or 127.0.0.1
HOST = 'localhost'  # or 127.0.0.1
PORT = 10015


def receive_proc(s):
    while True:
        try:
            msg = s.recv(1024)
            print(msg.decode('utf-8'))
        except socket.error:
            break


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Connected")
    # s.send("Test".encode('utf-8'))
    server_hello = s.recv(1024)
    print(server_hello.decode('utf-8'))
    name = input()
    s.send(name.encode('utf-8'))
    receive_thread = Thread(target=receive_proc, kwargs={'s': s})
    receive_thread.start()
    while True:
        msg = input()
        try:
            s.send(msg.encode('utf-8'))
        except Exception as e:
            break

    s.close()


if __name__ == '__main__':
    main()