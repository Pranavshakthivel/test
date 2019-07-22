from fabric.api import local
import os
import shutil


def cd():
    local('git config --global user.name "Pranavshakthivel"')
    local('git config --global user.email "Pranav.shakthivel@gmail.com"')


def pull():
    local("git pull origin master")


def ab():
    local('set PATH="c:\\Program Files\\PuTTY"')
    local('pscp c:\\Users\\Prakash\\PycharmProjects\\v2.0.zip root@192.168.50.237:/opt/v2.0.zip')
    local("hanTZ123")


def add():
    local("git add .")


def commit():
    n = input("Enter the commit : ")
    local('git commit -m "%s"' % n)


def push():
    local("git push -f origin master")


def tags():
    global t
    t = input("Enter the tag name : ")
    u = input("Enter the message: ")
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
    local("c:\\Program Files\\PuTTY")
    local('c:\\Users\\Prakash\\PycharmProjects\\%s.zip root:/opt/%s.zip' % (t, t))
    child.expect('Password:')
    child.sendline('hanTZ123')
    #local("hanTZ123")


def tag():
    cd()
    pull()
    add()
    push()
    tags()
    move()


def localpush():
    cd()
    pull()
    commit()
    add()
    push()
    tags()
    move()
