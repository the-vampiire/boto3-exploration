#! /usr/bin/env bash

yum update -y
yum install docker -y

usermod -aG docker ec2-user

docker run -d -p 8008:8008 launchcodedevops/sample-api:node