#!/usr/bin/python3

import smtplib
from subprocess import PIPE, run
import configparser
from datetime import date

DATE =  str(date.today())
logfile = open("log.txt", "a")

def send(data_to_send: str):
    try:
        try:
            creds = configparser.ConfigParser()
            creds.read("creds.ini")
            username = creds.get("creds", "username")
            password = creds.get("creds", "password")
        except configparser.Error:
            # TODO write to log that no config found, abort
            logfile.write(DATE + " creds not found\n")
            logfile.close()

        to = "pizzapwr@gmail.com"
        subject = "Server Info " + DATE
        body = data_to_send

        final_message = 'Subject: {}\n\n{}'.format(subject, body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, to, final_message)
        logfile.write(str(date.today()) + " success\n")
        logfile.close()
    except:
        logfile.write(str(date.today()) + " failure\n")
        logfile.close()


def out(command_to_execute: str):
    result = run(command_to_execute, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout


data = ""

commands = ["uptime", "users", "df -h", "cat /proc/mdstat", "apcaccess"]

for command in commands:
    data += "\n" + out(command)

send(data)
