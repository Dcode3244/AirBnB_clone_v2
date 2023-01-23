#!/usr/bin/python3
''' a Fabric script that generates a .tgz archive. and distributes
an archive to web server
'''
import os
from fabric.api import *
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.237.104.37', '35.174.176.205']


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


def do_deploy(archive_path=''):
    " distributes an arvhibe to web servers "
    if os.path.exists(archive_path) is False:
        return False
    if put('{}'.format(archive_path), '/tmp/').failed is True:
        return False
    name = archive_path.replace('.tgz', '')
    name = name.replace('versions/', '')
    if run('tar -xzvf /tmp/web_static*.tgz -C \
            /data/web_static/releases/'.format(name)).failed is True:
        return False
    if run('rm -f /tmp/web_static*').failed is True:
        return False
    if run('rm -rf /data/web_static/current').failed is True:
        return False
    if run('ln -sf /data/web_static/releases/web_static* \
            /data/web_static/current').failed is True:
        return False
    return True
