import json
import tornado.ioloop
import tornado.web
import tornado.websocket

from storage import RedisStorage


clients = []


class SenderHandler(tornado.web.RequestHandler):
    def post(self, id):
        data = json.loads(self.request.body)
        for client in clients:
            client.write_message(data)
        storage.set(id, data)
        self.set_status(201)


class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "web_socket opened"
        clients.append(self)

    def on_close(self):
        print "web_socket closed"
        clients.remove(self)


application = tornado.web.Application(
    [
        (r"/sender/([0-9]+)/", SenderHandler),
        (r"/channel/", SocketHandler),
    ],
    autoreload=True
)


if __name__ == "__main__":
    storage = RedisStorage('localhost', '6379')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
