import falcon

from app import auth, views


def create_app() -> falcon.API:
    api = falcon.API(middleware=[auth.ServiceAPIKeyMiddleware()])
    api.add_route("/auth_transactions_mock/mastercard", views.MockMastercardView())
    return api
