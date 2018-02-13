import falcon

from resources.home import Home

def create():
    api = application = falcon.API(middleware = [
    ])

    home_resource = Home()

    api.add_route('/', home_resource)
    return api

app = application = create()
