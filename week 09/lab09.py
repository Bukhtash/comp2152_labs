import os
import sys
import platform
import threading
import time
import unittest


# ============================================================
# Q1 — SYSTEM INFORMATION REPORTER
# ============================================================


def get_system_info():
    return {
        "os": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "machine": platform.machine(),
    }


def get_python_info():
    return {
        "version": sys.version,
        "executable": sys.executable,
        "platform": sys.platform,
    }


def get_directory_info(path):
    exists = os.path.exists(path)

    return {
        "path": os.path.abspath(path),
        "exists": exists,
        "file_count": len(os.listdir(path)) if exists else 0,
        "is_directory": os.path.isdir(path),
    }


def run_q1():
    print("=" * 60)
    print("SYSTEM INFORMATION REPORTER")
    print("=" * 60)

    print("\n--- System Info ---")
    for k, v in get_system_info().items():
        print(f"{k:12}: {v}")

    print("\n--- Python Info ---")
    for k, v in get_python_info().items():
        print(f"{k:12}: {v}")

    print("\n--- Directory Info ---")
    for k, v in get_directory_info(".").items():
        print(f"{k:12}: {v}")

    print("=" * 60)


# ============================================================
# Q2 — THREADING
# ============================================================


def simulate_task(name, duration, lock):
    lock.acquire()
    print(f"[START] {name}")
    lock.release()

    time.sleep(duration)

    lock.acquire()
    print(f"[DONE]  {name} ({duration}s)")
    lock.release()


def run_sequential(tasks, lock):
    for name, duration in tasks:
        simulate_task(name, duration, lock)


def run_threaded(tasks, lock):
    threads = []

    for name, duration in tasks:
        t = threading.Thread(target=simulate_task, args=(name, duration, lock))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


def run_q2():
    print("\n" + "=" * 60)
    print("SEQUENTIAL vs THREADED EXECUTION")
    print("=" * 60)

    tasks = [("Brew Coffee", 3), ("Toast Bread", 2), ("Fry Eggs", 4)]

    lock = threading.Lock()

    print("\n--- Running SEQUENTIALLY ---")
    start = time.time()
    run_sequential(tasks, lock)
    end = time.time()
    seq_time = end - start
    print(f"Sequential time: {seq_time:.2f} seconds")

    print("\n--- Running with THREADS ---")
    start = time.time()
    run_threaded(tasks, lock)
    end = time.time()
    thr_time = end - start
    print(f"Threaded time: {thr_time:.2f} seconds")

    print("=" * 60)


# ============================================================
# Q3 — FUNCTIONS TO TEST
# ============================================================


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False

    for p in parts:
        if not p.isdigit():
            return False
        n = int(p)
        if n < 0 or n > 255:
            return False

    return True


def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


# ============================================================
# Q3 — UNIT TESTS
# ============================================================


class TestCelsius(unittest.TestCase):
    def test_freezing(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_boiling(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)


class TestValidIP(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid_ip("192.168.1.1"))

    def test_invalid_octet(self):
        self.assertFalse(is_valid_ip("256.1.1.1"))

    def test_too_few_parts(self):
        self.assertFalse(is_valid_ip("1.2.3"))

    def test_empty(self):
        self.assertFalse(is_valid_ip(""))


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(7), "7")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    run_q1()
    run_q2()

    print("\nRunning Unit Tests...\n")
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
