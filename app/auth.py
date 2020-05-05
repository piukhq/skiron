import falcon

import settings


class ServiceAPIKeyMiddleware:
    def process_request(self, req: falcon.Request, resp: falcon.Response):
        try:
            auth_header = req.headers["AUTHORIZATION"]
        except KeyError:
            raise falcon.HTTPForbidden(title="Unauthorised", description="Missing authorization header")

        try:
            auth_type, credentials = auth_header.split()
        except ValueError:
            raise falcon.HTTPForbidden(title="Unauthorised", description="Malformed authorization header")

        if auth_type.lower() != "token":
            raise falcon.HTTPForbidden(title="Unauthorised", description="Incorrect authorization type")

        if credentials != settings.SERVICE_API_KEY:
            raise falcon.HTTPForbidden(title="Unauthorised", description="Incorrect credentials")
