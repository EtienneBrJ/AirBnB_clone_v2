#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
    from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress files to /version"""
    local("mkdir -p versions")
    archive = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                    capture=True)

    return archive if archive else None
