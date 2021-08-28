#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
    using the function do_deploy
"""
from getpass import getpass
from fabric.api import run, put, env
import os.path


env.hosts = ['34.75.72.178', '34.139.192.61']


def do_deploy(archive_path):
    """Distributes an archive to a web server
    """
    #env.password = getpass('Enter the password for %s: ' % env.hosts[0])
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).succeeded is False:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).succeeded is False:
        return False
    if run("rm /tmp/{}".format(file)).succeeded is False:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/"
           .format(name, name)).succeeded is False:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).succeeded is False:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).succeeded is False:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).succeeded is False:
        return False
    return True
