import sys 
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

if os == "ubuntu":
    all = both + ubuntu
    install = "sudo apt update && "
    install += "sudo apt upgrade && "
    install += "sudo apt install"
elif os == "arch":
    all = both + arch
    install = "sudo pacman -Syy && "
    install += "sudo pacman -Su && "
    install += "sudo pacman -S"

all.sort()

for pkg in all:
    install += " {}".format(pkg)

if os == "arch":
    aur.sort()
    install += ' && yaourt --m-arg "--skippgpcheck" -S'
    for pkg in aur:
        install += " {}".format(pkg)
print(install)
