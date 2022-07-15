from fastapi import FastAPI, Request
import uvicorn
import os
from helper import img64_to_cvImg, getImgfromURL
from countFace import countFaces

app=FastAPI()


@app.post('/api/countFace/')
async def countFace(info: Request):
    data = await info.json()
    img = img64_to_cvImg(data['img'])
    #img=img64_to_cvImg(img64)
    return {"id": data['ref'], "faceCount": countFaces(img)}

@app.post('/api/getCountByUrl/')
async def getCountByUrl(info:Request):
    data = await info.json()
    img=getImgfromURL(data['url'])
    return {"id": data['ref'], "faceCount": countFaces(img)}


if __name__=='__main__':
    #uvicorn.run(app)
    uvicorn.run("server:app", host='0.0.0.0', port=(int)(os.environ.get('PORT', 5000)))


    