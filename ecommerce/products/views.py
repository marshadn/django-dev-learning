from django.shortcuts import render,redirect
from .models import Product
from .forms import CreateProductForm,UpdateProductForm
# Create your views here.
def index(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'products/index.html',context)

def details(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    return render(request,'products/details.html',context)

def create(request):
    if request.method=='POST':
        form=CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')
    form=CreateProductForm
    context={'form':form}
    return render(request,'products/create.html',context)

def delete(request,id):
     product=Product.objects.get(id=id) 
     product.delete()
     return redirect('/products/')
 
def update(request,id):
    product=Product.objects.get(id=id) 
    if request.method=='POST':
        form=UpdateProductForm(request.POST,instance=product)  
        if form.is_valid():
            form.save()
            return redirect(f'/products/{product.id}')
    form=UpdateProductForm(instance=product)
    context={'product':product,'form':form}
    return render(request,'products/update.html',context)