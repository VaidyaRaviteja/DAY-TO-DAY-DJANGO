from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home_page(request):
    return JsonResponse({"msg":"Welcome To Django Day 4"})

# def greet(req):
#     return HttpResponse("Good Afternoon From Django")

def greet(req):
    return JsonResponse({"msg":"Good Afternoon From Django"})

@csrf_exempt
def if_post(req):
    if req.method == "POST":
        return JsonResponse({"msg":"Using POST Method"})
    else:
        return HttpResponse("Not a valid method")