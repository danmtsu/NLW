from cerberus import Validator
from src.errors.errors_type.http_unprocessable_entity import HttpUnprocessable_entityEntityError

def tag_creator_validator(request: any) -> None:
    body_validator = Validator({
        "product_code":{"type": "string" , "required":True, "empty": False}
    })
    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessable_entityEntityError(body_validator.errors)
