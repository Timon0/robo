import paramiko


class FileTransfer():

    def __init__(self, robot):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(robot.configuration.Ip, username=robot.configuration.Username, password=robot.configuration.Password)


    def get(self, remote, local):
        sftp = self.ssh.open_sftp()
        sftp.get(remote, local)
        sftp.remove(remote)
        sftp.close()

    def put(self, local, remote):
        sftp = self.ssh.open_sftp()
        sftp.put(local, remote)
        sftp.close()

    def remove(self, path):
        sftp = self.ssh.open_sftp()
        sftp.remove(path)
        sftp.close()

    def close(self):
        self.ssh.close()
