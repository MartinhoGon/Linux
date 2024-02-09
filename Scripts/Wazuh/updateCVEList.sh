#!/bin/bash

########################################
##   Developed By Martinho Gonçalves  ##
##             26/01/2024             ##
########################################

linuxVersion=('trusty' 'xenial' 'bionic' 'focal' 'jammy')
destinationFolder='/home/administrador/wazuh-docker/single-node/canonical_ovals'

dockerfolder='/home/administrador/wazuh-docker/single-node'

cd $destinationFolder

# ##Delete all existing OVAL files
rm -rf *.xml

#echo "${#linuxVersion[@]}"

##Download OVALS
for str in ${linuxVersion[@]}; do
  url="https://security-metadata.canonical.com/oval/com.ubuntu.$str.cve.oval.xml.bz2"
  curl -SO $url 
done

bzip2 -d com.ubuntu.*

sed -i '/<?xml version="1.0" ?>/d' com.ubuntu.*

#rebuild docker containers
cd $dockerfolder

docker compose down
docker compose up -d