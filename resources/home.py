import falcon
import json

class Home:

    def on_get(self, req, res):
        hello = {
            'hello': 'world'
        }
        res.data = json.dumps(hello).encode('utf-8')
        res.status = falcon.HTTP_200
