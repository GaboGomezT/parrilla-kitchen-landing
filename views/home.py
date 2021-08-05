import fastapi
from fastapi_chameleon import template
from starlette import status
from starlette.requests import Request

router = fastapi.APIRouter()


@router.get('/')
@template()
def index(request: Request):
    return {}