from werkzeug.routing import Map, Rule
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server
from werkzeug.wrappers import Request, Response


def form(req, **v):
    print(v)
    return Response('Hi')


route = {
    'form': form,
    'form1': form
}


@Request.application
def app(req):
    url_map = Map([
        Rule('/', endpoint='index'),
        Rule('/form', endpoint='form'),
        Rule('/form/<id>', endpoint='form1')
    ])
    urls = url_map.bind_to_environ(req.environ)
    return urls.dispatch(lambda e, v: route[e](req, **v))


serv = make_server('', 8080, app)
serv.serve_forever()
