from subprocess import Popen, PIPE, run
from os import path
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 500, bg = 'gray90', relief = 'raised')
canvas1.pack()
repository  = path.dirname(r'/Users/vzipparro/Documents/Github Repos/Cognition/') 
git_command = ['/usr/bin/git', 'pull']

def gitpull ():
    git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
    (git_status, error) = git_query.communicate()
    print(git_status)  

def deployStatus():
    Popen(["time", "bundle", "exec", "cap", "test-new", "deploy:web:status"], cwd=repository)
QA
def deployCheck():
    Popen(["time", "bundle", "exec", "cap", "test-new", "deploy:check"], cwd=repository)

def deployToTest():
    Popen(["time", "bundle", "exec", "cap", "test-new", "deploy"], cwd=repository)

button1 = tk.Button(text='Git Pull', command=gitpull)
button2 = tk.Button(text='Deploy Status', command=deployStatus)
button3 = tk.Button(text='Deploy Check', command=deployCheck)
button4 = tk.Button(text='Deploy Code to Test', command=deployToTest)
output  = tk.Entry(root)

canvas1.create_window(250, 75, window=button1)
canvas1.create_window(250, 125, window=button2)
canvas1.create_window(250, 175, window=button3)
canvas1.create_window(250, 225, window=button4)
canvas1.create_window(250, 275, window=output)


root.mainloop()
