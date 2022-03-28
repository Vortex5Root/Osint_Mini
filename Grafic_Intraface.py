import PySimpleGUI as sg
from cmd_Intraface import run
class Grafic():
    functions = run()
    def __init__(self):
        Gaficos = [
            [
                sg.Text('\n     Traget:\n   ', key='-bold-'),
                sg.InputText()
            ],
            [
                sg.Button("Full_Dns_Scan"),
                sg.Button("Singel_Scan")
            ]
        ]
        sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '# 99CC99',
                                                    'SCROLL': '# 99CC99',
                                                    'BORDER': 1, 'SLIDER_DEPTH': 0,
                                                    'PROGRESS_DEPTH': 0, }
        # Create the window
        window = sg.Window("Grafic", Gaficos)
        while True:
            event, values = window.read()
            if event == "Full_Dns_Scan":
                if len(values) != 0:
                    sub_Dns = self.functions.Sub_DNS_Lookup(values[0])
                    self.functions.Extenal_Nmap_Scan(sub_Dns,values[0],2)
                else:
                    sg.Window('Error',self.Error_Screan("You dont fill the Traget "))
                    while True:
                        event, values = window.read()
                        if event == 'OK':
                            break
            elif event == "Singel_Scan":
                if len(values) != 0:
                    #sub_Dns = self.functions.Sub_DNS_Lookup(values[0])
                    sg.Window('Error', self.Error_Screan("Brevemente...!"))
                    while True:
                        event, values = window.read()
                        if event == 'OK':
                            break
                else:
                    sg.Window('Error',self.Error_Screan("You dont fill the Traget "))
                    while True:
                        event, values = window.read()
                        if event == 'OK':
                            break
    def Error_Screan(self,Text_Error):
        Error = [
            [
                sg.Text('\n     Error\n   ' + str(Text_Error), key='-bold-'),
            ],
            [
                sg.Button("OK")
            ]

        ]
        return Error
gf = Grafic()