from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies' : ['Avengers', 'Batman', 'Django']
    }
    return render(request, 'movies/index.html', context) # dictionaries/objects/lists that we would want to render would be the third parameter
# The third parameter is known as the 'context'

def about(request):
    context = {
        'information' : {'first_name' : 'Jon', 
                         'last_name' : 'Ann', 
                         'age' : 25}
    }
    return render(request, 'movies/about.html', context)