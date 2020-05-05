import falcon
from falcon.media.validators import jsonschema

from app import queues


_schema = {
    "type": "object",
    "properties": {
        "third_party_id": {"type": "string"},
        "time": {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"},
        "amount": {"type": "number"},
        "currency_code": {"type": "string"},
        "payment_card_token": {"type": "string"},
        "mid": {"type": "string"},
    },
    "required": ["third_party_id", "time", "amount", "currency_code", "payment_card_token", "mid"],
}


class MockMastercardView:
    @jsonschema.validate(_schema)
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        with queues.mastercard_auth() as q:
            q.put(req.media)
        resp.media = req.media
