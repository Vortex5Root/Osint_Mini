
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
from FileRiter import reports
class info():
    rp = reports()
    def dnsDump(self,target_domain,outputs=False):
        arry = []
        if outputs == False:
            result = DNSDumpsterAPI().search(target_domain)
            for record in result['dns_records']['host']:
                arry.append(f"{record['domain']}:{record['ip']}")
            return arry
        else:
            self.rp.appende_Report(target_domain,str(target_domain),'Sub_Titil')
            print('\n-> DNSdumpster Results\n')
            rp_indix = self.rp.appende_Report('\n-> DNSdumpster Results\n',str(target_domain),'Sub_Titil')

            result = DNSDumpsterAPI().search(target_domain)

            if len(result) > 0:

                print('[@] Target: ' + result['domain'] + '\n')
                self.rp.appende_Report('\n[@] Target: ' + result['domain'] + '\n',str(target_domain),'report')
                print('[*] DNS Servers')
                self.rp.appende_Report('\n[*] DNS Servers\n\n',str(target_domain),'report')
                for record in result['dns_records']['dns']:
                    self.rp.appende_Report("""- Domain: {}
        - IP: {}
        - Reverse DNS: {}
        - AS: {}
        - ISP: {}
        - Country: {}
        - Header: {}\n
        """.format(record['domain'], record['ip'], record['reverse_dns'], record['as'], record['provider'],
                   record['country'], record['header']),str(target_domain),'report')
                    print("""- Domain: {}
        - IP: {}
        - Reverse DNS: {}
        - AS: {}
        - ISP: {}
        - Country: {}
        - Header: {}
        """.format(record['domain'], record['ip'], record['reverse_dns'], record['as'], record['provider'],
                   record['country'], record['header']))
                self.rp.appende_Report('\n[*] MX Records\n\n',str(target_domain),'report')
                print('[*] MX Records')
                for record in result['dns_records']['mx']:
                    self.rp.appende_Report("""- Domain: {}
        - IP: {}
        - Reverse DNS: {}
        - AS: {}
        - ISP: {}
        - Country: {}
        - Header: {}\n
        """.format(record['domain'], record['ip'], record['reverse_dns'], record['as'], record['provider'],
                   record['country'], record['header']),str(target_domain),'report')
                    print("""- Domain: {}
        - IP: {}
        - Reverse DNS: {}
        - AS: {}
        - ISP: {}
        - Country: {}
        - Header: {}
        """.format(record['domain'], record['ip'], record['reverse_dns'], record['as'], record['provider'],
                   record['country'], record['header']))
                self.rp.appende_Report('\n[*] TXT Records\n\n',str(target_domain),'report')
                print('[*] TXT Records')
                for record in result['dns_records']['txt']:
                    self.rp.appende_Report('\n- ' + record,str(target_domain),'report')
                    print('- ' + record)
                self.rp.appende_Report('\n[*] Host Records\n\n',str(target_domain),'report')
                print('\n[*] Host Records')
                for record in result['dns_records']['host']:
                    self.rp.appende_Report("""- Domain: {}
        - IP: {}
        - Reverse DNS: {}
        - AS: {}
        - ISP: {}
        - Country: {}
        - Header: {}\n
        """.format(record['domain'], record['ip'], record['reverse_dns'], record['as'], record['provider'],
                   record['country'], record['header']),str(target_domain),'report')
                    print("""- Domain: {}
        - IP: {}
        - Reverse DNS: {}
        - AS: {}
        - ISP: {}
        - Country: {}
        - Header: {}
        """.format(record['domain'], record['ip'], record['reverse_dns'], record['as'], record['provider'],
                   record['country'], record['header']))
                    arry.append(f"{record['domain']}:{record['ip']}")
            ##
            #
            # REFORMATE ARRY
            #
            ##
            new_arry = []
            ips = []
            for i in arry:
                a = str(i).split(':')[1]
                if a not in ips:
                    ips.append(a)
                    new_arry.append(i)
                else:
                    new_arry[ips.index(a)] = f"{str(new_arry[ips.index(a)]).split(':')[0]}/{str(i).split(':')[0]}:{str(i).split(':')[1]}"
            return new_arry
