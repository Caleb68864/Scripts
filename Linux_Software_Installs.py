import sys 
import os 
import subprocess 
# print "This is the name of the script: ", sys.argv[0] 
# print "Number of arguments: ", len(sys.argv) 
# print "The arguments are: " , str(sys.argv)

os = sys.argv[1] 
both = ["vlc", "terminator", "ranger", "vim", "tmux", "zsh", "python", "python-pip", "git", "htop", "dmenu", "vsftpd", "youtube-dl", "gimp", "inkscape"]
ubuntu = ["openssh-server"]
arch = ["openssh"]
aur = ["pithos", "google-chrome"]

all = []
install = ""

commands = []
pkg_manager = ""

if os == "ubuntu":
    all = both + ubuntu
    #install = "sudo apt update && "
    #install += "sudo apt upgrade && "
    #install += "sudo apt install"
    
    pkg_manager = "sudo apt install"
    commands.append(["sudo", "apt", "update"])
    commands.append(["sudo", "apt", "upgrade", "-y"])

elif os == "arch":
    all = both + arch
    #install = "sudo pacman -Syy && "
    #install += "sudo pacman -Su && "
    #install += "sudo pacman -S"

    pkg_manager = "sudo pacman -S"
    commands.append(["sudo", "pacman", "-Syy"])
    commands.append(["sudo", "pacman", "-Su"])

all.sort()

for pkg in all:
    install += " {}".format(pkg)

pi = pkg_manager + install

commands.append(pi.split(" "))

if os == "arch":
    aur.sort()
    yaourt += 'yaourt --m-arg "--skippgpcheck" -S'
    y_install = ""
    for pkg in aur:
        y_install += " {}".format(pkg)

    yi = yaourt + y_install

    commands.append(yi.split(" "))

pip_pkgs = ["pandas", "numpy", "youtube-dl", "xlrd", "wxPython"]
pip = "sudo pip install"
pip_install = ""

for pkg in pip_pkgs:
    pip_install += " {}".format(pkg)

pipi = pip + pip_install

commands.append(pipi.split(" "))

for command in commands:
    subprocess.call(command)
