**A simple application to show the usage of docker. **

Sample docker run commands:


docker build --build-arg a="2" -t add_nums_img:v1 -f ./Dockerfie_w_args .

docker run --rm add_nums_img:v1  

docker build -t add_static_nums_img:v1 . 

docker run --rm add_static_nums_img:v1
