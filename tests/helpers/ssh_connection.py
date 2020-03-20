import paramiko


class SSHConnection:
    def __init__(self, host, user, password):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(host, username=user, password=password)

    def __del__(self):
        self.ssh_client.close()

    def execute_command(self, command):
        print('ssh_connection: ' + command)
        stdin, stdout, stderr = self.ssh_client.exec_command(command)

        print('ssh command stdout:')
        for line in stdout:
            print(line.strip('\n'))

        print('ssh command stderr:')
        for line in stderr:
            print(line.strip('\n'))
