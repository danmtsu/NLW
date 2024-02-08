from src.views.http_types.http_response import HttpResponse
from src.errors.errors_type.http_unprocessable_entity import HttpUnprocessable_entityEntityError
def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessable_entityEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "erros":[{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server error",
                "details": str(error)
            }]
        }
    )
