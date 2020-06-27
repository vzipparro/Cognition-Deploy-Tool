from subprocess import Popen, PIPE, run
from os import path
import tkinter as tk
import git
import shutil

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400, bg = 'gray90', relief = 'raised')
canvas1.pack()

user_repo_path = path.expanduser("~/Desktop")
repository  = path.dirname(rf'{user_repo_path}/Cognition/') 
git_pull_command = ['/usr/bin/git', 'pull']

def gitRetrieve():
    if path.exists(repository):
        git_pull_command = ['/usr/bin/git', 'pull']
        git_query = Popen(git_pull_command, cwd=repository, stdout=PIPE, stderr=PIPE)
        (git_status, error) = git_query.communicate()
        print(f'The repo already exists on your desktop and the status is: {git_status}')  
    else:
        git.Git(user_repo_path).clone("https://github.com/cloudvox/Cognition.git")
        git_pull_command = ['/usr/bin/git', 'pull']
        git_query = Popen(git_pull_command, cwd=repository, stdout=PIPE, stderr=PIPE)
        (git_status, error) = git_query.communicate()
        print(f'The repo has been cloned to your desktop and the statis is: {git_status}') 

def removeRepoFromDesktop():
    shutil.rmtree(repository)
    print(f'{repository} has been deleted from your desktop')

def deployStatus():
    Popen(["time", "bundle", "exec", "cap", "test-new", "deploy:web:status"], cwd=repository)

def deployCheck():
    Popen(["time", "bundle", "exec", "cap", "test-new", "deploy:check"], cwd=repository)

def deployToTest():
    Popen(["time", "bundle", "exec", "cap", "test-new", "deploy"], cwd=repository)

button1 = tk.Button(text='Git Pull', command=gitRetrieve)
button2 = tk.Button(text='Deploy Status', command=deployStatus)
button3 = tk.Button(text='Deploy Check', command=deployCheck)
button4 = tk.Button(text='Deploy Code to Test', command=deployToTest)
button5 =  tk.Button(text='Delete Repo From Desktop', command=removeRepoFromDesktop)
# output  = tk.Entry(root)

canvas1.create_window(200, 75, window=button1)
canvas1.create_window(200, 125, window=button2)
canvas1.create_window(200, 175, window=button3)
canvas1.create_window(200, 225, window=button4)
canvas1.create_window(200, 275, window=button5)
# canvas1.create_window(250, 300, window=output)

root.title("Cognition Deploy Tool")
root.mainloop()
