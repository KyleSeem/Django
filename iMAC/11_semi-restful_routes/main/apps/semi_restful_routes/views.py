from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Product, Description, Price

# Create your views here.
def index(request):
    context = {
        'products':Product.objects.all()
    }
    return render(request, 'semi_restful_routes/index.html', context)

# shows details for selected item
def show(request, id):
    if request.method == "GET":
        context = {
            'product':Product.objects.get(id=id)
        }
    return render(request, 'semi_restful_routes/show.html', context)

# displays form to define a new product
def new(request):
    return render(request, 'semi_restful_routes/create.html')

# displays form to edit an existing product
def edit(request, id):
    if request.method == "GET":
        context = {
            'product':Product.objects.get(id=id)
        }
    return render(request, 'semi_restful_routes/edit.html', context)

# processes form data to instantiate new product
def createProduct(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['description'] = request.POST['description']

        verify = Product.productManager.create(request.POST)

        if verify[0] == False:
            for alert in verify[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('products:new'))

        elif verify[0] == True:
            request.session.clear()
            return redirect(reverse('products:index'))

# processes form data to update existing product details
def update(request, id):
    if request.method == "POST":
        verify = Product.productManager.change(request.POST, id)

        if verify[0] == False:
            # print('validation failed')
            for alert in verify[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('products:edit', kwargs={'id':id}))

        elif verify[0] == True:
            message = verify[1]
            messages.add_message(request, messages.INFO, message)
            return redirect(reverse('products:index'))

# delete an existing product from the database
def destroy(request, id):
    if request.method == "GET":
        context = {
            'product':Product.objects.get(id=id)
        }
        return render(request, 'semi_restful_routes/delete.html', context)

    elif request.method == "POST":
        Product.objects.get(id=id).delete()
        return redirect(reverse('products:index'))
