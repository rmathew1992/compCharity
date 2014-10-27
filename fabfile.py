"""
Example of using fabric for deployment

from fabric.api import local, lcd


def prepare_deployment(branch_name):
    local('python manage.py test django_project')
    local('git add -p && git commit')


def deploy():
    with lcd('/path/to/my/prod/area/'):

        # With git...
        local('git pull /my/path/to/dev/area/')

        # With Mercurial...
        local('hg pull /my/path/to/dev/area/')
        local('hg update')

        # With both
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')
"""