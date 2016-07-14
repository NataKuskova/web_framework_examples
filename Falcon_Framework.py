import falcon
from wsgiref.simple_server import make_server


class Resource:
    def on_get(self, req, res):
        # print(req.params)  # QS
            # req.stream
        # res.body = str(req.params)
        res.body = '{"message": "test"}'
        res.status = falcon.HTTP_200


api = falcon.API()
r = Resource()
api.add_route('/', r)

serv = make_server('', 8080, api)
serv.serve_forever()
