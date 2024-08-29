#!/bin/bash


app_name=${1:-'Operation-site'}
version=${2:-`date +%Y-%m%d-%H%m`}
harbor_url=${3:-'172.17.200.84:80'}
git_branch=${4:-'main'}

#release=$(git describe --abbrev=0 --tags)

docker buildx build --push --no-cache \
	--build-arg APP_Version="${version}" \
    --build-arg APP_Name="${app_name}" \
	-t "${harbor_url}/yyd/${app_name}-${git_branch}:${version}" \
	-f Dockerfile .

docker buildx prune -f
