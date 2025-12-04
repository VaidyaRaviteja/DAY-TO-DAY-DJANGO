from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def test(self):
    # return HttpResponse("Hello this second app from second project of django")
    return JsonResponse({"msg":"Hello this second app from second project of django",
                         "code":200
                         })