from threading import Thread
from FileRiter import reports
from Arts import __arts__
import nmap
import random
class nmap_tool():
    art = __arts__()
    rp = reports()
    def __init__(self,all_Tragetes):
        self.Traget = all_Tragetes
        self.dnss = []
        self.ips = []
        print(all_Tragetes)
        for adr in all_Tragetes:
            self.dnss.append(str(adr).split(':')[0])
            self.ips.append(str(adr).split(':')[1])
        self.Servers_OS = []
        self.Servers_Ports_and_Services = []
    def get_AllOpenPorts(self,base,speed = 1):
        self.base = base
        self.ip = self.ips
        for i in range(speed):
            Thread(target=self.scan_Ports()).start()
        return self.Servers_Ports_and_Services
    def scan_Ports(self):
        nm = nmap.PortScanner()
        self.rp.appende_Report("\nNMAP  -sV  :P",self.base,'Sub_Titil')
        while True:
            scan_ip = self.ip[random.randint(0,len(self.ip)-1)]
            self.ip.remove(scan_ip)
            print(scan_ip)
            sc = nm.scan(hosts=str(scan_ip), arguments='-sV --script vulners  -sN -f')
            print(sc['scan'])
            self.rp.appende_Report(f"\n{scan_ip}",self.base,'Sub_Titil')
            print(sc['scan'][str(scan_ip)])
            for a in sc['scan'][str(scan_ip)]['tcp']:
                print(a)
                name = sc['scan'][str(scan_ip)]['tcp'][a]['name']
                product = sc['scan'][str(scan_ip)]['tcp'][a]['product']
                vr = sc['scan'][str(scan_ip)]['tcp'][a]['version']
                try:
                    vluns = sc['scan'][str(scan_ip)]['tcp'][a]['script']['vulners']
                except:
                    vluns=''
                self.rp.appende_Report(f"\n         {a}/TCP - {name}|{product}/{vr} [{sc['scan'][str(scan_ip)]['tcp'][a]['state']}]\n{vluns}",self.base,'report')
            if len(self.ip) == 0:
                break