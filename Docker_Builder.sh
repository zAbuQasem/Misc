#!/bin/bash

set -xe
basedir=$(pwd)

# Getting Directory names execluding current dir
dirs=$(find $(pwd)/ -mindepth 1 -maxdepth 1 -type d -exec basename {} \;)

Builder{  
  privchk $1
  for dir in "$dirs"
  do
    cd $dir
    docker build -t $dir . 
    aws ecr get-login-password \
        | docker login 
        --username AWS 
        --password-stdin
        $1
      docker push "$dir"
        # Returning to the base dir
        cd $basedir
  done
}


privchk{
  chk=$(cat /etc/group | grep -e docker | grep -o $USER)
  if [[ ! -f "$HOME/.aws/config" || ! -f "$HOME/.aws/credentials"]]; then 
    echo "[!] AWS credentials not found.... Aborting"
    exit 1
  elif [[ -z "$chk" ]]; then
    echo "[!] $USER isn't in docker group... aborting"
    exit 1
  elif [[ -z "$EUID" ]]; then 
    echo "[WARNING] You are running as root user here!"
  elif [[ -z "$1" ]];then
    echo "[!] Please specify ECR Repository link"
    exit 1
  fi          
}
