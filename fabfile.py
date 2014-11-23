from fabric.api import local, env, run, task, cd, execute, runs_once

env.hosts.extend(["hvashchilo@hvashchilo-vm.inca.infoblox.com"])

@task
def connect_to_vm():
    local("ssh hvashchilo@hvashchilo-vm.inca.infoblox.com")

@task
def run_test(script):
#    connect_to_vm()
    with cd("/mnt/home/hvashchilo/Upgrade_and_Install/install_and_run"):
        return run("./run.sh %s" % script)

@task
def stop_test(script):
    with cd("/mnt/home/hvashchilo/Upgrade_and_Install/install_and_run"):
        return run("./stop.sh %s" % script)

@task
@runs_once
def go(script):
    results = execute(run_test(script))
    print results

@task
def stop_build_deploy():
    run("ssh hvashchilo@hvashchilo-vm.inca.infoblox.com")
    run("killscreens")

@task
def add():
    local("git add -p")

@task
def commit():
    local("git commit")

@task
def push():
    local("git push")

@task
def prepare_deploy():
    add()
    commit()
    push()

