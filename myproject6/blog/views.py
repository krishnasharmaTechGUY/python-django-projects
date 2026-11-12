from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    blogs = [
        {"title": "Django Basics","is_featured":True,"Author":"krishna sharma"},
        {"title": "Django Advanced","is_featured":False,"Author":""},
        {"title": "Django Rest framework","is_featured":False,"Author":"Aarti sharma"},
    ]
    context = {
        "blogs":blogs,
        "today": datetime.now(),
        "html_code":"<h1> welcome to my blog</h1>"
    }
    return render(request, 'blog/blog_list.html', context)