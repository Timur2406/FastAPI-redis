from typing import AsyncGenerator
from fastapi import FastAPI

from fastapi_cache import FastAPICache

from redis_db.manager import backend
from routers import number_router
from core import BaseHTTPException, base_exception_handler


async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    
    FastAPICache.init(backend=backend, prefix="fastapi-cache")

    app.include_router(number_router)

    print('Start')
    yield
    print('End')


app = FastAPI(lifespan=lifespan,
                exception_handlers={
                BaseHTTPException: base_exception_handler
                }
                )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', port=80, host='0.0.0.0', reload=True)