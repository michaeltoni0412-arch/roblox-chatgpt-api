from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Roblox ChatGPT API</title>
    </head>
    <body style="font-family:Arial;text-align:center;padding-top:80px">
        <h1>Roblox ChatGPT API</h1>
        <h2>🟢 RUNNING</h2>
        <p>The API is ready.</p>
    </body>
    </html>
    """

@app.get("/status")
def status():
    return {"running": True}

@app.post("/send-code")
def send_code(data: dict):
    return {
        "success": True,
        "received": data.get("code", "")
    }
