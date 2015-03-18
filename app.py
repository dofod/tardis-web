from datetime import date
import os
import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.template
from settings import settings
from urls import urls

document = """
  a: 1
  b:
    c: 3
    d: 4
"""

application = tornado.web.Application(
    handlers=urls,
    **settings
)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
