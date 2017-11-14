import json
import requests

from django.http.response import HttpResponse
from django.conf import settings

from wpsblog.renderer import render


def home(request):

    context = {}
    return render("home", context)


def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=ture&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
	response.content,
	content_type="application/json",
    )

def news(request):
    search = request.GET.get("search");
    url = "https://watcha.net/home/news.json?page=1&per=50"
    response = requests.get(url)
    news_dict = response.json()
    news_list = news_dict.get("news")
    # news_dict = json.loads(response.text)
    # from IPython import embed; embed()
    if search:
        news_list = list(filter(
            lambda news: search in news.get("title"),
            news_list,)
        )

    news_content = "".join([
        "<h3>{title}</h3><img src={img} /><p>{content}</p>".format(title=news["title"],img=news["image"],content=news["content"])
        for news
        in news_list
    ])

    context = {
        "count" : str(len(news_list)),
        "news_content" : news_content,
    }

    return render("news", context)

