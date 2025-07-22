#!/bin/python3

import time
import threading
import subprocess

class Loader:
    def __init__(self, desc="Exploits && options yozilmoqda...", end="Exploits && options yozildi! Bir oz kuting...", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout
        self._running = False
        self._thread = None
        self.spinner = "|/-\\"

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._animate)
        self._thread.start()

    def _animate(self):
        idx = 0
        while self._running:
            print(f"\r{self.desc} {self.spinner[idx % len(self.spinner)]}", end="", flush=True)
            idx += 1
            time.sleep(self.timeout)

    def stop(self):
        self._running = False
        self._thread.join()
        print(f"\r{self.end}{' ' * 20}")  # clear qator

# Eksploitlarni o‘qish
with open("search_result.txt", "r") as file:
    exploits = [line.strip() for line in file if line.strip()]

# Loader boshlash
loader = Loader()
loader.start()

# all_options.rc faylini yaratish
with open("all_options.rc", "w") as rc:
    for exploit in exploits:
        rc.write(f"use {exploit}\n")
        rc.write("show options\n")
    rc.write("exit\n")

# msfconsole orqali optionslarni olish
try:
    subprocess.run(["msfconsole", "-q", "-r", "all_options.rc"], stdout=open("see_option_result.txt", "w"), stderr=subprocess.DEVNULL)
except Exception as e:
    print(f"\nXatolik: {e}")

# Loader to‘xtatish
loader.stop()
