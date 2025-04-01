#!/bin/bash

export ENVIRONMENT_NAME=dcapt-product

for i in {1..1}
do
   docker run --pull=always --env-file ./app/util/k8s/aws_envs -e REGION=us-east-2 -e ENVIRONMENT_NAME=$ENVIRONMENT_NAME -v "/$PWD:/data-center-terraform/dc-app-performance-toolkit" -v "/$PWD/app/util/k8s/bzt_on_pod.sh:/data-center-terraform/bzt_on_pod.sh" -it atlassianlabs/terraform:2.9.7 bash bzt_on_pod.sh confluence.yml
   sleep 20
done
