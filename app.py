from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Model for text input
class TextInput(BaseModel):
    text: str

@app.post("/text")
async def handle_text(input: TextInput):
    return {"message": "okay"}

@app.post("/image")
async def handle_image(file: UploadFile = File(...)):
    return {"message": "okay"}

@app.post("/audio")
async def handle_audio(file: UploadFile = File(...)):
    return {"message": "okay"}

@app.post("/video")
async def handle_video(file: UploadFile = File(...)):
    return {"message": "okay"}

# For testing purposes: a home route
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app!"}

# Entry point for running directly
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
