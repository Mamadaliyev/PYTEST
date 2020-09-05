import tornado.web
import tornado.ioloop
import asyncio


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(
            'Hello World this is a python command executed from the backend')


class queryParamsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 == 1 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class studentRequestHandler(tornado.web.RequestHandler):
    def get(self, name, id):
        self.write(f"ID of {name} is {id}")


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animals", listRequestHandler),
        (r"/isEven", queryParamsRequestHandler),
        (r"/student/([a-z,A-Z]+)/([0-9]+)", studentRequestHandler),
    ])

    port = 8882
    app.listen(port)
    print(f"Application listening and ready on port {port}")
    tornado.ioloop.IOLoop.current().start()
