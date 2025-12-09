from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def my_details(req):
    if req.method == "GET":
        return JsonResponse({"Country":"India","state":"Telangana","City":"Hyderabad"})
    else:
        return HttpResponse("Sorry not supported to this method")



