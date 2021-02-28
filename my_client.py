import json
from socket import *
import click
import time

unix_timestamp  = int("1284101485")
utc_time = time.gmtime(unix_timestamp)
local_time = time.localtime(unix_timestamp)
# print(time.strftime("%Y-%m-%d %H:%M:%S", local_time))
# print(time.strftime("%Y-%m-%d %H:%M:%S+00:00 (UTC)", utc_time))


 # @click.command()
 # @click.option('-- addr', help =('Number of greetings.'))
 # @click.option('-- port', default = 7777, help=('Person to greet.'))
 #
 # def hello(addr, port ):
 #
 #     for x in range(addr):
 #         click.echo('Hello server %s!' % port)
#
#  if __name__ == '_main_':
#      hello()
#

ENCODING = 'utf-8'

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(('', 8008))

    auth_msg = {
        "action": "authenticate",
        "time":12345, #local_time,
        "user": {
        "account_name":"PapaMama",
        "password": "CorrectHorseBatteryStaple"
         }
}

    msg = json.dumps(auth_msg)
    s.send(msg.encode(ENCODING))
    data = s.recv(1000000)
    recv_str = data.decode(ENCODING)
    print("Massage from 'Server': ", recv_str, 'len = ', len(data), 'bt')

    recv_msg = json.loads(recv_str)
    print(f'msg {recv_msg}')

