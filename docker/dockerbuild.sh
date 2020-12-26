docker-compose down
docker build -f Dockerfile-client -t cyranochen/spare-parts-recognition-client:latest ../client
docker build -f Dockerfile-server -t cyranochen/spare-parts-recognition-server:latest ../server
docker push cyranochen/spare-parts-recognition-client:latest
docker push cyranochen/spare-parts-recognition-server:latest