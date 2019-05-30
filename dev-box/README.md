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

### Old:

## Docker
Docker and Docker-Compose installed. 

## Python
Ready to go because Ubuntu rules. Try it out by running `python3 /vagrant/python/main.py`.