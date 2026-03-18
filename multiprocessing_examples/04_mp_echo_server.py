"""
Многопроцессный TCP эхо-сервер.

Каждое подключение клиента обрабатывается в отдельном процессе ОС
(аналог многопоточного сервера из lab 2, но с multiprocessing.Process
вместо threading.Thread).

Задание:
  TODO 9 — реализовать тело handle_client (recv, лог, sendall, close)

Запуск:
    python3 04_mp_echo_server.py

Для проверки используйте клиент 05_mp_echo_client.py (в другом терминале).
Откройте 2–3 терминала с клиентами одновременно и обратите внимание
на PID каждого обработчика — они будут разными.
"""

import os
import socket
from multiprocessing import Process

HOST = '127.0.0.1'
PORT = 9096


def handle_client(conn, addr):
    """Обработка одного клиента в отдельном процессе."""

    # TODO 9: Реализуйте обработку клиента:
    #
    # 1. Выведите PID текущего процесса:
    #        print(f"[PID {os.getpid()}] Клиент {addr} подключён")
    #
    # 2. Прочитайте данные от клиента:
    #        data = conn.recv(1024)
    #
    # 3. Выведите полученное сообщение:
    #        print(f"[PID {os.getpid()}] Получено: '{data.decode()}'")
    #
    # 4. Отправьте данные обратно (эхо):
    #        conn.sendall(data)
    #
    # 5. Закройте соединение:
    #        conn.close()
    #        print(f"[PID {os.getpid()}] Клиент {addr} отключён")

    # --- Ваш код здесь ---
    pass
    # --- Конец вашего кода ---


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"[PID {os.getpid()}] Сервер запущен на {HOST}:{PORT}")
    print("Ожидание подключений... (Ctrl+C для остановки)\n")

    try:
        while True:
            conn, addr = server_socket.accept()
            p = Process(target=handle_client, args=(conn, addr))
            p.start()
            conn.close()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server_socket.close()
