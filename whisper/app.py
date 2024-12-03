from fastapi import FastAPI, File, UploadFile
import whisper
from gtts import gTTS
import os

app = FastAPI()

# Load Whisper model
model = whisper.load_model("base")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Whisper Multilingual API!"}

@app.post("/speech-to-text/")
async def speech_to_text(audio: UploadFile = File(...)):
    """
    Transcribe speech to text.
    """
    try:
        # Save the uploaded file temporarily
        temp_file = f"temp_{audio.filename}"
        with open(temp_file, "wb") as f:
            f.write(await audio.read())
        
        # Perform transcription
        result = model.transcribe(temp_file)
        transcription = result["text"]

        # Remove temporary file
        os.remove(temp_file)

        return {"transcription": transcription}
    except Exception as e:
        return {"error": str(e)}

@app.post("/detect-language/")
async def detect_language(audio: UploadFile = File(...)):
    """
    Detect the language of the speech.
    """
    try:
        # Save the uploaded file temporarily
        temp_file = f"temp_{audio.filename}"
        with open(temp_file, "wb") as f:
            f.write(await audio.read())
        
        # Perform language detection
        result = model.transcribe(temp_file)
        detected_language = result["language"]

        # Remove temporary file
        os.remove(temp_file)

        return {"detected_language": detected_language}
    except Exception as e:
        return {"error": str(e)}

@app.post("/translate-to-english/")
async def translate_to_english(audio: UploadFile = File(...)):
    """
    Transcribe and translate speech to English text.
    """
    try:
        # Save the uploaded file temporarily
        temp_file = f"temp_{audio.filename}"
        with open(temp_file, "wb") as f:
            f.write(await audio.read())
        
        # Perform transcription and translation
        result = model.transcribe(temp_file, task="translate")
        translation = result["text"]

        # Remove temporary file
        os.remove(temp_file)

        return {"translation": translation}
    except Exception as e:
        return {"error": str(e)}

@app.post("/text-to-audio/")
async def text_to_audio(text: str, language: str):
    """
    Convert text to audio in English or Hindi.
    """
    try:
        if language not in ["en", "hi"]:
            return {"error": "Unsupported language. Please use 'en' for English or 'hi' for Hindi."}
        
        # Generate audio using gTTS
        tts = gTTS(text=text, lang=language)
        audio_file = "output.mp3"
        tts.save(audio_file)

        return {"audio_file": audio_file, "message": "Text-to-Audio conversion successful!"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/enhance-audio/")
async def enhance_audio(audio: UploadFile = File(...)):
    """
    Noise handling and enhance audio quality.
    """
    # Placeholder for advanced noise handling
    return {"message": "Noise handling is not yet implemented. Please integrate your preferred enhancement library."}
