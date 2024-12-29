#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import threading
import queue
import time


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def producer(num_queue, count):
    for i in range(count):
        number = i
        print(f"Производитель: сгенерировано число {number}")
        num_queue.put(number)
        time.sleep(1)
    num_queue.put(None)


def consumer(num_queue):
    while True:
        number = num_queue.get()
        if number is None:
            break
        print(f"Потребитель: вычисление Фибоначчи для {number}")
        result = fibonacci(number)
        print(f"Потребитель: Фибоначчи({number}) = {result}")


def main():
    num_queue = queue.Queue()
    producer_thread = threading.Thread(target=producer, args=(num_queue, 10))
    consumer_threads = []

    for _ in range(3):
        thread = threading.Thread(target=consumer, args=(num_queue,))
        consumer_threads.append(thread)
        thread.start()

    producer_thread.start()
    producer_thread.join()

    for _ in consumer_threads:
        num_queue.put(None)
    for thread in consumer_threads:
        thread.join()


if __name__ == "__main__":
    main()