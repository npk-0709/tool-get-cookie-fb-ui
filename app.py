"""
    # Copyright © 2022 By Nguyễn Phú Khương
    # ZALO : 0363561629
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""
from ui import *
import sys
import threading
import numpy
from coreThread import *
import ctypes
from chrome import *
import webbrowser




class core(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.success_total.setStyleSheet(f"color: blue;font-weight: bold;")
        self.btnEvent.setStyleSheet(f"color: green;font-weight: bold;")
        self.btnEvent.clicked.connect(lambda: threading.Thread(target=self._btnEvents).start())
        self.btnExportFile.clicked.connect(lambda: self.exportFile())
        self.inputData.textChanged.connect(lambda: ThreadUpdate([None,self.callback_updatedata]).update())
        self.resultData.textChanged.connect(lambda: ThreadUpdate([None,self.callback_updatedata]).update())
        self.btnContactAdmin.clicked.connect(lambda: webbrowser.open_new('https://zalo.me/0363561629'))
        self.successValue = 0
    
    def update(self,_):
        ThreadUpdate([None,self.callback_updatedata]).update()


    def _btnEvents(self):
        
        if self.btnEvent.text() == "BẮT ĐẦU":
            self.successValue = 0
            self.isRunning = True
            self.btnEvent.setStyleSheet(f"color: red;font-weight: bold;")
            self.btnEvent.setText("BẤM ĐỂ DỪNG")
            datas = list(numpy.array_split(self.inputData.toPlainText().split('\n'),self.numThread.value()))
            for data in datas:
                threading.Thread(target=self.appmain,args=(data,)).start()


        else:
            self.btnEvent.setStyleSheet(f"color: green;font-weight: bold;")
            self.btnEvent.setText("BẮT ĐẦU")
            self.isRunning = False
    
    def exportFile(self):
        try:
            with open('result.txt','a+',encoding='utf-8') as f:
                    f.write(self.resultData.toPlainText())
            ctypes.windll.user32.MessageBoxW(0, "XUẤT FILE THÀNH CÔNG `result.txt`", "EXPORT SUCCESS", 64)
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"XUẤT FILE THẤT BẠI `{str(e)}`", "EXPORT ERROR", 64)
        
    
    def appmain(self,data:list):
        for datax in data:
            try:
                if self.isRunning == False:
                    break
                if self.typeLogin.currentText() == 'COOKIE':
                    uid = str(datax).split('c_user=')[1].split(';')[0].strip()
                    cookie = str(datax).strip()
                    ThreadUpdate([[self.status,f'[{uid}]ĐANG KHỞI TẠO MÔI TRƯỜNG....'],self.callback_appendDataResult]).update()
                    driver = WebDriver().startDriver()
                    driver.get('https://mbasic.facebook.com/login')
                    ThreadUpdate([[self.status,f'[{uid}]ĐANG ĐĂNG NHẬP BẰNG COOKIE'],self.callback_appendDataResult]).update()
                    isLogins,resp = LoginFacebookCookie(driver,cookie)
                    if isLogins:
                        if self.typeGet.currentText() == 'COOKIE':
                            ThreadUpdate([[self.status,f'[{uid}]ĐÃ ĐĂNG NHẬP THÀNH CÔNG - ĐANG GET COOKIE MỚI'],self.callback_appendDataResult]).update()
                            cookie_New = getFullCookie(driver)
                            if self.typeResult.currentText() == 'UID|RESULT':                       
                                ThreadUpdate([[self.resultData,uid+'|'+str(cookie_New)],self.callback_appendDataResult]).update()
                            else:
                                ThreadUpdate([[self.resultData,str(cookie_New)],self.callback_appendDataResult]).update()
                            self.successValue+=1
                            ThreadUpdate([[self.status,f'[{uid}]ĐÃ HOÀN TẤT'],self.callback_appendDataResult]).update()

                        if self.typeGet.currentText() == 'ACCESS_TOKEN EAAB':
                            ThreadUpdate([[self.status,f'[{uid}]ĐÃ ĐĂNG NHẬP THÀNH CÔNG - ĐANG GET ACCESSTOKEN EAAB'],self.callback_appendDataResult]).update()
                            token = getAccesstokenEAAB(driver)
                            if self.typeResult.currentText() == 'UID|RESULT':
                                ThreadUpdate([[self.resultData,uid+'|'+str(token)],self.callback_appendDataResult]).update()
                            else:
                                ThreadUpdate([[self.resultData,str(token)],self.callback_appendDataResult]).update()
                            self.successValue+=1
                            ThreadUpdate([[self.status,f'[{uid}]ĐÃ HOÀN TẤT'],self.callback_appendDataResult]).update()
                    else:
                        ThreadUpdate([[self.status,f'[{uid}]ĐĂNG NHẬP THẤT BẠI'],self.callback_appendDataResult]).update()
                        ThreadUpdate([[self.resultData,uid+'|LOGIN_FAIL|'+str(resp)],self.callback_appendDataResult]).update()
                    
                if self.typeLogin.currentText() == 'USER|PASS|2Fa':
                    uid = str(datax).split('|')[0].strip()
                    ThreadUpdate([[self.status,f'[{uid}]ĐANG KHỞI TẠO MÔI TRƯỜNG....'],self.callback_appendDataResult]).update()
                    driver = WebDriver().startDriver()
                    driver.get('https://mbasic.facebook.com/login')
                    passw = str(datax).split('|')[1].strip()
                    twoFa = str(datax).split('|',4)[2].strip()
                    ThreadUpdate([[self.status,f'[{uid}]ĐANG ĐĂNG NHẬP BẰNG USER|PASS|2FA...'],self.callback_appendDataResult]).update()
                    isLogins,resp = LoginFacebookUserPass2Fa(driver,uid,passw,twoFa)
                    if isLogins:
                        if self.typeGet.currentText() == 'COOKIE':
                            ThreadUpdate([[self.status,f'[{uid}]ĐÃ ĐĂNG NHẬP THÀNH CÔNG - ĐANG GET COOKIE MỚI'],self.callback_appendDataResult]).update()
                            cookie_New = getFullCookie(driver)
                            if self.typeResult.currentText() == 'UID|RESULT':                       
                                ThreadUpdate([[self.resultData,uid+'|'+str(cookie_New)],self.callback_appendDataResult]).update()
                            else:
                                ThreadUpdate([[self.resultData,str(cookie_New)],self.callback_appendDataResult]).update()
                            self.successValue+=1
                            ThreadUpdate([[self.status,f'[{uid}]ĐÃ HOÀN TẤT'],self.callback_appendDataResult]).update()

                        if self.typeGet.currentText() == 'ACCESS_TOKEN EAAB':
                            ThreadUpdate([[self.status,f'[{uid}]ĐÃ ĐĂNG NHẬP THÀNH CÔNG - ĐANG GET ACCESSTOKEN EAAB'],self.callback_appendDataResult]).update()
                            token = getAccesstokenEAAB(driver)
                            if self.typeResult.currentText() == 'UID|RESULT':
                                ThreadUpdate([[self.resultData,uid+'|'+str(token)],self.callback_appendDataResult]).update()
                            else:
                                ThreadUpdate([[self.resultData,str(token)],self.callback_appendDataResult]).update()
                            self.successValue+=1
                            ThreadUpdate([[self.status,f'[{uid}]ĐÃ HOÀN TẤT'],self.callback_appendDataResult]).update()
                    else:
                        ThreadUpdate([[self.status,f'[{uid}]ĐĂNG NHẬP THẤT BẠI'],self.callback_appendDataResult]).update()
                        ThreadUpdate([[self.resultData,uid+'|LOGIN_FAIL|'+str(resp)],self.callback_appendDataResult]).update()
                ThreadUpdate([None,self.callback_updatedata]).update()
                try:
                    driver.quit()
                except:pass
            except Exception as e:
                with open('debug.error.log','a+',encoding='utf-8') as f:
                    f.write(str(e)+'\n')

            
        

    def callback_updatedata(self, _):
        total = str(len(self.inputData.toPlainText().split('\n')))
        if self.inputData.toPlainText().strip() == '':
            total ='0'
        result = str(len(self.resultData.toPlainText().split('\n')))
        if self.resultData.toPlainText().strip() == '':
            result = '0'
        self.success_total.setText(f'{str(self.successValue)}/{result}/{total}')
    
    def callback_appendDataResult(self,data:list):
        data[0][0].appendPlainText(data[0][1].strip())
        




app = QtWidgets.QApplication(sys.argv)
cores = core()
cores.show()
sys.exit(app.exec_())