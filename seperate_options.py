#!/bin/python3

import json
import time
import threading

# Loader klassi
class Loader:
    def __init__(self, desc="Tekshirilmoqda...", end="Boldi!", timeout=0.1):
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
        print(f"\r{self.end}{' ' * 20}")  # tozalash

# Asosiy qism
with open('see_option_result.txt', 'r') as file:
    context_list = file.readlines()

test_list = []
options_dict = {}

for i in context_list:
    index = i.find("yes")
    if index != -1:
        i = i[:index + 3]
        test_list.append(i)

for i in test_list:
    i = i.split()
    i.pop()
    options_dict[i[0]] = i[1] if len(i) > 1 else ""

for key, value in options_dict.items():
    print(f"{key} = {value}")
    val = input(f"{key} uchun qiymat kiriting default uchun hech narsa kiritmang: ")
    if val != "":
        options_dict[key] = val

with open("required_argument.json", "w") as file:
    json.dump(options_dict, file)

# Oxirida keyingi bosqichga o'tishda loader
loader = Loader(
    desc="\033[33mKeyingi bosqichga o‘tilmoqda...\033[0m", 
    end="\033[33mBosqich o‘tdi!\033[0m"
)

loader.start()
time.sleep(3)  # Bu yerda 2-3 soniya kutadi (xohlasangiz o‘zgartiring)
loader.stop()
