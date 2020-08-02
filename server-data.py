#!/usr/bin/python3

import os
import smtplib
import paramiko

def validate_key(key_path):
    """ Validate a key

        :param key_path: path to a key to use for authentication
        :type key_path: str

        :return: key object used for authentication
        :rtype: paramiko.RSAKey
    """

    key_path = os.path.expanduser(key_path)

    if not os.path.isfile(key_path):
        return False

    return paramiko.RSAKey.from_private_key_file(key_path)


# TODO try/except load from user input or popup somehow?
key = validate_key('/home/user/.ssh/id_rsa')
client = paramiko.SSHClient()
# TODO don't use this, doesn't protect from Mitm attackes
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("Connecting")
    client.connect(hostname="desktop", username="user", password="",
                   pkey=client.load_host_keys('/home/user/.ssh/id_rsa.pub'))
    # TODO success function
    print("Success")

except ConnectionError:
    # TODO using negative print statement
    print("Connection Error")

# TODO run script
# TODO format script
# TODO write to file
# TODO email script

commands = ["uptime", "users", "df -h", "cat /proc/mdstat", "apcaccess"]
for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read())

client.close()g