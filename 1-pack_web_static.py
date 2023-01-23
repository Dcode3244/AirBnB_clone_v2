#!/usr/bin/python3
# a Fabric script that generates a .tgz archive.

from fabric.api import *
from datetime import datetime


def do_pack():
    " generates .tgz archive "
    date = datetime.utcnow()
    path = 'versions/web_static{}{}{}{}{}{}.tgz'.format(date.year, date.month,
                                                        date.day, date.hour,
                                                        date.minute,
                                                        date.second)
    local("mkdir -p versions")
    a = local("tar -czvf {} web_static".format(path))
    if a.failed:
        return None
    else:
        return path
