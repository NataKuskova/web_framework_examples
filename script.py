from werkzeug.wrappers import Request, Response
from wsgiref.simple_server import make_server

"""
def app(env, start_res):
    req = Request(env)
    res = Response('', mimetype='text/html')
    print(req.args)
    print(req.form)
    print(req.files)
    print(req.path)
    print(req.environ)
    return res(env, start_res)
"""


@Request.application
def app(req):
    return Response('')


serv = make_server('', 8080, app)
serv.serve_forever()