import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

hello_world = """
<h1>Hello, <s>world</s> devhub!</h1>
<a href="http://github.com/hgenru/hello-devhub">fork me on github</a>
"""
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(hello_world)
 
def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()