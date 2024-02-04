# main.py
from fastapi import FastAPI
import uvicorn
from service import ipsos

app = FastAPI()
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
    

