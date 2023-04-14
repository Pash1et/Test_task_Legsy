from fastapi import FastAPI

from routers import products

app = FastAPI(title='Parse WB')

app.include_router(products.router)


@app.get('/')
def homepage():
    return {'message': 'Parse WB, go to the 127.0.0.1:8080/docs'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', port=8000, host='0.0.0.0')
