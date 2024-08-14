#!/bin/bash
docker run -d -p 8000:8000  \
	--name operation-site operation-site:v0.1