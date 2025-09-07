from django.shortcuts import render

def show_main(request):
    product = {
        'name': 'Adidas Predator Acceler 1998 Red White Black',
        'price': 32907538,
        'stock': 1,
        'brand': 'Adidas',
        'size': 'Us8,5 Fr42',
        'category': 'Shoes',
        'is_featured': True,
        'description': 
            'Step back into football history with iconic style and unstoppable control. The legendary Predator Acceler 1998 returns in bold red, white, and black, combining classic design with modern comfort. Own the pitch, own the moment.',
        'thumbnail': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.soccerbible.com%2Fperformance%2Ffootball-boots%2F2018%2F08%2Fadidas-reissue-the-1998-predator-accelerator-blackwhitered%2F&psig=AOvVaw1RKg9NCwI7tgzAjmj9Dtve&ust=1757300224276000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCJC528_TxY8DFQAAAAAdAAAAABAE'
    }

    context = {"product": product}
    return render(request, "main.html", context)
