#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a .tgz archive"""
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None
