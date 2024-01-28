from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    # This function render index page of ecommerce views

    return HttpResponse ('Welcome to 6410742289 Thanaphon Muangmaroang views!')

def item_view(request, item_id):   
    
    context_data = {
        "item_id": item_id   
        }
    
    return render(request, 'index.html',context= context_data)

def page_view(request, page_name):

    context_data = {
        "page_name": page_name
    }

    return render(request, f'{page_name}.html', context= context_data)