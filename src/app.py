import argparse
from funcs.console import console_print
from funcs.email import email_send
from time import time, sleep




parser=argparse.ArgumentParser()
parser.add_argument('--interval')
parser.add_argument('--where')
args=parser.parse_args()



while True:
    sleep(int(args.interval) - time() % int(args.interval))
    if(args.where =="email"):
        email_send()
    else:
        console_print()
    


    









