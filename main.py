import uvicorn
from fastapi import FastAPI
import hentai

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/json/")
async def read_item():
    comic = hentai.Utils.get_random_hentai()
    ok = {
        'title': comic.title(hentai.Format.Pretty),
        'author': [artist.name for artist in comic.artist],
        'tags': [tag.name for tag in comic.tag],
        'img': comic.image_urls,
        'id': comic.id
    }
    return ok
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
