from django.shortcuts import render, get_object_or_404, redirect
from .models import Good, Cart


# Create your views here.
def home(request):
    goods = Good.objects.all()
    return render(request, 'core/home.html', {'goods':goods})

def info(request, pk):
    good = get_object_or_404(Good, pk=pk)
    return render(request, 'core/good_info.html', {'good': good})

def add_good(request, pk):
    if request.method == 'POST':
        # amount = request.GET.get("amount_goods")
        cart = get_object_or_404(Cart, user=request.user)
        if cart is not None:
            good = Good.objects.filter(id=pk)
            cart.goods_list.add(good[0])
            return redirect('cart')
        else:
            cart = Cart(user=request.user, goods_list=None)
            cart.save()
            good = Good.objects.filter(id=pk)
            cart.goods_list.add(good[0])
            return redirect('cart')


def remove_good(request, pk):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        good = Good.objects.filter(id=pk)
        cart.goods_list.remove(good[0])
        return redirect('cart')


def cart(request):
    goods_in_cart = Cart.objects.filter(user=request.user)
    # print(goods_in_cart[1].goods.list)
    return render(request, "core/cart.html", {"cart": goods_in_cart})
