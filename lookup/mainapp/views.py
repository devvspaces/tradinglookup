import requests

from django.shortcuts import render

# Create your views here.
def search(request):
    context = {'found': True}

    # Get the search from the get obj
    search = request.GET.get('search')
    if search:
        # Call api and pass search parameter
        response = requests.get(url='http://127.0.0.1:8000/', params={'search': search})
        result = response.json()

        if result:
            obj = result[0]

            context['result'] = obj
        else:
            context['found'] = False

    return render(request, 'mainapp/index.html', context=context)