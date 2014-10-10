'''
Created on Jul 30, 2014

@author: naruto
'''
import conn_ssh
import os
import argparse
import time
import getpass

def credentials():
    username='admin'
    username=raw_input('Username: ')
    password=getpass.getpass()
    return username, passworda
def execute_main(cmd, host_IP, username, password):
    con=conn_ssh.CONN_SSH(cmd=cmd, host_IP=host_IP, user=username, password=password)
    time.sleep(2)
    con.CMD_TO_FILE()
def main():
    parser=argparse.ArgumentParser(description='Connect to a device using SSH, executing a command and sending the output to a file')
    parser.add_argument('-i','--ip_address', type=str, help='IP address to connect')
    parser.add_argument('-c','--command', type=str, help='Command to execute')
    parser.add_argument('-v', '--verbosity', help='still not implemented')
    args = parser.parse_args()
    print args.ip_address
    print args.command
    print('Please enter your credentials')
    username, password=credentials()
    try:
        if not args.ip_address:
            raise Exception('You need to specify the IP address "connect.py --help"')
        elif not args.command:
            raise Exception('You need to specify the command option use "connect.py --help"')
        elif os.path.isfile(args.ip_address):
            print('The IP address is a file')
            if os.path.isfile(args.command):
                print('The command is a file\n', 'Executing all the commands in all the devices:...')
                for ii in open(args.ip_address):
                    for i in open(args.command):
                        execute_main(i, ii, username, password)
            else:
                print('Is just one command to execute in many devices...')
                for i in open(args.ip_address):
                    execute_main(args.command, i, username, password)
                    
        else:
            print('Is an IP address')
            if os.path.isfile(args.command):
                print('The command is a file to execute in one device')
                for i in open(args.command):
                    execute_main(i, args.ip_address, username, password)    
            else:
                print('Is just one command to execute in one device:...')
                execute_main(args.command, args.ip_address, username, password)
    except Exception as X:
        print(X)

if __name__ == '__main__':
    main()
