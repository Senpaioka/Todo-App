import asyncio
import tornado

# variables

SERVER_PORT = 8088 
print("Server Open at : http://localhost:8088/")

# classes

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


# functions

def main_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])


# running instance

async def main():
    app = main_app()
    app.listen(SERVER_PORT)
    await asyncio.Event().wait()


if __name__ == '__main__':
    asyncio.run(main())