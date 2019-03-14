# DevOps

## Host Machine prerequisites:
- Downloaded Vagrant from: https://www.vagrantup.com/downloads.html
- Downloaded Virtualbox from: https://www.virtualbox.org/wiki/Downloads

## Jenkins
On startup, Jenkins is configured by the contents of `/vagrant/jenkins-config.yaml` via the [Configuration as Code Plugin](https://github.com/jenkinsci/configuration-as-code-plugin) and its [demos](https://github.com/jenkinsci/configuration-as-code-plugin/tree/master/demos).

Access at http://192.168.33.10:8080/

login: admin/secret

## VM Configuration
`/home/vagrant/.profile`
---
`source /vagrant/scripts/functions.sh`

## Ansible
Installed, ready to go.

## Python
Ready to go because Ubuntu rules. Try it out by running `python3 /vagrant/python/main.py`.

## Sonar? That would be sweet.