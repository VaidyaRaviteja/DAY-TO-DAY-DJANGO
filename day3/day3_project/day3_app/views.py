from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# def test(self):
#     return HttpResponse("Hello everyone today is day 3 of django learning")

# @csrf_exempt
# def welcome(req):
#     method = req.method
#     if method == 'GET':
#         return HttpResponse(f"We are using {method} method")
#     elif method == 'POST':
#         return HttpResponse(f"We are using {method} method")
#     elif method == 'PUT':
#         return HttpResponse(f"We are using {method} method")
#     elif method == 'PATCH':
#         return HttpResponse(f"We are using {method} method")
#     else:   
#         return HttpResponse(f"We are using {method} method")
    

def get_view(req):
    return HttpResponse("This is GET view")
@csrf_exempt
def post_view(req):
    return HttpResponse("This is POST view")

@csrf_exempt
def put_view(req):
    return HttpResponse("This is PUT view")

@csrf_exempt
def patch_view(req):
    return HttpResponse("This is PATCH view")

@csrf_exempt
def delete_view(req):
    return HttpResponse("This is DELETE view")