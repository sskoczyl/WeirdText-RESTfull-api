from weirdtext_lib import weird_text

import json

from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse


class Encode(APIView):
    @staticmethod
    def get(request):
        request_body = json.loads(request.body)

        response = {
            "encoded": weird_text.encode(request_body["text"])
        }

        return JsonResponse(response)


class Decode(APIView):

    @staticmethod
    def get(request):
        request_body = json.loads(request.body)

        response = {
            "decoded": weird_text.decode(request_body["text"])
        }

        return JsonResponse(response)
