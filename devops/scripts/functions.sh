#!/bin/bash

function finalize() 
{ 
    sudo apt-get clean
	sudo dd if=/dev/zero of=/EMPTY bs=1M
	sudo rm -f /EMPTY
	sudo cat /dev/null > ~/.bash_history && history -c && exit;
}
