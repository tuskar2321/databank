import glob
import os
import pathlib
import time

from .params_registry import ParamsRegistry

class Waiter:
    def wait_file_download_by_glob(download_glob):
        timeout = 2 # сек
        estimated_time = 0
        while estimated_time < ParamsRegistry.downdload_timeout():
            time.sleep(timeout)
            estimated_time += timeout
            if len(glob.glob(download_glob)) > 0:
                break

    wait_file_download_by_glob = staticmethod(wait_file_download_by_glob)