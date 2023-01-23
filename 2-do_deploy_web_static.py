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
    if os.path.isfile(archive_path) is False:
        return False
    a = put('{}'.format(archive_path), '/tmp/')
    name = archive_path.replace('.tgz', '')
    name = name.replace('versions/', '')
    b = run('tar -xzvf /tmp/web_static*.tgz -C \
            /data/web_static/releases/'.format(name))
    c = run('rm -f /tmp/web_static*')
    d = run('rm -rf /data/web_static/current')
    e = run('ln -sf /data/web_static/releases/web_static* \
            /data/web_static/current')
    if (a.failed or b.failed or c.failed or d.failed or e.failed):
        return False
    return True
