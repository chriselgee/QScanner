# docker build . -t qscanner && docker run -v $(pwd):/app/output --rm qscanner

# Use the official Golang base image to create a build artifact.
FROM golang:1.18

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy the source code into the container
COPY . .

# Prep the build
RUN go clean -modcache
RUN go mod tidy

# Run it on `docker run`, when we can mount the output dir
CMD ["go","build","-o","output/qscanner"]
