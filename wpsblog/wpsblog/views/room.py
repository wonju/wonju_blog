import requests

from django.http.response import HttpResponse


def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=ture&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
        response.content,
        content_type="application/json",
    )
