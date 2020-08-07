# server-data

This is a simple script to get some stats on my home server, and then email them to me.

# usage

Create a config.ini file in the same directory as the script with the following contents

[creds]<br>
username = *putusernamehere*<br>
password = *putpasswordhere*<br>

[recipient]<br>
recipient = *putemailrecipienthere*<br>

After that, set up a cron job to run the script at whatever interval you'd like. 
