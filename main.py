# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from service import ipsos

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
 return {"greeting":"Hello world"}

@app.get("/code/{codeword}")
async def code_word(codeword:int):
   ipsosSrv = ipsos.IpsosService()
   return ipsosSrv.find_code(codeword)

@app.get("/action_id/{action}")
async def code_word(action:str):
   ipsosSrv = ipsos.IpsosService()
   return ipsosSrv.find_id(action)    

if __name__ == '__main__':
    uvicorn.run(app, port=3000)
    

