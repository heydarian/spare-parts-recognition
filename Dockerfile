FROM publysher/alpine-numpy

LABEL maintainer="Cyrano Chen <cyrano.chen@sap.com>"

EXPOSE 8000 8443 8080 8090

# environment
WORKDIR /home/server
COPY ./server/requirements.txt /home/server
RUN pip install -r /home/server/requirements.txt

# nodejs client
WORKDIR /home/client
RUN apk add --update nodejs
COPY ./client /home/client/
RUN npm install

# python server
WORKDIR /home/server
RUN mkdir logs && mkdir sample && mkdir label
COPY ./server/cert/ /home/server/cert/
COPY ./server/label/ /home/server/label/
COPY ./server/*.py /home/server/

WORKDIR /home
COPY ./start.sh /home/