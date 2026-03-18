"""
TCP-клиент для тестирования многопроцессного эхо-сервера (04_mp_echo_server.py).

Этот файл готов к использованию — TODO нет.
Откройте несколько терминалов и запустите этот клиент в каждом,
чтобы увидеть, что сервер создаёт отдельный процесс для каждого клиента.

Запуск (сервер 04_mp_echo_server.py должен быть запущен в другом терминале):
    python3 05_mp_echo_client.py
"""

import socket

HOST = '127.0.0.1'
PORT = 9096


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            message = "Привет от клиента!"
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Отправлено: '{message}' -> Получено: '{data.decode()}'")
    except ConnectionRefusedError:
        print("Ошибка: не удалось подключиться к серверу.")
        print("Убедитесь, что сервер 04_mp_echo_server.py запущен в другом терминале.")


if __name__ == '__main__':
    main()
