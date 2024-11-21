from fastapi import FastAPI
from routers.gpt_router import gpt_router
from routers.translator_router import translator_router 

app = FastAPI()
app.include_router(router=gpt_router)
app.include_router(router=translator_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)