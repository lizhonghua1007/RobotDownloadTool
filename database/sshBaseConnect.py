import paramiko

class SSH_test:
    def __init__(self,host,port,username,password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #ssh连接
    def sshConnect(self):
        #连接服务器
        try:
            self.ssh.connect(self.host,self.port,self.username,self.password)
            return '成功'
        except Exception as e:
            print(e)
            return e.args[1]

    #执行shell语句
    def run_shell(self,cmd):
        ssh_in,ssh_out,ssh_error = self.ssh.exec_command(cmd)
        result = ssh_out.read() or ssh_error.read()
        return result.decode().strip()

    #reboot
    def reboot_ssh(self):
        #在远程执行sudo命令时，一般主机都会需要通过tty才能执行，通过把get_pty值设置为True，可以模拟tty。如果需要保留页面，比如说启动tomcat，不可用此种方法
        ssh_in, ssh_out, ssh_error = self.ssh.exec_command('sudo reboot',get_pty=True)
        ssh_in.write(self.password+'\n')
        result = ssh_out.read() or ssh_error.read()
        # print(result)

    #关闭ssh连接
    def sshClose(self):
        self.ssh.close()

    #链接服务器,otion为上传下载动作，1上传put，2下载get
    def sftp_test(self,from_file,to_file,option):
        transport = paramiko.Transport((self.host,self.port))
        try:
            transport.connect(username=self.username,password=self.password)
        except Exception as e:
            print(e)
            return
        sftp = paramiko.SFTPClient.from_transport(transport)

        #将文件下载到本地用get，如果上传用put
        if option == 1:
            sftp.put(from_file,to_file)
        if option == 2:
            sftp.get(from_file,to_file)
        transport.close()


# if __name__ == '__main__':
#     ssh = SSH_test('192.168.1.39',22,'robot','robot')
#     print(ssh.sshConnect())
#     # ssh.reboot_ssh()
#     ssh.sshClose()