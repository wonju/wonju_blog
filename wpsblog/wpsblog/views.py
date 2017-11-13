import json
import requests

from django.http.response import HttpResponse


def home(request):
    return HttpResponse("hello world")


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

    content = "<h1>News</h1>" +\
        "<h2>This is news page.</h2>" +\
        "<p>{count}개의 영화 정보가 있습니다.</p>".format(count=len(news_list))+\
        "".join([
            "<h3>{title}</h3><img src={img} /><p>{content}</p>".format(title=news["title"],img=news["image"],content=news["content"])
            for news
            in news_list
        ])

    return HttpResponse(
        content
    )

