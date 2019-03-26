FROM publysher/alpine-numpy

LABEL maintainer="Cyrano Chen <cyrano.chen@sap.com>"

EXPOSE 8000 8443 8080 8090

# python server
WORKDIR /home/server
RUN mkdir log && mkdir sample && mkdir label
COPY ./server/cert/ /home/server/cert/
COPY ./server/*.py /home/server/
COPY ./server/label/ /home/server/label/

# python package
COPY ./server/requirements.txt /home/server
RUN pip install -r /home/server/requirements.txt

# nodejs client
WORKDIR /home/client
COPY ./client /home/client/
RUN apk add --update nodejs
RUN npm install

WORKDIR /home
COPY ./start.sh /home/