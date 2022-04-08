import os
import re

open_file = open('cert.txt', 'r')
show_file_content = open_file.read()
open_file.close()
lines = show_file_content.splitlines()

if os.path.exists("tls.cert") :
    print("Updating existing .cert file")
    os.remove("tls.cert")
else:
    print("Creating New .cert file")

if os.path.exists("tls.key"):
    print("Updating existing .key file")
    os.remove("tls.key")
else:
    print("Creating New .key file")

start_with = re.compile("^(-)+(beginning)(-)+$", re.IGNORECASE)
end_with = re.compile("^(-)+(ending)(-)+$", re.IGNORECASE)

file_state = 0
create_cert_file = open("tls.cert", "a")
create_key_file = open("tls.key", "a")
for i in range(len(lines)):
    if  end_with.match(lines[i]):
        file_state = 2
    elif file_state == 3:
        create_key_file.write(lines[i]+"\n")
    elif file_state == 1:
        create_cert_file.write(lines[i]+"\n")
    elif start_with.match(lines[i]):
        file_state += 1
create_cert_file.close()
create_key_file.close()
