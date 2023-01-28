from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import *
from home.models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method=='GET':
        lowStockProducts=Product.objects.filter(qty__lte=10)
        paginator = Paginator(lowStockProducts,5)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
        totalproducts=Product.objects.all().count()
        soldProducts=Sold_prduct.objects.filter(date=datetime.today().date())
        totalSale=0
        for prod in soldProducts:
            totalSale=totalSale + (prod.product.saleprice - prod.costprice)*prod.qty
        topProducts=Product.objects.all().order_by('-countsoldProduct')[:5]
        print(topProducts)
        context={'products':products, 'totalproducts':totalproducts, 'todaysale':totalSale, 'topProducts':topProducts}
        return render(request, 'home/dashboard.html', context)

class CreateProductView(SuccessMessageMixin,CreateView):
    model = Product
    fields=['name', 'qty','costprice','saleprice','prod_model']
    success_url=reverse_lazy('addproduct')
    success_message = "%(name)s was created successfully"
    def form_valid(self,form):
        return super().form_valid(form)
class ListProductView(ListView):
    model=Product
    context_object_name='products'
    paginate_by=10
    fields=['name', 'qty','costprice','saleprice','prod_model']
class DeleteProductView(DeleteView):
    model=Product
    success_messagem= "%(name)% was deleted successfully"
    success_url=reverse_lazy('productlist')
class UpdateProductView(UpdateView):
    model=Product
    template_name='home/update_product_form.html'
    success_url=reverse_lazy('productlist')
    fields=['name', 'qty','costprice','saleprice','prod_model']
def searchProduct(request):
    if request.method=='GET':
        name=request.GET.get('name')
        results=Product.objects.filter(Q(name__icontains=name))#filter(A).filter(B) is OR and filter(A,B) is AND
        # if id is not None or name is not None:
            # results=Product.objects.all()
        # else: 
        context={'products':results}
        return render(request,'home/product_list.html',context)
# -------------------------------sold product-------------------------------------
def soldProduct(request):
    if request.method=='GET':
        products=Product.objects.all()
        soldproducts=Sold_prduct.objects.filter(date=datetime.today().date()).order_by('-costprice')
        paginator = Paginator(soldproducts,5)
        page_number = request.GET.get('page')
        pag_obj = paginator.get_page(page_number)
    #    form=soldProductForm()
        context={'products':products, 'soldp':pag_obj}
        return render(request,'home/soldProduct_form.html',context)
    if request.method=='POST':
        id=request.POST.get('product_id')
        qty=request.POST.get('qty')
        product=Product.objects.get(id=id)
        costprice=product.costprice
        date=datetime.today().date()
        if product is not None and product.qty !=0 and product.qty>=int(qty):
           sold= Sold_prduct()
           sold.product=product
           sold.qty=qty
           sold.costprice=costprice
           sold.date=date
           sold.save()
           messages.success(request,'product sold successfully')
           remaining_qty=product.qty-int(qty)
           product.qty=remaining_qty
           countsoldproduct=int(qty)
           product.countsoldProduct = product.countsoldProduct + countsoldproduct
           print(product)
           product.save()
        else:
            messages.error(request, f'stock is short for  {product.name}. remaining stock {product.qty} and required {qty}')
            context={'product':product}
            return render(request,'home/soldProduct_form.html',context)
    return redirect('soldproduct')