# -*- coding: utf-8 -*-
import base64
import json
import logging
import os
import sys

from time import time

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.escape import json_decode
from tornado.options import define, options

import settings
from recognize import generate_labels, process, export_results
from service import get_image_tensor, extract_feature_vector

define("port", default=int(os.environ.get('PORT', 8080)), help="Spare Parts recognition Server Hub", type=int)
define("ssl_port", default=8443, help="Spare Parts recognition Server Hub", type=int)


class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Cache-Control', 'no-cache')
        self.set_header('Content-Type', 'application/json')

    def post(self, *args, **kwargs):
        try:
            content = self.request.body
            if not content or content == "":
                self.write(json.dumps({"state": "error", "message": "invalid post data"}))
                return

            logging.info(self.request.headers['Content-Type'])

            if self.request.headers['Content-Type'] == 'application/json':
                input_data = json_decode(content)
                # file_name = input_data['filename']
                file_name = str(hash(time())) + os.path.splitext(input_data['filename'])[-1]

                img = base64.b64decode(input_data['image']
                                       .replace('data:image/jpeg;base64,', '')
                                       .replace('data:image/png;base64,', ''))
            else:
                file_name = str(hash(time())) + '.' + self.request.headers['Content-Type'].split('/')[-1]
                img = content

            logging.info('input: ' + file_name)
            with open(settings.SAMPLE_FILEPATH + file_name, 'wb') as f:
                f.write(img)

            results = process(file_name)

            resp = {"state": "success", "filename": file_name, "data": export_results(results)}

            logging.info(resp)
            logging.info('-' * 80)

            self.write(json.dumps(resp))
        except Exception as e:
            # raise e
            self.set_status(500)
            self.write(json.dumps({"state": "error", "message": str(e)}))

    def get(self):
        pass

    def data_received(self, chunk):
        pass

    def options(self):
        # no body
        self.set_status(202)
        self.finish()


class GenerateHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Cache-Control', 'no-cache')
        self.set_header('Content-Type', 'application/json')

    def post(self, *args, **kwargs):
        try:
            labels = generate_labels()

            resp = {"state": "success", "data": labels}

            logging.info(resp)
            logging.info('-' * 80)

            self.write(json.dumps(resp))
        except Exception as e:
            # raise e
            self.set_status(500)
            self.write(json.dumps({"state": "error", "message": str(e)}))

    def get(self):
        pass

    def data_received(self, chunk):
        pass

    def options(self):
        # no body
        self.set_status(202)
        self.finish()


class ExtractHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Cache-Control', 'no-cache')
        self.set_header('Content-Type', 'application/json')

    def post(self, *args, **kwargs):
        try:
            content = self.request.body
            if not content or content == "":
                self.write(json.dumps({"state": "error", "message": "invalid post data"}))
                return

            logging.info(self.request.headers['Content-Type'])

            if self.request.headers['Content-Type'] == 'application/json':
                input_data = json_decode(content)
                # file_name = input_data['filename']
                file_name = str(hash(time())) + os.path.splitext(input_data['filename'])[-1]

                img = base64.b64decode(input_data['image']
                                       .replace('data:image/jpeg;base64,', '')
                                       .replace('data:image/png;base64,', ''))
            else:
                file_name = str(hash(time())) + '.' + self.request.headers['Content-Type'].split('/')[-1]
                img = content

            logging.info('input: ' + file_name)
            with open(settings.SAMPLE_FILEPATH + file_name, 'wb') as f:
                f.write(img)

            fv = extract_feature_vector(get_image_tensor(settings.SAMPLE_FILEPATH + file_name))

            resp = {"state": "success", "filename": file_name, "data": list(fv.astype(float))}

            logging.info(resp)
            logging.info('-' * 80)

            self.write(json.dumps(resp))
        except Exception as e:
            # raise e
            self.set_status(500)
            self.write(json.dumps({"state": "error", "message": str(e)}))

    def get(self):
        pass

    def data_received(self, chunk):
        pass

    def options(self):
        # no body
        self.set_status(202)
        self.finish()


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    # generate_labels()

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[('/api/recognize', MainHandler),
                                            ('/api/generate', GenerateHandler),
                                            ('/api/extract', ExtractHandler),
                                            (r"/labels/(.*)", tornado.web.StaticFileHandler,
                                             {"path": r"./label/b1_items/"})])

    # https_server = tornado.httpserver.HTTPServer(app, ssl_options={
    #     "certfile": "./cert/server.crt",
    #     "keyfile": "./cert/private.pem",
    # })
    # https_server.listen(options.ssl_port)

    http_server = tornado.httpserver.HTTPServer(app)

    if settings.MULTI_PROCESSES_MODE:
        http_server.bind(options.port)
        http_server.start(num_processes=settings.NUM_PROCESSES)
    else:
        http_server.listen(options.port)

    logging.info('tornado server started on port: ' + str(options.port))
    logging.info('-' * 100)
    tornado.ioloop.IOLoop.instance().start()
