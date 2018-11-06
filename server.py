import os.path
import traceback

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

DEBUG = True

def load_cookie_secret():
    with open('cookie_secret.txt','r') as f:
        content = ''.join(i.strip() for i in f).strip()
    return content

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self,status_code,**kwargs):
        print "error"

class IndexHandler(BaseHandler):
    def get(self):
        if 'Accept-Language' in self.request.headers:
            pass
        self.render('index_en.html')

if __name__ == "__main__":
    define("port", default=10547, help="run on the given port", type=int)
    define("local", default=False, help="designates whether instance is run on the local/server", type=bool)
    tornado.options.parse_command_line()
    
    static_path = os.path.join(os.curdir, "static") 
    template_path = os.path.join(os.curdir, "templates") 

    app_settings = {
        "debug":DEBUG,
        "cookie_secret":load_cookie_secret(),
        "login_url":"/auth/login",
        "xsrf_cookies":True,
        "template_path":template_path
    }
    server_settings = {}

    app = tornado.web.Application(
        [
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path':static_path}),
            (r'/', IndexHandler),
            (r'.*', IndexHandler)
        ], **app_settings
    )
    http_server = tornado.httpserver.HTTPServer(app,**server_settings)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



