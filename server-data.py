#!/usr/bin/python3

import smtplib
from subprocess import PIPE, run
import configparser
from datetime import date

DATE = str(date.today())
LOGFILE = open("config.txt", "a")


def send(data_to_send: str):
    try:
        try:
            creds = configparser.ConfigParser()
            creds.read("config.ini")
            username = creds.get("creds", "username")
            password = creds.get("creds", "password")
            recipient = creds.get("recipient", "recipient")

            try:
                subject = "Server Info " + DATE
                body = data_to_send
                final_message = 'Subject: {}\n\n{}'.format(subject, body)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(username, password)
                server.sendmail(username, recipient, final_message)
                LOGFILE.write(str(date.today()) + " report success\n")
                LOGFILE.close()

            except smtplib.SMTPException:
                LOGFILE.write(str(date.today()) + "email error\n")

        except configparser.Error:
            LOGFILE.write(DATE + " creds not found\n")
            LOGFILE.close()

    except:
        LOGFILE.write(str(date.today()) + " generic failure\n")
        LOGFILE.close()


def out(command_to_execute: str) -> str:
    result = run(command_to_execute, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout

# build list of commands to email, add commands to data[] as needed
data = ""
commands = ["uptime", "users", "last -10", "df -h", "cat /proc/mdstat",
            "apcaccess"]
for command in commands:
    data += "\n" + out(command)

send(data)