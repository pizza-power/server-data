#!/usr/bin/python3

import smtplib
from subprocess import PIPE, run
import configparser


def send(data_to_send: str):
    try:
        try:
            creds = configparser.ConfigParser()
            creds.read("creds.ini")
            username = creds.get("creds", "username")
            password = creds.get("creds", "password")
        except configparser.Error:
            # TODO write to log that no config found, abort
            print("error opening creds")

        to = "pizzapwr@gmail.com"
        subject = "Test Email"
        body = data_to_send

        final_message = 'Subject: {}\n\n{}'.format(subject, body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, to, final_message)
        print("success")

    except:
        # TODO write to log files instead
        print("Error sending email")


def out(command_to_execute: str):
    result = run(command_to_execute, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout


data = ""

commands = ["uptime", "users", "df -h", "cat /proc/mdstat", "apcaccess"]

for command in commands:
    data += "\n" + out(command)

send(data)
