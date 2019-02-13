from django.shortcuts import render, redirect
from .models import Product, Contact
from .forms import ProductForm
from  django.contrib import  messages
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

def list_products(request):
    pesquisa = request.GET.get('pesquisa', None)
    if pesquisa:
        products = Product.objects.filter(description__contains =pesquisa)
        #SQL select from clientes nome LIKE %nome%
       #clientes = clientes.filter(nome=termo_busca)
    else:
        products = Product.objects.all()
    return render(request, 'products/lista.html', {'products':products})

def list_tabela(request):
    pesquisa = request.GET.get('pesquisa', None)
    if pesquisa:
        products = Product.objects.filter(description__contains =pesquisa)
        #SQL select from clientes nome LIKE %nome%
       #clientes = clientes.filter(nome=termo_busca)
    else:
        products = Product.objects.all()
    return render(request, 'products/tabela.html', {'products':products})

def list_tabela2(request):
    pesquisa = request.GET.get('pesquisa', None)
    if pesquisa:
        products = Product.objects.filter(description__contains =pesquisa)
        #SQL select from clientes nome LIKE %nome%
       #clientes = clientes.filter(nome=termo_busca)
    else:
        products = Product.objects.all()
    return render(request, 'products/tabela2.html', {'products':products})

def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, ('Salvo Com Seucesso'))
        return redirect('list_products')

    return render(request, 'products/inserir.html', {'form':form})

def update_product(request):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
    return render(request, 'products-form.html', {'form': form, 'product': product})


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'product': product})

@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template = "contact_upload.html"

    prompt = {
       # 'order': "Order of csv should be first_name, last_name, email, ip_address, message"
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.txt'):
        messages.error(request, "This file is not a .txt file")

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)

    for column in csv.reader(io_string):
        linha = ''.join(str(e) for e in column)
        linha2=  linha[:9]
        _, created = Contact.objects.update_or_create(
            first_name= linha2,
            #last_name=column[1],
           # email=column[2],
            #ip_address=column[3],
            #message=column[4]
        )

    context = {}
    return render(request, template, context)