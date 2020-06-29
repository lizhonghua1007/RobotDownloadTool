from database.sshBaseConnect import SSH_test
import os

class Option:
    '''
    根据sshOption ssh到服务器
    master为主目录/data/packages/
    branch为分支 firefight/  gas_station/  oil_field/  security/
    file为压缩或者解压的文件
    path为目的地址
    '''
    def __init__(self,master,branch,file,path,host,port,user,passwd):#正在改，init添加了host,port,user,passwd,删除了sshOption，明天继续
        self.master = master
        self.branch = branch
        self.file = file
        self.path = path
        self.ssh = SSH_test(host, port, user, passwd)
        self.ssh.sshConnect()
    '''
    tar动作
    cmd 为tar
    option 为xvf 或者为cvf。xvf为解压，cvf为压缩
    '''
    def tarOption(self,cmd,option):
        try:
            # 切割master,获取到ros_slam地址
            ros_slam = self.master.split(self.master.split('/')[4])[0]
            branchFile = self.ssh.run_shell('cd ' + ros_slam + ';ls')
            if branchFile == '':
                print('此次为第一次安装，配置文件不需要备份')
                return '此次为第一次安装，配置文件不需要备份'
            else:
                script = self.tar(cmd, option)
                return script
        except IndexError as e:
            script = self.tar(cmd,option)
            return script

    def tar(self,cmd,option):
        # option xf为解压，cf为压缩
        if option == 'cf':
            # if self.ssh.run_shell('cd ' + self.master + self.branch + ';ls')
            command = cmd + ' -pzcf ' + self.file + '.tar.gz ' + self.file
            self.ssh.run_shell('cd ' + self.master + self.branch + ';' + command)
            return '压缩' + self.file + '.tar.gz ' + '文件'
        elif option == 'xf':
            command = cmd + ' -xpf ' + self.file + '.tar.gz'
            self.ssh.run_shell('cd ' + self.master + self.branch + ';' + command)
            return '解压' + self.file + '.tar.gz ' + '文件'

    #获取分支，列表并以列表的方式输出
    def single(self):
        launchs = self.ssh.run_shell('cd ' + self.master + ';ls')
        lis = launchs.split('\n')
        return lis

    #reboot重启
    def reboot(self):
        self.ssh.reboot_ssh()
        return '重启ubuntu系统'

    #项目备份，将项目备份成项目_backup
    def copyFile(self):
        branchFile = self.ssh.run_shell('cd ' + self.master + self.branch + ';ls')
        if branchFile == '':
            print('此次为第一次安装，项目不需要备份')
            return '此次为第一次安装，项目不需要备份'
        else:
            print('备份原文件项目，将文件备份为install_isolated_backup......')
            command = 'cp -r ' + self.file + ' ' + self.file + '_backup'
            self.ssh.run_shell('cd ' + self.master + self.branch + ';' + command)
            return '备份原文件项目，将文件备份为install_isolated_backup......'

    def chmod(self):
        command = 'chmod 777 ' + self.file
        print(self.ssh.run_shell('cd ' + self.master + self.branch + ';' + command))
        return '赋予' + self.file + '文件777权限'

    def createWinPath(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def createLinuxPath(self):
        if not os.path.exists(self.master + self.branch):
            os.mkdir(self.master + self.branch)

    # 针对tar文件，多文件暂不支持
    def downloadFile(self):
        self.createWinPath()
        if self.file in self.ssh.run_shell('ls ' + self.master + self.branch):
            self.ssh.sftp_test(self.master + self.branch + self.file + '.tar.gz',
                               os.path.join(self.path, self.file + '.tar.gz'), 2)
            return '下载' + self.file + '.tar.gz' + '文件'
        else:
            print('没有' + self.file + '.tar.gz这个文件，不需要备份')
            return '没有' + self.file + '.tar.gz这个文件，不需要备份'

    # 针对tar文件，多文件暂不支持
    def uploadFile(self):
        try:
            self.ssh.sftp_test(os.path.join(self.path, self.file + '.tar.gz'),
                               self.master + self.branch + self.file + '.tar.gz', 1)
            return '上传' + self.file + '.tar.gz文件.....'
        except FileNotFoundError as FileNotFound:
            print('因第一次安装,' + FileNotFound.args[1]+'文件为:'+FileNotFound.filename)
            return '因第一次安装,' + FileNotFound.args[1]+'文件为:'+FileNotFound.filename

    #删除rm -rf
    def removeTar(self):
        print(self.master + self.branch)
        print(self.file + '.tar.gz')
        self.ssh.run_shell('cd ' + self.master + self.branch + ';rm -rf ' + self.file + '.tar.gz')
        return '删除' + self.file + '.tar.gz文件......'

    def remove(self):
        print(self.master + self.branch)
        print(self.file)
        self.ssh.run_shell('cd ' + self.master + self.branch + ';rm -rf ' + self.file)

    def sourceFile(self):
        print('source setup.bash')
        self.ssh.run_shell('cd ' + self.master + self.branch + self.file + ';source setup.bash')
        return 'source setup.bash'

    def optionClose(self):
        self.ssh.sshClose()