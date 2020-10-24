from django.shortcuts import redirect, render
from django.http import HttpResponse

notes = [
    {'content' : 'hello world!, this is the first post in the whole website!', 'author' : 'noU'},
    {'content' : 'hi!, this is the second post in website. not static, its in the database', 'author' : 'Testuser2'},
    {'content' : 'webapps are great since you can access them anywhere on any platforms', 'author' : 'maker of this gay website'},
    {'content' : 'just a placebo note to see where does this go', 'author' : 'hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm'}
]

def homepage(request):
    return render(request, 'homepage/index.html', {'title':'Homepage', 'notes':notes})

def about(request):
    return render(request, 'about/index.html', {'title' : 'About'})

def features(request):
    return render(request, 'features/index.html', {'title' : 'features'})

def stats(request):
    return render(request, 'stats/index.html', {'title' : 'stats'})

def contact(request):
    return render(request, 'contact/index.html', {'title' : 'contact'})