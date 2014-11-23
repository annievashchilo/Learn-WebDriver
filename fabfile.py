from fabric.api import local, env, run, task, cd, execute, runs_once

env.hosts.extend(["hvashchilo@hvashchilo-vm.inca.infoblox.com"])
run_folder = "/mnt/home/hvashchilo/Upgrade_and_Install/install_and_run"
build_folder = "/mnt/home/hvashchilo/Upgrade_and_Install/upgrade"

@task
def connect_to_vm():
    local("ssh hvashchilo@hvashchilo-vm.inca.infoblox.com")

@task
def run_test(script):
#    connect_to_vm()
    with cd(run_folder):
        return run("./run.sh %s" % script)

@task
def stop_test(script):
    with cd(run_folder):
        return run("./stop.sh %s" % script)
@task
def deploy_test(branch, script):
    with cd(run_folder):
        return run("./deploy.sh {branch} {script}".format(branch = branch, script = script))

@task
def stop_build_deploy():
    run("killscreens")

@task
def start_test(branch, script):
    deploy_test(branch, script)
    run_test(script)

