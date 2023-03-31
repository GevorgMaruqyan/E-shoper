from django.shortcuts import render, redirect
from .models import G_Logo, Soc, Category, SubCategory, Brand, HomeSlider, HomeSliderActive, Contact
from .forms import NewUserForm, ContactForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def g_logo():
    logo = G_Logo.objects.all()[0]
    return logo

def home(request):
    slider_activ = HomeSliderActive.objects.all()[0]
    slider = HomeSlider.objects.all()
    category_list = Category.objects.all()
    subcategory_list = SubCategory.objects.all()
    brand_list = Brand.objects.all()
    return render(request, 'main/index.html', context={
        'nbar': 'home', 'logo':g_logo(),
        'category_list':category_list,
        'subcategory_list':subcategory_list,
        'brand_list':brand_list,
        'slider_activ':slider_activ,
        'slider':slider
    })


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={
              "register_form":form, 'nbar': 'register', 'logo':g_logo()
    })

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={
              "login_form":form, 'nbar': 'login', 'logo':g_logo()
    })

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")



def shop(request):
    category_list = Category.objects.all()
    brand_list = Brand.objects.all()
    return render(request, 'main/shop.html', context={
        'nbar': 'shop','logo':g_logo(),
        'category_list':category_list,
        'brand_list':brand_list
    })

def product_details(request):
    category_list = Category.objects.all()
    brand_list = Brand.objects.all()
    return render(request, 'main/product-details.html', context={
        'nbar': 'product-details', 'logo':g_logo(),
        'category_list':category_list,
        'brand_list':brand_list
    })

def checkout(request):
    return render(request, 'main/checkout.html', context={
        'nbar': 'checkout', 'logo':g_logo()
    })

def cart(request):
    return render(request, 'main/cart.html', context={
        'nbar': 'cart', 'logo':g_logo()
    })



def blog(request):
    return render(request, 'main/blog.html', context={
        'nbar': 'blog', 'logo':g_logo()
    })

def blog_single(request):
    return render(request, 'main/blog-single.html', context={
        'nbar': 'blog-single', 'logo':g_logo()
    })

def opps(request):
    return render(request, 'main/404.html', context={
        'nbar': '404'
    })

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = ContactForm()
          
    social = Soc.objects.all()
    return render(request, 'main/contact-us.html', context={
        'nbar': 'contact-us', 'logo':g_logo(),
        'social':social, 'form':form
    })