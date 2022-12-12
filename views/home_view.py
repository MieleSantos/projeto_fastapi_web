from fastapi.routing import APIRouter
from fastapi.requests import Request
from core.configs import settings

router = APIRouter()
templates = settings.TEMPLATES


@router.get("/", name="index")
async def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/index.html", context=context)


@router.get("/about", name="about")
async def about(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("about/index.html", context=context)


@router.get("/contact", name="contact")
async def contact(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("contact/index.html", context=context)


@router.get("/pricing", name="pricing")
async def pricing(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("pricing/index.html", context=context)


@router.get("/faq", name="faq")
async def faq(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("faq/index.html", context=context)


@router.get("/blogs_home", name="blogs_home")
async def blogs_home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("blogs/blog_home/index.html", context=context)


@router.get("/blogs_post", name="blogs_post")
async def blogs_post(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("blogs/blog_post/index.html", context=context)


@router.get("/portfolio_item", name="portfolio_item")
async def portfolio_item(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(
        "portfolio/portfolio_item/index.html", context=context
    )


@router.get("/portfolio_overview", name="portfolio_overview")
async def portfolio_overview(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(
        "portfolio/portfolio_overview/index.html", context=context
    )
