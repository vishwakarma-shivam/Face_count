from fastapi import FastAPI
import uvicorn
import os
from helper import img64_to_cvImg, getImgfromURL
from countFace import countFaces

app=FastAPI()


@app.post('/api/countFace/')
async def countFace(ref,img64):
    img=img64_to_cvImg(img64)
    return {"id": ref, "faceCount": countFaces(img)}

@app.post('/api/getCountByUrl/')
async def getCountByUrl(ref,url):
    img=getImgfromURL(url)
    return {"id": ref, "faceCount": countFaces(img)}


if __name__=='__main__':
    #uvicorn.run(app)
    uvicorn.run("server:app", host='0.0.0.0', port=(int)(os.environ.get('PORT', 5000)))


    