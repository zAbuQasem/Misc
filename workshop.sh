#!/bin/bash

sudo ls &>/dev/null
echo "[!] Checking if docker is installed"
if ! command -v docker &> /dev/null 
then
  echo -e "[!] Installing Docker...\n"
  sudo apt update
  sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt update
  apt-cache policy docker-ce
  sudo apt install docker-ce -y
  sudo docker pull ubuntu 
  if ! command -v docker &> /dev/null
  then
    echo -e  "\n\n[!] Error installing docker please contact zeyad"
    exit 127
  else
    echo -e "\n\n[+] Installed docker Successfully"
  fi
else
  echo -e "[+] Docker is already installed\n"
fi

#echo "[@] Adding $USER to docker group"
#sudo adduser $USER docker
#echo "[@] Setting up working environment..."; sleep 2
#mkdir ~/Desktop/workshop
#cd ~/Desktop/workshop
#wget https://github.com/zAbuQasem/Misc/raw/main/workshop.tar.gz
#tar -zxvf workshop.tar.gz
#rm -rf workshop.tar.gz
#chmod +x restart.sh
#./restart.sh
