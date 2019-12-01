from django.shortcuts import render

# Create your views here.

def post_list(requst):
    return render(requst, 'blog/post_list.html')