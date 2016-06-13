# -*-  conding: utf8  -*-

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/vendor")

import tornado.options
import tornado.ioloop
import tornado.web
import tornado.template
import tornado.auth
import tornado.locale
import tornado.httpclient
import tornado.httpserver

from setting import settings


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "anonymous")
        self.render('./template/hello.html', name=name)


application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    tornado.options.define("port", default=8001, help="Run server on a specific port", type=int)
    tornado.options.parse_command_line()
    application_server = tornado.httpserver.HTTPServer(application)
    application_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


