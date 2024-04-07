# A simple application to show the usage of docker.

Sample docker run commands:

## Using static values
docker build -t add_static_nums_img:v1 . 

docker run --rm add_static_nums_img:v1

# Using build args: 
docker build --build-arg a="4" --build-arg b="5" -t add_nums_img:v1 -f ./Dockerfile_w_build_args .

docker run --rm add_nums_img:v1  

# Using env vars: 
docker build -t add_nums_img:v1 -f ./Dockerfile_w_env .

docker run --rm -e A="2" -e B="6" add_nums_img:v1 