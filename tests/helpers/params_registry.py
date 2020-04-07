import os


class ParamsRegistry:
    def remote_host():
        host = 'localhost'
        try:
            host = os.environ['HOST']
        except:
            host = 'localhost'
        return host
    remote_host = staticmethod(remote_host)

    def ssh_user():
        user = 'vagrant'
        try:
            user = os.environ['SSH_USER']
        except:
            user = 'vagrant'
        return user
    ssh_user = staticmethod(ssh_user)

    def ssh_password():
        password = 'vagrant'
        try:
            password = os.environ['SSH_PASSWORD']
        except:
            password = 'vagrant'
        return password
    ssh_password = staticmethod(ssh_password)

    def test_data_repo_remote_path():
        return 'http://192.168.0.201/repos/test-data/geodbse-test-data.git'
    test_data_repo_remote_path = staticmethod(test_data_repo_remote_path)

    def geodbse_upload_data_path():
        return '/var/Panorama/GeoDBSE/upload'

    def downdload_timeout():  # сек
        return 15 * 60  # 15 мин
    downdload_timeout = staticmethod(downdload_timeout)
