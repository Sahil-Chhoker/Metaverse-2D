from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the "static" directory to serve all static files (HTML, JS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the index.html file as the entry point for the Phaser game
@app.get("/")
def serve_game():
    return FileResponse("index.html")

