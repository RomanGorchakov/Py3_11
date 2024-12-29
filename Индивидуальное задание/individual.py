#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import threading
import queue


def calculate_term(x, n, output_queue):
    term = x**n
    output_queue.put(term)


def calculate_series_sum(x, tolerance):
    output_queue = queue.Queue()
    threads = []
    n = 0

    while True:
        thread = threading.Thread(target=calculate_term, args=(x, n, output_queue))
        threads.append(thread)
        thread.start()
        thread.join()

        term = output_queue.get()
        if abs(term) < tolerance:
            break

        n += 1

    series_sum = sum(output_queue.queue)  # Все элементы в очереди

    for thread in threads:
        thread.join()

    return series_sum


if __name__ == "__main__":
    x = 0.7
    tolerance = 1e-6

    series_sum = calculate_series_sum(x, tolerance)
    control_value = 1 / (1 - x)

    print(f"Сумма ряда с точностью {tolerance}: {series_sum}")
    print(f"Контрольное значение функции: {control_value}")
    print(f"Разница: {abs(series_sum - control_value)}")