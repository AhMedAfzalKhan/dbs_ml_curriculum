# AWS - Setting up your machine
## Let's start installing packages!

#### Check which version of python is installed
```console
ubuntu@ip-172-31-60-68:~$ python --version
Python 2.7.6
ubuntu@ip-172-31-60-68:~$
```
#### Let's use `pip list` to see which packages are installed
```console
ubuntu@ip-172-31-60-68:~$ pip list
The program 'pip' is currently not installed. You can install it by typing:
sudo apt-get install python-pip
```
---
## Some Helpful Notes

#### We can run things as root by prefixing our commands with `sudo`
#### To update your libraries, use `apt-get update`
```
ubuntu@ip-172-31-60-68:~$ sudo apt-get update
```
#### [`apt-get` Package Management Tool](https://help.ubuntu.com/12.04/serverguide/apt-get.html)   
Read more about `apt-get` at above link.  


## Two ways to do Python package management

### The old-school way:
---

#### Install `pip`
Accept all the suggestions it makes, and hit `Enter` and watch it go.  It will take some time for this to finish installing.    
```
ubuntu@ip-172-31-60-68:~$ sudo apt-get install python-pip
```  
> Fun Fact:  Did you know that when you see a yes/no prompt in this format `[Y]/n`, that you can simply hit `Enter` and it will assume you mean the default(capital and bracketed) option?  No need to type a capital Y.  (time saved can be spent on other things.)  
For `apt-get`, you can alsojust add the `-y` flag.  

#### Install `scipy` stack
Now that we're on Ubuntu, we can install our stack of usual tools with this line. (There are convenient `apt-get` packages instead of doing everything via `pip`.)
```console
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook
```
```console
sudo apt-get install python-pandas python-sympy
```

#### Install `emacs` editor
We'll also be interacting with repositories from our server, and I like Emacs, so let's do this.  
```console
sudo apt-get install git emacs
```

---

### The new school way:
---

Go to this website [Anaconda](https://www.anaconda.com/download/#linux) and
find the linux version of anaconda (Python 3.\*). Right click on the button
for that and copy the link address (it should be a **.sh** file). **.sh** files are
  called "shell scripts" and tell the terminal a set of instructions to do. We
  want to go to our new terminal and do (NOTE: Replace with your version of
  the .sh file).

  `wget https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh`

  That will download the file to our new ubuntu machine. To use it, simply do:
  
  `bash Anaconda3-5.1.0-Linux-x86_64.sh`

  This is going to install all of the Anaconda data science stack for python.
  It's going to ask some questions - tell it that 'yes' I want to install this
  and also tell it to install in the default location. You don't need the
  Microsoft Visual coder thing it tries to sell you.

  When that's all done, we need to tell Ubuntu where anaconda lives. To do
  that, go to your home folder and open up the file called `.bashrc`. This
  file contains a bunch of rules that run every time we start up our shell. We
  want to add this line to the file (right at the top is fine).

```
export PATH=/home/ubuntu/anaconda3/bin:$PATH
```

This says, "hey, when you look for programs like python, please also look at
what anaconda installed. Also, when I try to import things to Python, please
look at the python packages that anaconda installed."

That's it: you now have Sklearn, pandas, numpy, etc all installed on your
remote machine. Good on ya'.

---

## Some final setup pointers

**on your local machine:**   
**Open a new shell on your local machine.** You should be able to log in to your remote machine like this:

```console
$ ssh -i /path/to/dot_pem_file ubuntu@123.234.123.234
```
**My example:**  
```console
zachmiller$ ssh -i ~/.ssh/aws_key.pem ubuntu@54.172.80.95
```

---

Nobody wants to type all that. Edit your `~/.ssh/config` (on your local machine):

```
Host name_i_want_to_call_my_aws_instance
     Hostname 123.234.123.234
     User my_username
     IdentityFile /path/to/dot_pem_file
```
**My example:**  
Give your machine the name: `myaws`
```
Host myaws
     HostName 54.172.80.95
     User ubuntu
     IdentityFile ~/.ssh/aws_key.pem
```
Now you can log in to your remote machine with `ssh myaws`.

**My example:**  
```
zachmiller$ ssh myaws
```

#### Send a file from your local machine to your remote machine
```
scp cool_file.png myaws:~
```
**My Example:**  
```
zachmiller$ scp trysql.py myaws:~
```
Note:  check your user account on AWS.  The file was copied there!!! :clap:

---

# THE POSSIBILITIES ARE ENDLESS

Seriously. Think about what you can do.

