import os
SYSTEM_OS = os.name
print(SYSTEM_OS)
if SYSTEM_OS == 'nt':
    try:
        os.system("py -m pip uninstall nmap")
    except:
        o = 1
    os.system("py ./python-nmap/setup.py install")
    os.system("py -m pip install python-nmap")