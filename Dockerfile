FROM nginx:alpine
LABEL Name=findthebutton Version=0.0.1
COPY . /usr/share/nginx/html
EXPOSE 80
