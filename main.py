import socket

HOST = 'localhost'  # or 127.0.0.1
PORT = 10015


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    server_hello = s.recv(1024)
    print(server_hello.decode('utf-8'))
    name = input()
    s.send(name.encode('utf-8'))
    while True:
        msg = input()
        try:
            s.send(msg.encode('utf-8'))
        except Exception as e:
            break

    s.close()


if __name__ == '__main__':
    main()