from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/upload-image/")
async def upload_image(image: bytes):
    with open("uploaded_image.jpg", "wb") as f:
        f.write(image)
    return {"message": "Image uploaded successfully"}
