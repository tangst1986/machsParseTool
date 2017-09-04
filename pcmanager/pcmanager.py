from tornado.options import define, options
import tornado
import tornado.web
import tornado.httpserver
import os
from tornado.ioloop import PeriodicCallback
from runningTb import RunningTb, engine
from sqlalchemy.orm import sessionmaker, scoped_session

define("port", default=8888, help="run on the given port", type=int)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
        ]

        settings = dict(
            title = u"Pc Manager",
            template_path = os.path.join(os.path.dirname(__file__), "templates")
        )

        super(Application, self).__init__(handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        session = Session()
        instances = session.query(RunningTb).filter_by(type = 'Nyquist')

        nyquist_entries = [{"ip":item.ip, "status":item.status, "username":item.username,
                    "lastuser":item.lastuser,"lastlogintime":item.lastlogintime} for item in instances]

        instances = session.query(RunningTb).filter_by(type = 'Faraday')
        faraday_entries = [{"ip":item.ip, "status":item.status, "username":item.username,
                    "lastuser":item.lastuser,"lastlogintime":item.lastlogintime} for item in instances]

        instances = session.query(RunningTb).filter_by(type = 'FSMr4')
        fsmr4_entries = [{"ip":item.ip, "status":item.status, "username":item.username,
                    "lastuser":item.lastuser,"lastlogintime":item.lastlogintime} for item in instances]
        Session.remove()
        return (nyquist_entries, faraday_entries, fsmr4_entries)


class HomeHandler(BaseHandler):
    def get(self):
        nyquist_entries, faraday_entries, fsmr4_entries = self.db
        catalog_info = [{"name":"Nyquist", "entries":nyquist_entries},
                        {"name":"Faraday", "entries":faraday_entries},
                        {"name":"FSMr4", "entries":fsmr4_entries}]
        self.render("home.html", catalog_info = catalog_info)
        #self.render("home.html", nyquist_entries = nyquist_entries, faraday_entries =faraday_entries,
         #           fsmr4_entries = fsmr4_entries)


def work():
    print "this is the callback"

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    ioloop = tornado.ioloop.IOLoop.instance()

    # background update every x seconds
    task = tornado.ioloop.PeriodicCallback(
            work,
            2 * 1000)
    task.start()

    ioloop.start()

if __name__ == "__main__":
    main()
