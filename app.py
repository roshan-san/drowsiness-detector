from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated
import os


app = FastAPI()

@app.get("/hihi")
async def read_root():
    return {"message": "Hello World"}



@app.post("/upload_image/")
async def upload_image(file: Annotated[UploadFile, File()]):
    UPLOAD_FOLDER = "received_images"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    allowed_extensions = {"png", "jpg", "jpeg"}
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid file format. Allowed formats: png, jpg, jpeg")

    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as image_file:
            while content := await file.read(1024):  # Read in chunks
                image_file.write(content)
        return JSONResponse(content={"filename": file.filename, "message": "Image uploaded successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving the image: {e}")

