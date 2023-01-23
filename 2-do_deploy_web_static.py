#!/usr/bin/python3
''' a Fabric script that generates a .tgz archive. and distributes
an archive to web server
'''
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['54.237.104.37', '35.174.176.205']


def do_deploy(archive_path):
    " distributes an arvhibe to web servers "
    if os.path.exists(archive_path) is False:
        return False
    if put('{}'.format(archive_path), '/tmp/').failed is True:
        return False
    tgzfile = archive_path.split('/')[-1]
    name = tgzfile.split('.')[0]
    if run('mkdir -p /data/web_static/releases/{}/'
            .format(name)).failed is True:
        return False
    if run('rm -rf /data/web_static/releases/{}/*'
            .format(name)).failed is True:
        return False
    if run('tar -xzf /tmp/{} -C \
            /data/web_static/releases/{}/'
            .format(tgzfile, name)).failed is True:
        return False
    if run('rm -f /tmp/{}'.format(tgzfile)).failed is True:
        return False
    if run('mv -f /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'
            .format(name, name)).failed is True:
        return False
    if run('rm -rf /data/web_static/releases/{}/web_static'
            .format(name)).failed is True:
        return False
    if run('rm -rf /data/web_static/current').failed is True:
        return False
    if run('ln -sf /data/web_static/releases/{}/ \
            /data/web_static/current'.format(name)).failed is True:
        return False
    return True
