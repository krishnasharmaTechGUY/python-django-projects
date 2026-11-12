from django.shortcuts import render
from datetime import datetime


def blog_details(request):
    post={

    "title": "this is my second template post",
    "author":None,
    "descriptions": "django is one of the most used framework for beckend development in python",
    "created_at": datetime(2026,8,4,5,40),
    "comments_count":5,
    "tags": ["django", "python", "webdevelopment"],
    "price": 100,
    "number": 7, 
    }


    return render(request, "blog/blog_details.html", {"post":post})
