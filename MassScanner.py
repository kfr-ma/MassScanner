#!/usr/bin/python3

import sys
import os.path
import getpass
import socket
import itertools

VERSION = "1.0.0"

def kippo_test(host):
    port = 22
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    banner = s.recv(1024)
    s.send('\n\n\n\n\n\n\n\n')
    response = s.recv(1024)
    s.close()
    if "168430090" in response:
        return 1
    else
        return 0

def ip_range(input_string):
    octets = input_string.split('.')
    chunks = [list(map(int, octet.split('-'))) for octet in octets]
    ranges = [range(c[0], c[1] + 1) if len(c) == 2 else c for c in chunks]

    for address in itertools.product(*ranges):
        yield '.'.join(map(str, address))

if __name__ == '__main__':
    username = getpass.getuser()
    ans = True
    print("MassScanner v" + str(VERSION) + " - Github: http://github.com/LuckiestMan/MassScanner")
    print("type help for showing list of commands")
    while ans:
        ans = input(username + "@MassScanner> ")
        ans = ans.split(' ')
        if ans[0] == "generate" and len(ans) >= 2:
            if os.path.exists(ans[1]):
                os.remove(ans[1])
            db = open(ans[1], "w")
            total = 0
            if len(ans) == 3:
                for address in ip_range(ans[2]):
                    db.write(address + "\n")
                    total = total + 1
            else:
                for address in ip_range("5.0-255.0-255.0-255"):
                    db.write(address + "\n")
                    total = total + 1
            print(str(total) + " ips writed in " + ans[1])
            db.close()
        elif ans[0] == "rpot" and len(ans) == 4:
            if ans[1] == "kippo":
                if os.path.exists(ans[2]):
                    db = open(ans[3], "w")
                    with open(ans[1]) as f:
                        for line in f:
                            if kippo_test(line) == 1:
                                print(line + " is a kippo honeypot !")
                            else:
                                db.write(line)
                                print(line + " is not a kippo honeypot !")
                        f.close
                    db.close()
                else
                    print("Invalid filename")
            else:
                print("Invalid type")
        elif ans[0] == "hpot" and len(ans) == 4:
            if ans[1] == "kippo":
                if os.path.exists(ans[2]):
                    db = open(ans[3], "w")
                    with open(ans[1]) as f:
                        for line in f:
                            if kippo_test(line) == 1:
                                db.write(line)
                                print(line + " is a kippo honeypot !")
                            else:
                                print(line + " is not a kippo honeypot !")
                        f.close
                    db.close()
                else
                    print("Invalid filename")
            else:
                print("Invalid type")
        elif ans[0] == "alive" and len(ans) == 3:
            if os.path.exists(ans[1]):
                db = open(ans[2], "w")
                with open(ans[1]) as f:
                    for line in f:
                        try:
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(0.2)
                            result = sock.connect_ex((line,80))
                            if result == 0:
                                db.write(line)
                                print(line + " is alive")
                            else:
                                print(line + " is not open")
                            sock.close()
                        except socket.error:
                            print("Invalid ip: " + line)
                    f.close
                db.close()
            else:
                print("Invalid filename")
        elif ans[0] == "port" and len(ans) == 4:
            if os.path.exists(ans[1]):
                if int(ans[3]) > 1 and int(ans[3]) < 65535:
                    db = open(ans[2], "w")
                    with open(ans[1]) as f:
                        for line in f:
                            try:
                                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                sock.settimeout(0.2)
                                result = sock.connect_ex((line,int(ans[3])))
                                if result == 0:
                                    db.write(line)
                                    print(line + ":" + ans[3] + " is open")
                                else:
                                    print(line + ":" + ans[3] + " is not open")
                                sock.close()
                            except socket.error:
                                print("Invalid ip: " + line)
                        f.close
                    db.close()
                else:
                    print("Invalid port")
            else:
                print("Invalid filename")
        elif ans[0] == "exit":
            print("Have a nice day !")
            sys.exit(0)
        elif ans[0] == "info":
            print("MassScanner v" + str(VERSION) + " - Github: http://github.com/LuckiestMan/MassScanner")
            print("type help for showing list of commands")
        elif ans[0] == "help":
            print("help: this dialog")
            print("exit: quit MassScanner")
            print("generate <filename> [ip range: 82-83.0-255.0-255.0.255]: generate ip list from a range (default: 5.0.0.0 to 5.255.255.255)")
            print("port <filename> <output> <port>: generate open port ip list from another ip list")
            print("alive <filename> <output>: generate alive ip list from another ip list")
            print("hpot <type: kippo> <filename> <output>: generate a list with only honeypots ip")
            print("rpot <type: kippo> <filename> <output>: generate a list without honeypots ip")
        else:
          print("Error: command not found, type help for showing a list of valid commands")
          ans = True
