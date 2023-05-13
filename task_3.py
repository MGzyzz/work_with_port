import socket

HOST = '127.0.0.1'
PORT = 4798


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen()
    print("Waiting for connection:")

    while True:
        client_socket, client_addr = s.accept()
        print(f'Connected by {client_addr}')

        client_socket.send("\nВведите первое число: \n".encode())
        data_one = client_socket.recv(1024)
        client_socket.send("Введите второе число: \n".encode())
        data_two = client_socket.recv(1024)

        number_one = int(data_one.decode().strip())
        number_two = int(data_two.decode().strip())
        client_socket.send(f"Сумма: {str(number_one + number_two)}\n".encode())
        client_socket.send(f"Произведение: {str(number_one * number_two)}\n".encode())
        client_socket.send(f"Разность: {str(number_one - number_two)}\n".encode())
        client_socket.send(f"Частное от деления: {str(number_one / number_two)}\n".encode())
        client_socket.close()



if __name__ == '__main__':
    start_server()