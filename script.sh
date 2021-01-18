cd flask_app
docker build . -t flask_application
cd ../nginx
docker build . -t my_nginx
cd ..
docker-compose up