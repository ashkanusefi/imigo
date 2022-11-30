import requests
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class NewsList(APIView):
    def get(self, request):
        response = requests.get(
            "https://feeds.npr.org/1004/feed.json").json()["items"][-5:]
        for i in response:
            try:  # check if the new is in database or not
                News.objects.get(new_id=i['id'])
                continue
            except:  # creating the news in database
                try:  # this is a simple error handling
                    image_url = i.get('image')
                    name = image_url.split('/')[-1]
                    with open(str(BASE_DIR) + f'/media/news/{name}',
                              'wb') as File:
                        File.write(requests.get(image_url).content)
                    News.objects.create(new_id=i.get('id' or None), url=i.get('url' or None),
                                        title=i.get('title' or None),
                                        summary=i.get('summary' or None),
                                        date_published=i.get('date_published') or None,
                                        date_modified=i.get('date_modified') or None,
                                        image=File.name.split('/media')[1])
                except:  # raising errors
                    msg = "some errors"
                    return Response(msg)
        return Response(response)
