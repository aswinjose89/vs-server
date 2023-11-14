import io, os, base64

from config import basedir

class SharedUtils:
    def return_error(err_str):
        return {
            "status": 1,
            "data": err_str
        }

    def get_base_dir(self):
        return basedir