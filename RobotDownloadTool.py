import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from graphGUI.robotGUI import *
from config import set
from business.sshCall import SSHStep
from database.sshBaseConnect import SSH_test
from database.readConf import ReadIni
from PyQt5.QtGui import QIcon
import _thread
import time

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.hostname = ''

    # 获取config配置文件中的host、port、user、passwd值，回写到界面上
    def getSSHInformation(self,sshOption):
        keys = ReadIni(set.TEST_CONFIG, sshOption).ReadIniFile()
        host, port, user, passwd = keys['host'], int(keys['port']), keys['user'], keys['password']
        if sshOption == 'SourceSSH':
            self.sourceHost.setText(host)
        elif sshOption == 'DstSSH':
            self.dstHost.setText(host)

    # 根据分支列表，选择当前选中的分支，将当前分支的值传给确定按钮
    def selectBrunchChange(self):
        return self.branch.currentText()

    # 根据界面获取source或dst的host,port,user,passwd
    def set_sourceOrdst(self,select):
        lis = []
        if select == 'SourceSSH':
            dic = ReadIni(set.TEST_CONFIG, 'SourceSSH').ReadIniFile()
            host = dic['host']
            port = int(dic['port'])
            user = dic['user']
            password = dic['password']
            lis.append(host)
            lis.append(port)
            lis.append(user)
            lis.append(password)

        elif select == 'DstSSH':
            dic = ReadIni(set.TEST_CONFIG, 'DstSSH').ReadIniFile()
            host = dic['host']
            port = int(dic['port'])
            user = dic['user']
            password = dic['password']
            lis.append(host)
            lis.append(port)
            lis.append(user)
            lis.append(password)

        return tuple(lis)

        # ssh到source上，获取分支列表
    def getBrunch(self):
        tup = self.set_sourceOrdst('SourceSSH')
        host, port, user, passwd = tup
        ssh = SSHStep()
        braunshs = ssh.selectSrcLaunch(host, port, user, passwd)
        for braunsh in braunshs:
            self.branch.addItem(braunsh)

    # 获取当前界面上source的host,port,user,passwd值
    def click_ssh_source_test(self):
        tup = self.set_sourceOrdst('SourceSSH')
        host, port, user, passwd = tup
        ssh = SSH_test(host, port, user, passwd)
        result = ssh.sshConnect()
        if result == '成功':
            self.branch.clear()
            self.getBrunch()
        self.log('测试连接主机:'+host + ',' + result)
        ssh.sshClose()

    # 获取当前界面上dst的host,port,user,passwd值
    def click_ssh_dst_test(self):
        tup = self.set_sourceOrdst('DstSSH')
        host, port, user, passwd = tup
        host = self.dstHost.text()
        ssh = SSH_test(host, port, user, passwd)
        result = ssh.sshConnect()
        if result == '成功':
            self.hostname = ssh.run_shell('cat /etc/hostname')
        self.log('测试连接主机:'+host + ',' + result)
        ssh.sshClose()

    def selectDir(self):
        dirname = self.dirName()
        self.filePath.setText(dirname)

    def log(self,logtext):
        self.logView.append(logtext)
        self.flush()

    # 点击确定，确定分支的值
    def check(self):
        brunch = self.selectBrunchChange()
        ssh = SSHStep()
        ssh.path = self.filePath.text()
        if self.filePath.text() == '未选择路径' or self.filePath.text() == '':
            self.selectDir()
            ssh.path = self.filePath.text()
        else:
            # 调用ssh业务，顺序见sshCall方法
            tup = self.set_sourceOrdst('SourceSSH')
            host, port, user, passwd = tup
            self.log('分支压缩和下载......')
            source_tar, source_download = ssh.sshSourceDownLoad(brunch, host, port, user, passwd)
            self.log(source_tar)
            self.log(source_download)
            tup = self.set_sourceOrdst('DstSSH')
            host, port, user, passwd = tup
            self.log('备份机器人配置文件......')
            dst_set_file_tar, dst_set_file_dw = ssh.sshDstShareBackup(host, port, user, passwd)
            # dst_set_file_tar  此次为第一次安装，项目不需要备份，需要删除之前安装过的rcp_slam.tar.gz
            if dst_set_file_tar == '此次为第一次安装，配置文件不需要备份':
                localFileSlam = ssh.deleteLocalFile('rcp_slam.tar.gz')
                self.log('删除本地缓存文件，文件路径为:' + localFileSlam)
            self.log(dst_set_file_tar)
            self.log(dst_set_file_dw)
            self.log('备份机器人项目......')
            dst_program_download = ssh.sshDstProgectBackup(host, port, user, passwd)
            self.log(dst_program_download)
            self.log('删除老版本机器人项目.....')
            ssh.sshDstProgectRemove(host, port, user, passwd)
            self.log('上传新版本install_isolated.tar.gz压缩文件，并解压......')
            dst_program_tar, dst_program_upload = ssh.sshuploadInstal(host, port, user, passwd)
            self.log(dst_program_tar)
            self.log(dst_program_upload)
            self.log('上传rcp_slam.tar.gz压缩文件，并解压......')
            dst_set_tar, dst_set_upload = ssh.sshupLoadSlam(host, port, user, passwd)
            self.log(dst_set_tar)
            self.log(dst_set_upload)
            tup = self.set_sourceOrdst('SourceSSH')
            host, port, user, passwd = tup
            self.log('恢复环境，删除多余的包，删除源地址的tar包，删除目的地址的install_isolated.tar.gz包和rcp_slam.tar.gz包......')
            source_tar_delete = ssh.sshSourceDel(brunch, host, port, user, passwd)
            self.log(source_tar_delete)
            tup = self.set_sourceOrdst('DstSSH')
            host, port, user, passwd = tup
            self.log('恢复环境，删除机器人上的install_isolated.tar.gz包......')
            dst_program_tar_delete = ssh.sshDstDel(host, port, user, passwd)
            self.log(dst_program_tar_delete)
            self.log('恢复环境，删除机器人上的rcp_slam.tar.gz包......')
            dst_set_tar_delete = ssh.sshDstShareDel(host, port, user, passwd)
            self.log(dst_set_tar_delete)
            localFile = ssh.deleteLocalFile('install_isolated.tar.gz')
            self.log('删除本地缓存文件，文件路径为:' + localFile)
            chmod, source, reboot = ssh.sshchmod(host, port, user, passwd)
            self.log(chmod)
            self.log(source)
            self.log(reboot)
            self.messageSuccessDownload()

    # 处理消息框
    def information(self):
        if self.selectBrunchChange() == '':
            self.messageBoxTip()
        else:
            if self.hostname == '':
                self.messageBoxDst()
            else:
                information = self.messageBoxinstall(self.selectBrunchChange(), self.hostname)
                if information == 16384:  # 选择yes
                    # self.check()
                    try:
                        _thread.start_new_thread(self.check,())

                    except:
                        print('无法启动线程')
                else:
                    print('取消')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    myWin.getSSHInformation('SourceSSH')
    myWin.getSSHInformation('DstSSH')
    myWin.sourceSSHTest.clicked.connect((myWin.click_ssh_source_test))
    myWin.dstSSHTest.clicked.connect((myWin.click_ssh_dst_test))
    myWin.commit.clicked.connect(myWin.information)
    myWin.selectFile.clicked.connect(myWin.selectDir)
    myWin.setWindowIcon(QIcon(set.logoImage))

    sys.exit(app.exec_())