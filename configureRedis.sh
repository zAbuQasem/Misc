#!/bin/bash

function Basic_Install
{
	echo "Starting the installation process"
	# Install redis 
	sudo apt install redis-server -y
	sudo apt-get install redis-tools -y

	# Setup systemd for ubuntu
	sudo sed -i 's/supervised no/supervised systemd/g' /etc/redis/redis.conf

	# Restart redis to apply configuration
	sudo systemctl restart redis.service

	# Test if everything is OK
	echo "ping" | redis-cli -h 127.0.0.1

	if [[ "echo $?" == "0" ]];
	then
		echo "Done"
	else
		echo "Error Ocuured during installation Process"
	fi
}

Basic_Install
