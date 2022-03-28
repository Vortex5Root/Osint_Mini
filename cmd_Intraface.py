from Dns_Dumpter import info
from Nmap_API.nmap_api import nmap_tool
from sys import argv
from Arts import __arts__
from FileRiter import reports
class run():
    '''
    def __init__(self,args):
        if '-h' in args:
            print('User cmd_Intraface.py -t <Main_DNS>')
        try:
            alvo = args[int(args.index('-t'))]
        except:
            pass
    '''
    def Sub_DNS_Lookup(self,alvo):
        dumpster = info()
        r = dumpster.dnsDump(alvo,True)
        return r
    def Extenal_Nmap_Scan(self,subdns,alvo,speed=1):
        api = nmap_tool(subdns)
        api.get_AllOpenPorts(alvo, speed)
class cmd():
    at = __arts__()
    tool = run()
    def __init__(self,agrv):
        if '-h' in agrv:
            self.at.get_art('help')
            print('[Report_Tool_Cmd] Options')
            print('[Report_Tool_Cmd] -full <Base_DNS> For Report Whid Vulns off all sub_dns')
            print('[Report_Tool_Cmd] -simple <sub_dns/dns> For un Report of un exp dns/sub_dns')
        elif '-full' in agrv:
            try:
                tg = agrv[int(agrv.index('-full'))+1]
                sub_Dns = self.tool.Sub_DNS_Lookup(tg)
                self.tool.Extenal_Nmap_Scan(sub_Dns, tg, 2)
            except:
                print('[Report_Tool_Cmd] User cmd_Intraface.py -full <Base_DNS>')
        elif '-simple' in agrv:
            print('[Report_Tool_Cmd] Working ON')
            self.at.get_art('   ; (')
        else:
            print('[Report_Tool_Cmd] User cmd_Intraface.py -h for help')
cmd(argv)
#Traget = ''
#rp = reports()
#t = run()
#s = t.Sub_DNS_Lookup(Traget)