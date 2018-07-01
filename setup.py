#!/usr/bin/env python3
import os

# ask confirmation
confirm = input("Do you want to install(Y/n): ")
if confirm == 'Y' or confirm == 'y':

    # handling all the directories gracefully
    cwd = os.getcwd()
    path_to_sniff = cwd + "/sniff.py"
    if os.path.isdir("~/.url_sniffer"):
        os.system("mkdir  ~/.url_sniffer")
    path_to_installation_dir = "~/.url_sniffer/url_sniffer"
    command_to_copy = "cp -R " + cwd + " " + path_to_installation_dir + "/"
    bashrc = "~/.bash_aliases"

    # copying and giving execute access
    os.system(command_to_copy)
    os.system("chmod +x " + path_to_installation_dir + "/sniff.py")

    # add to path
    os.system('echo "# Url_sniffer settings" >> ' + bashrc) 
    os.system(('''echo 'alias sniffurl="python3 ''' + path_to_installation_dir + '''/sniff.py"' >> ''' + bashrc))
    os.system('echo "case $- in *i*) . ~/.bash_aliases;; esac" >> ~/.bash_profile')

    print("Installation complete!")

else:
    print("Installation Aborted!")



