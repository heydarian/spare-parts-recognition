FROM publysher/alpine-numpy

LABEL maintainer="Cyrano Chen <cyrano.chen@sap.com>"

EXPOSE 8000 9000 8080 9080

# environment
WORKDIR /home/server
COPY ./server/requirements.txt /home/server
RUN pip install -r /home/server/requirements.txt

# nodejs client
WORKDIR /home/client
RUN apk add --update nodejs
COPY ./client/package.json /home/client
RUN  npm install
COPY ./client /home/client/

# python server
WORKDIR /home/server
RUN mkdir logs && mkdir sample && mkdir label
COPY ./server/cert/ /home/server/cert/
COPY ./server/label/ /home/server/label/
COPY ./server/*.py /home/server/

WORKDIR /home
COPY ./start.sh /home/