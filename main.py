import uvicorn
from fastapi import FastAPI
import hentai
import faker, random

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/json/")
async def read_item(exc, inc):
    global comic, found
    hentai.RequestHandler._fake = faker.Faker()
    found = False
    if exc and inc == "None":
        comic = hentai.Utils.get_random_hentai()
    else:
        if inc != "None":
            global ran, maxran
            maxran = 3000
            while True:
                try:
                    ran = random.randint(1, maxran)
                    comics = hentai.Utils.search_by_query(query='tag:' + inc, sort=hentai.Sort.Popular, page=ran)
                    comic = comics[random.randint(0, 24)]
                    found = True
                except IndexError:
                    maxran = ran
        extags = exc.split(', ')
        while True:
            if found == False:
                comic = hentai.Utils.get_random_hentai()
            if (bool(set(extags) & set([tag.name for tag in comic.tag])) == False):
                break
    ok = {
        'title': comic.title(hentai.Format.Pretty),
        'author': [artist.name for artist in comic.artist],
        'tags': [tag.name for tag in comic.tag],
        'img': comic.image_urls,
        'id': comic.id,
        'exclusions': exc,
        'inclusions': inc
    }
    return ok
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
