from fabric.api import local

def add():
    local("git add -p")

def commit():
    local("git commit")

def push():
    local("git push")

def prepare_deploy():
    add()
    commit()
    push()

