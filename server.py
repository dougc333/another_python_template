#from lib.logic import wiki, wiki_search
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_client import start_http_server, Summary
import random 
import time
import uvicorn

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


@REQUEST_TIME.time()
async def process_request(t):
    time.sleep(t)



#print("running wiki()")
#print(wiki())
#print("running wikisearch()")
#print(wiki_search())

app = FastAPI()

app.mount("/", StaticFiles(directory="static",html=True), name="static")
#templates = Jinja2Templates(directory="templates")

@app.get("/hi")
async def index():
    return {"Hello":"again"}

    
#@app.get("/",response_class=HTMLResponse)
#async def hi(request: Request):
#    return templates.TemplateResponse("index.html", {"request": request})


uvicorn.run(app, host="127.0.0.1", port=8000)
#migrations sqlalembic
#async mongodb, microxx
#async postgres db very fast
#serve statc out of nginx not fastapi never touch fastapi
#awesome-asgi shows fastapi servers...,
#

