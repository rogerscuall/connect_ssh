import paramiko
class CONN_SSH:
    def __init__(self, cmd, host_IP, user, password, mult=30):
        self.cmd=cmd
        self.host_IP=host_IP
        self.user=user
        self.password=password
        self.mult=30
        print('HOST: ', self.host_IP.rstrip(), 'COMMAND: ', self.cmd.rstrip(), 'USERNAME: ', self.user)
    def CMD_TO_FILE(self, path_file='output.log'):
        ssh = paramiko.SSHClient()
        delimiter= '\n' +'#'*self.mult+ ' HOST: '+ self.host_IP.rstrip() + ' COMMAND: ' + self.cmd.rstrip() + ' ' + '#'*self.mult+'\n'
        try:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect( self.host_IP, username=self.user, password=self.password)
            stdin, stdout, stderr = ssh.exec_command(self.cmd)
            file_list=[]
            file_list.append(delimiter)
            file_list[1:]=stdout.readlines()
            with open(path_file, 'a') as myfile:
                for i in file_list:
                    myfile.write(i)
                myfile.write(delimiter)
        finally:
            ssh.close()
        
if __name__ == '__main__':
    conn=CONN_SSH()
    conn.CMD_TO_FILE()