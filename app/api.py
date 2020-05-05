import falcon

from app import views


def create_app() -> falcon.API:
    api = falcon.API()
    api.add_route("/auth_transactions_mock/mastercard", views.MockMastercardView())
    return api
