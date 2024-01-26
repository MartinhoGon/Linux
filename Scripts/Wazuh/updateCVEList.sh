#!/bin/bash

linuxVersion = ('trusty','xenial','bionic','focal','jammy')
destinationFolder = '/home/administrador/wazuh-docker/single-node/canonical_ovals/'

for str in ${linuxVersion[@]}; do
  echo $str
done