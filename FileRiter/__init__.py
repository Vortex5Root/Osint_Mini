from Arts import __arts__
import os
class reports():
    def __init__(self):
        self.Titil = ''
        self.subTitils = []
        self.reportss = []
        self.art = __arts__()
    def set_titil(self,titil):
        self.Titil = titil
        return True
    def set_SubTitil(self,subtitil):
        index_of = len(self.subTitils)
        self.subTitils.append(subtitil)
        print(self.subTitils)
        return index_of
    def set_reportss(self,text,new=True):
        if new != True:
            self.reportss[int(new)].append(text)
        else:
            self.reportss.append([text])
    def appende_Report(self,text,Name,layer):
        id = '  '
        if layer == 'Sub_Titil':
            id = id *2
            text = self.art.get_art(text)
        elif layer == 'report':
            id = id *3
        save_report = open('./Reports/' + str(Name) + '.txt', 'a')
        save_report.writelines(text)
        save_report.close()
    def save_Report(self,Name):
        os.system('mkdir Reports')
        save_report = open('./Reports/'+str(Name)+'.txt','w')
        titulo = self.art.get_art(self.Titil)
        print(titulo)
        save_report.writelines(titulo)
        print(len(self.subTitils)-1)
        for i in range(len(self.subTitils)-1):
            save_report.writelines(self.art.get_art(self.subTitils[i]))
            for rep in self.reportss[i]:
                save_report.writelines(rep)
        save_report.close()
        return True