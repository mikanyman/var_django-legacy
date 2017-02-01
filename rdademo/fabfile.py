from fabric.api import *
from fabric.contrib import django

django.project('rdademo')
from rdademo.rda.models import *

def production():
    env.hosts = ['a29.myrootshell.com']
    env.user = 'rdademo'
    env.app_details = { 'name': 'RDA Demo', \
                        'version': '0.1'}   
    env.deploy_to = '/tmp/rdademo'
    env.repository = {'url':'svn+ssh://a29.myrootshell.com/var/svn/rdademo/trunk', \
                        'username': 'root', \
                        'password': 'T543ufebrup+' \
                        'command': 'svn export --force'}
                     
set(fab_user='rdademo',
    root='/var/django/rdademo/',
    site='rda',
    backup_name = 'prod_db.sql')

def export_repository():
    """ Export svn repository """
    run('%s --username %s --password %s --no-auth-cache %s %s' % \
        (env.repository['command'], env.repository['username'], env.repository['password'], env.repository['url'], env.deploy_to)
    run('tar -C env.deploy_to -czvf rdademo.tar.gz')

def dump_production_database():
    """ Dump the postgres database """
    run('pg_dump -U %s -W %s %s > /tmp/$(backup_name) | gzip > prod_db.sql.tar.gz' % (
        settings.DATABASE_USER,
        settings.DATABASE_PASSWORD,
        settings.DATABASE_NAME
    ))
    
def deploy():
    export_repository()
    dump_production_database()
    local('rm /tmp/$(backup_name)')
    #run('rm $(backup_name) && rm -rf $s' % (env.deploy_to)
    put('rdademo.tar.gz', '$(root)rdademo.tar.gz')
    run('cd $(root)')
    run('tar zxf rdademo.tar.gz')
    put('$(backup_name).tar.gz', '$(root)$(backup_name).tar.gz')
    run('tar zxf $(backup_name).tar.gz')
    run('psql rdademo < $(backup_name)')
    run('rm $(backup_name).tar.gz')
    run('python manage.py syncdb')
    
