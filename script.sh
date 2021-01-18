cd flask_app/
docker build . -t app_1:1.0
cd ../nginx/
docker build . -t my_nginx:1.0
cd ..
docker-compose up