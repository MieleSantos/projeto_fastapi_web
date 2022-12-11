from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

app = FastAPI(docs_url=None, redoc_url=None)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")


@app.get("/", name="index")
async def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/index.html", context=context)


@app.get("/about", name="about")
async def about(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("about/index.html", context=context)


@app.get("/contact", name="contact")
async def contact(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("contact/index.html", context=context)


@app.get("/pricing", name="pricing")
async def pricing(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("pricing/index.html", context=context)


@app.get("/faq", name="faq")
async def faq(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("faq/index.html", context=context)


@app.get("/blogs_home", name="blogs_home")
async def blogs_home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("blogs/blog_home/index.html", context=context)


@app.get("/blogs_post", name="blogs_post")
async def blogs_post(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("blogs/blog_post/index.html", context=context)


@app.get("/portfolio_item", name="portfolio_item")
async def portfolio_item(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(
        "portfolio/portfolio_item/index.html", context=context
    )


@app.get("/portfolio_overview", name="portfolio_overview")
async def portfolio_overview(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(
        "portfolio/portfolio_overview/index.html", context=context
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app", host="0.0.0.0", port=8001, log_level="info", reload=True
    )
