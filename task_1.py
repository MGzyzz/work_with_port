import socket
import random



HOST = '127.0.0.1'
PORT = 1234


def start_sever():
    massive = [
        'Ты не несешь отвественности за то, чего ждут от тебя другие люди. Если от тебя ждут слишком многого, то это их ошибка, а не твоя вина.\n',
        'Мы становимся тем, о чем думаем больше всего. Поэтому следует стараться думать только о хорошем.\n',
        'Единственный способ делать отличную работу - это любить то, что ты делаешь.\n',
        'Наша жизнь - это то, что наши мысли делают с нами.\n',
        'Изменение начинается с нас самих. Если мы хотим изменить мир, мы должны сначала изменить себя.\n']

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print(f'Waiting for connection:')

    while True:
        client_sock, client_addr = s.accept()
        print(f'Connected by {client_addr}')
        random_1 = random.choice(massive)
        client_sock.send(random_1.encode())
        client_sock.close()


if __name__ == '__main__':
    start_sever()