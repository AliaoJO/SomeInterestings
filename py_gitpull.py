# 使用python git pull 当前文件夹下所有git项目
import os
import subprocess

def gitpull(path):
    return subprocess.call(['git', 'pull'], cwd=path)

def gitpull_current_dir(path):
    for file in os.listdir(path):
        hit = False
        if file == '.git':
            print('git pull %s' % path)
            fatelTimes = 0
            while True:
                res = gitpull(path)
                if res == 0:
                    hit = True
                    break
                fatelTimes += 1
            print('** git pull success (fatel times - %s)' % fatelTimes)
        elif os.path.isdir(file):
            gitpull_current_dir(file)    
            
        if hit:
            break

git_dir = os.getcwd()
print(git_dir)
gitpull_current_dir(git_dir)
input('press any key to exit')