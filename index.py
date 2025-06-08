import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, World, This is a python command. Executed from the backend")

class listRequestHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")



if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",BasicRequestHandler),
        (r"/animal",listRequestHandler)
    ])

    port  = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()



