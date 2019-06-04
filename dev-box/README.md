# Dev-Box

Ubuntu 18.04

## Host Machine prerequisites:
- Downloaded Vagrant from: https://www.vagrantup.com/downloads.html
- Downloaded Virtualbox from: https://www.virtualbox.org/wiki/Downloads

## Finalizing Box:

`sudo apt-get clean`
`sudo dd if=/dev/zero of=/EMPTY bs=1M`
`sudo rm -f /EMPTY`
`sudo cat /dev/null > ~/.bash_history && history -c && exit;`
`vagrant package --output pick1.box`

## Out of Space Error
This happens from time to time and I'm working on isolating a solution.

Initially, it seemed like the cause was the `sudo dd if=/dev/zero of=/EMPTY bs=1M` command. By packaging box 1.0.1 without this command, the error did not occur. The trouble is this command is very useful, and helps to minimize the compression size of the box file, so I kinda want to us it. 

What I'm trying now is to repackage 1.0.1 and `vagrant up` after deleting the `.vagrant` directory since that dir being around has caused issues before.

If you make a box and then get a runtime error about no more disk space, it's probably because you forgot to run the `sudo rm -f /EMPTY` command when finalizing. Then again no? I used it and it still failed. wtf.

As of dev-box 1.0.2, I was able to get past the error for the intermediate step of turning off the docker image. The next step is to try and get a box that has maven and maven dependencies installed without hitting the out of space error.

### Features:

## Docker
Docker and Docker-Compose installed. 

## Python
Ready to go because Ubuntu rules. Try it out by running `python3 /vagrant/python/main.py`.

## Current Version
We're back on v1.0.2 since it's Gradle now instead of Maven. I haven't installed Gradle yet since I'm just running from the local for now.