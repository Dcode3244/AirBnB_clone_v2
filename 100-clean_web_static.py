#!/usr/bin/python3
''' deletes out-of-date archives '''

from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['54.237.104.37', '35.174.176.205']


def do_clean(number=0):
    ''' deletes out-of-date archives '''
    tgz = sorted(os.listdir('versions'))
    number = int(number)
    if number == 0:
        number = 1
    for i in range(number):
        tgz.pop()

    with lcd('versions/'):
        for file in tgz:
            local('rm {}'.format(file))

    with cd('/data/web_static/releases'):
        tgz = run('ls -tr').split()
        delete = []
        for file in tgz:
            if '.tgz' in file:
                delete.append(file)
        for i in range(number):
            if len(delete):
                delete.pop()
        for file in delete:
            run('rm -rf {}'.format(file))
