docker rm -f spare-parts-recognition-server
docker build -f Dockerfile-server -t cyranochen/spare-parts-recognition-server:latest ../server
# docker push cyranochen/spare-parts-recognition-server:latest