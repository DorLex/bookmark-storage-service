from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from og_parser.parser import Parser
from og_parser.request_utils import get_page_html


class BookmarkAPIView(APIView):
    def post(self, request):
        # link = request.data.get('link')

        # link = r'https://lenta.ru/news/2023/08/11/pitt_jolie_divorce/'
        link = r'https://www.russianfood.com/recipes/bytype/?fid=99'

        page_html = get_page_html(link)
        parser = Parser(page_html)

        print(parser.title)
        print(parser.description)

        return Response({'result': 123}, status.HTTP_201_CREATED)
