from sshConnect.commonOption import Option
import os
import shutil

class SSHStep:
        def __init__(self):
                self.windowsPath = 'C:\\installtest'
        @property
        def path(self):
                return self.windowsPath
        @path.setter
        def path(self,windowsPath):
                self.windowsPath = windowsPath
        # 调用列表函数，返回分支列表数据
        def selectSrcLaunch(self, host, port, user, passwd):
                # 'SourceSSH',
                sshSource = Option('/data/packages/', '', '', '', host, port, user, passwd)
                lis = sshSource.single()
                sshSource.optionClose()
                return lis

        def sshSourceDownLoad(self, launch, host, port, user, passwd):
                # 源地址'SourceSSH',
                sshSource = Option('/data/packages/', launch + '/', 'install_isolated', self.windowsPath, host, port, user,
                                   passwd)
                # 下载
                print('压缩源文件.....')
                script1 = sshSource.tarOption('tar', 'cf')
                print('下载源文件.....')
                script2 = sshSource.downloadFile()
                sshSource.optionClose()
                return script1,script2

        def sshDstShareBackup(self, host, port, user, passwd):
                print('备份机器人rcp_slam配置文件......')
                # 备份目的地址share配置文件'DstSSH',
                sshDstShare = Option('/home/robot/ros_slam/install_isolated/', 'share/', 'rcp_slam', self.windowsPath,
                                     host, port, user, passwd)
                # 压缩配置文件，进行备份
                print('压缩配置文件，进行备份......')
                script1 = sshDstShare.tarOption('tar', 'cf')
                print('下载配置文件，进行备份......')
                script2 = sshDstShare.downloadFile()
                sshDstShare.optionClose()
                return script1,script2
        def sshDstProgectBackup(self, host, port, user, passwd):
                # 备份目的地址项目'DstSSH',
                sshDstProgectBack = Option('/home/robot/', 'ros_slam/', 'install_isolated', self.windowsPath, host, port, user, passwd)
                script1 = sshDstProgectBack.copyFile()
                sshDstProgectBack.optionClose()
                return script1

        def sshDstProgectRemove(self, host, port, user, passwd):
                # 删除目的地址项目'DstSSH',
                sshDstProgectRemove = Option('/home/robot/', 'ros_slam/', 'install_isolated', self.windowsPath,
                                             host, port, user, passwd)
                sshDstProgectRemove.remove()
                sshDstProgectRemove.optionClose()

        def sshuploadInstal(self, host, port, user, passwd):
                # 上传install_isolated压缩文件，并解压'DstSSH',
                sshupload = Option('/home/robot/', 'ros_slam/', 'install_isolated', self.windowsPath, host, port, user, passwd)
                print('上传install_isolated.tar.gz文件......')
                script1 = sshupload.uploadFile()
                print('解压install_isolated.tar.gz文件......')
                script2 = sshupload.tarOption('tar', 'xf')
                sshupload.optionClose()
                return script1,script2

        def sshupLoadSlam(self, host, port, user, passwd):
                print('上传rcp_slam......')
                # 上传rcp_slam压缩文件，并解压'DstSSH',
                sshupLoadSlam = Option('/home/robot/ros_slam/install_isolated/', 'share/', 'rcp_slam', self.windowsPath,
                                       host, port, user, passwd)
                # 删除rcp_slam文件，需要先判断一下，如果是第一次安装，不删除，如果是升级，需要删除，
                # sshupLoadSlam.remove()
                script1 = sshupLoadSlam.uploadFile()
                print('解压rcp_slam.tar.gz......')
                script2 = sshupLoadSlam.tarOption('tar', 'xf')
                sshupLoadSlam.optionClose()
                return script1,script2

        def sshSourceDel(self,launch, host, port, user, passwd):
                # 恢复环境，删除多余的包，删除源地址的tar包，删除目的地址的install_isolated.tar.gz包和rcp_slam.tar.gz包'SourceSSH',
                print('恢复环境，删除源地址的tar包')
                sshSourceDel = Option('/data/packages/', launch + '/', 'install_isolated', self.windowsPath, host, port, user, passwd)
                script1 = sshSourceDel.removeTar()
                sshSourceDel.optionClose()
                return script1

        def sshDstDel(self, host, port, user, passwd):
                print('恢复环境，删除机器人上的install_isolated.tar.gz包')
                # 'DstSSH',
                sshDstDel = Option('/home/robot/', 'ros_slam/', 'install_isolated', self.windowsPath, host, port, user, passwd)
                script1 = sshDstDel.removeTar()
                sshDstDel.optionClose()
                return script1

        def sshDstShareDel(self, host, port, user, passwd):
                print('恢复环境，删除机器人上的rcp_slam.tar.gz包')
                # 'DstSSH',
                sshDstShareDel = Option('/home/robot/ros_slam/install_isolated/', 'share/', 'rcp_slam',
                                        self.windowsPath, host, port, user, passwd)
                script1 = sshDstShareDel.removeTar()
                sshDstShareDel.optionClose()
                return script1

        # 删除本地缓存文件
        def deleteLocalFile(self,filename):
                file = os.path.join(self.windowsPath, filename)
                try:
                        os.remove(file)
                        return file
                except FileNotFoundError as s:
                        return file

        # 删除空文件夹
        def removeDir(self):
                try:
                        os.removedirs(self.windowsPath)
                        return '删除本地缓存文件夹' + self.windowsPath
                except OSError as e:
                        print(e)
                return '配置文件备份路径为：' + self.windowsPath




        def sshchmod(self, host, port, user, passwd):
                print('赋予权限......')
                # 赋予777权限'DstSSH',
                sshchmod = Option('/home/robot/', 'ros_slam/', 'install_isolated', self.windowsPath, host, port, user, passwd)
                script1 = sshchmod.chmod()
                script2 = sshchmod.sourceFile()
                script3 = sshchmod.reboot()
                sshchmod.optionClose()
                return script1,script2,script3











