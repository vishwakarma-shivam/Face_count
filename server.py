from fastapi import FastAPI
import uvicorn
from helper import img64_to_cvImg
from countFace import countFaces

app=FastAPI()


@app.post('/api/countFace/')
async def countFace(ref,img64):
    img=img64_to_cvImg(img64)
    return {"id": ref, "faceCount": countFaces(img)}


if __name__=='__main__':
    uvicorn.run("server:app")


    