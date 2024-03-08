#!/bin/bash
docker build . -t qscanner && docker run -v $(pwd):/app/output --rm qscanner
