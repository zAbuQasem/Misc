#!/bin/bash

#set -xe
basedir=$(pwd)


Builder(){  
  privchk $1 $2

  # Getting Directory names execluding current dirs
  dirs=$(find $(pwd)/ -mindepth 1 -maxdepth 1 -type d -exec basename {} \;)
  
  for dir in $dirs
  do
    echo -e "\n[+] Building $dir"
    cd "$dir"
    docker build -t "$dir" . 
    docker login --username AWS -p $(aws ecr get-login-password "$2") "$1"
    docker push "$dir"
    # Returning to the base dir
    cd $basedir
  done
}

privchk(){
  chk=$(cat /etc/group | grep -e docker | grep -o $USER)
  if [[ ! -f "$HOME/.aws/config" || ! -f "$HOME/.aws/credentials" ]]; then 
    echo "[!] AWS credentials not found.... Aborting"
    exit 1
  elif [[ "$1" == "help" ]]; then
    echo "---> Usage: $0 <ECR Repo Link> <AWS Profile>"
    exit 0
  elif [[ -z "$chk" ]]; then
    echo "[!] $USER isn't in docker group... aborting"
    exit 1
  elif [[ -z "$EUID" ]]; then 
    echo "[WARNING] You are running as root user here!"
  elif [[ -z "$1" ]];then
    echo "[!] Please specify ECR Repository link"
    exit 1
  elif [[ -z "$2" ]]; then
    echo "[WARNING] You didn't specify a profile argument for AWS"
  fi
}

# Running
Builder $1 $2
