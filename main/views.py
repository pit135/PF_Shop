from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Petrus Wermasaubun',
        'class': "PBP B",
  
    }

    return render(request, "main.html", context)