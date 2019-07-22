from fabric.api import local
import os
import shutil
from fabric.api import env, run
from datetime import date


def config():
    configuration = open("C:\\Users\\Prakash\\PycharmProjects\\config.txt", "r")
    con = configuration.readlines()
    conf = []
    global final
    final = {}
    for i in range(len(con)):
        conf.append(con[i].split('"')[1].split('"')[0])

    details = ['username', 'email']

    for i in range(len(details)):
        final[details[i]] = conf[i]


def cd():
    local('git config --global user.name "%s"' % final['username'])
    local('git config --global user.email "%s"' % final['email'])


def pull():
    local("git pull origin master")


def ab():
    env.hosts = ["192.168.50.237"]
    env.user = ["root"]
    env.password = ["hanTZ123"]
    run('uname -s')
    local('set PATH="c:\\Program Files\\PuTTY"')
    local('pscp c:\\Users\\Prakash\\PycharmProjects\\v2.0.zip root@192.168.50.237:/opt/v2.0.zip')


def add():
    local("git add .")


def commit():
    n = input("Enter the commit : ")
    local('git commit -m "%s"' % n)


def push():
    local("git push -f origin master")


def tags():
    global t
    t = "Build" + str(date.today())
    u = "Built on "+str(date.today())
    local('git tag -a %s -m "%s"' % (t, u))
    local("git push --tags")
    local("git archive --format=zip --output %s.zip %s" % (t, t))


def move():
    c = '%s.zip' % t
    path = 'C:\\Users\\Prakash\\PycharmProjects\\mark3\\'
    moveto = "C:\\Users\\Prakash\\PycharmProjects\\"
    file = os.listdir(path)
    file.sort()
    for f in file:
        if f == c:
            src = path + f
            dst = moveto + f
            shutil.move(src, dst)
    #local("c:\\Program Files\\PuTTY")
    #local('c:\\Users\\Prakash\\PycharmProjects\\%s.zip root:/opt/%s.zip' % (t, t))
    #local("hanTZ123")


def tag():
    config()
    cd()
    pull()
    add()
    push()
    tags()
    move()


def localpush():
    config()
    cd()
    pull()
    commit()
    add()
    push()
    tags()
    move()
