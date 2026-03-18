"""
Справочный пример: создание процессов с помощью multiprocessing.

Этот файл демонстрирует базовые операции:
- создание процесса (Process)
- запуск (start) и ожидание завершения (join)
- получение PID текущего и родительского процесса

Запуск:
    python3 01_basic_process.py
"""

import os
import time
from multiprocessing import Process, current_process


def worker(task_name, duration):
    """Функция, выполняемая в отдельном процессе."""
    print(f"[{current_process().name}] Начало задачи '{task_name}' "
          f"(PID={os.getpid()}, родитель={os.getppid()})")
    time.sleep(duration)
    print(f"[{current_process().name}] Задача '{task_name}' завершена "
          f"за {duration} сек")


if __name__ == '__main__':
    print(f"Главный процесс: PID={os.getpid()}\n")

    processes = []
    tasks = [("Загрузка данных", 2), ("Обработка", 3), ("Сохранение", 1)]

    for name, dur in tasks:
        p = Process(target=worker, args=(name, dur))
        processes.append(p)

    start_time = time.time()

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    elapsed = time.time() - start_time
    print(f"\nВсе процессы завершены за {elapsed:.2f} сек")
    print("(Последовательно это заняло бы ~6 сек)")
