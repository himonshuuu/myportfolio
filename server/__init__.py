import time
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .middlewares.nocachestatic import NoCacheStaticMiddleware
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(NoCacheStaticMiddleware)

projects = []
with open("server/projects.json", "r") as f:
    projects = json.loads(f.read())


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "home/index.html",
        {
            "request": request,
            "time": time.time(),
            "title": "Himonshu's Portfolio",
            "description": "I'm a self-taught developer who loves to code and build cool projects.",
            "og_description": "I'm a self-taught developer who loves to code and build cool projects.",
            "keywords": "Himonshu, IPv6, website, cool, personal",
            "projects": projects,
            "now": datetime.now(),
            "og_title": "Himonshu's Portfolio",
            "og_url": "https://himonshu.com",
            "og_type": "website",
            "og_locale": "en_US",
            "og_site_name": "Himonshu's Portfolio",
        },
    )


def run(port=443):
    import uvicorn

    print(f"HTTPS server started on port {port}")

    try:
        uvicorn.run(
            "server:app",
            host="::",
            port=port,
            reload=True,
            reload_dirs=["server"],
            ssl_keyfile="key.pem",
            ssl_certfile="cert.pem",
        )
    except KeyboardInterrupt:
        print("\nServer shutting down...")
