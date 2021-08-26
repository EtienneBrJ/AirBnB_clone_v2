#!/usr/bin/python3
""" creates and distributes an archive to your web servers,
    using the function deploy
"""
from fabric.api import run, put, local, env
from datetime import datetime
from os import path


env.hosts = ['34.75.72.178', '34.139.192.61']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/holberton'


def do_pack():
    """Compress files to /version"""
    local("mkdir -p versions")
    archive = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                    capture=True)

    return archive if archive else None


def do_deploy(archive_path):
    """Distributes an archive to a web server
    """
    if path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).succeeded is False:
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
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).succeeded is False:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server

            Call the do_pack() function and store the path of the
                created archive

            Return False if no archive has been created

            Call the do_deploy(archive_path) function,
                using the new path of the new archive

            Return the return value of do_deploy
    """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
