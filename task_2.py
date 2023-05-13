import socket
import math


HOST = '127.0.0.1'

PORT = 2345


def start_server():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for connection:")

    while True:
        client_sock, client_addr = s.accept()
        print(f"Connected by: {client_addr}")

        client_sock.send("\nВведите число: \n".encode())
        data = client_sock.recv(1024)
        number = int(data.decode().strip())
        if number >= 50000:
            client_sock.send('Число слишком большое. Попробуете еще раз\n'.encode())
        else:
            result = math.factorial(number)
            client_sock.send(f'Результат = {str(result)}\n'.encode())
        client_sock.close()


if __name__ == '__main__':
    start_server()