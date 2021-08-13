from django.shortcuts import render

def index(request):
    mentor_list = [
        {'name': 'name1', 'subject': 'math'},
        {'name': 'name2', 'subject': 'math'},
        {'name': 'name3', 'subject': 'english'},
        {'name': 'name4', 'subject': 'english'},
    ]

    context = {
        'mentor_list': mentor_list
    }

    return render(request, 'index.html', context)