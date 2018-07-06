#!/usr/bin/env bash

cwd=$(pwd)
echo "Are you sure you want to uninstall? (Y/n)"
read choice
if [ $choice == 'Y' ] || [ $choice == 'y' ]
then
    #Edit bash_aliases
    sed '/# Url_sniffer settings/d' ~/.bash_aliases > ./temp
    cat temp > ~/.bash_aliases
    sed '/alias sniffurl="python3/d' ~/.bash_aliases > ./temp
    cat temp > ~/.bash_aliases

    #Remove the folder and all files
    rm -rf ~/.url_sniffer
    echo "Uninstalling Complete - Please delete the ~/.url_sniffer directory if it still exists"

else
    echo "Uninstalling aborted - Great Choice"
fi