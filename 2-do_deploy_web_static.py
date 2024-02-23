#!/usr/bin/python3
"""distributes an archive to the coding-max.tech web servers,
   using the function do_deploy"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['web-01.coding-max.tech', 'web-02.coding-max.tech']


def do_deploy(archive_path):
    """distributes an archive to the coding-max.tech web servers"""
    if exists(archive_path) is False:
        return False
    file_name = archive_path.split("/")[-1]
    file_wout = file_name.split(".")[0]
    path = "/data/web_static/releases/"
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_wout))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, file_wout))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_wout))
        run('rm -rf {}{}/web_static'.format(path, file_wout))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_wout)) 
        return True
    except:
        return False
