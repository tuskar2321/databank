from .ssh_connection import SSHConnection


class GitHelper:
    def __init__(self, remote_repo):
        self.remote_repo = remote_repo

    def clone_or_reset_via_ssh(self, host, user, password, dest_dir):
        print('cloning or resetting remote repo...')

        ssh_connection = SSHConnection(host, user, password)
        clone_or_reset_command = 'if [ -d {1} ]; then cd {1} && git reset HEAD --hard; else git clone {0} {1}; fi'.format(self.remote_repo, dest_dir)
        ssh_connection.execute_command(clone_or_reset_command)

        change_rights_command = 'sudo chmod -R a+rwx {0}'.format(dest_dir)
        ssh_connection.execute_command(change_rights_command)
