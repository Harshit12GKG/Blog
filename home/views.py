from calendar import c
from django.shortcuts import redirect, render, HttpResponse
from flask import render_template
from . forms import *
from django.contrib.auth import logout
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/')

#Home View
def index(request):
    user = request.user
    context = {'blogs' : BlogModel.objects.all(), 'user' : user}
    return render(request, 'home.html', context)

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] = blog_obj
        context['blogs'] = BlogModel.objects.all()
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

#See blog View

def see_blog(request):
    context = {}
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] = blog_objs
    except Exception as e: print(e)
    return render(request, 'see_blog.html', context)

#Login View
def login_view(request):
    return render(request, 'login.html')

# Add Blog View
def add_blog(request):
    context = {'form' : BlogForm}

    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            title = request.POST.get('title')
            image = request.FILES['imageBlog']
            user = request.user

            # check form validation
            if form.is_valid():
                content = form.cleaned_data['content']
            blog_obj = BlogModel.objects.create(title = title, image=image, user=user, content = content)
            return HttpResponse(f'Your Blog with name {title} was created Successfuly <br> <a href="/">Go Back to Home page</a>')

    except Exception as e:
        print(e)
    
    return render(request, 'add_blog.html', context)

def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id = id)

        if blog_obj.user == request.user:
            blog_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/your-blogs/')

def blog_update(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(slug = slug)
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial = initial_dict)

        if request.method == 'POST':
            form = BlogForm(request.POST)
            title = request.POST.get('title')
            image = request.FILES['imageBlog']
            user = request.user

            if image == '' :
                return HttpResponse("Please Fill all the details!")

            # check form validation
            if form.is_valid():
                content = form.cleaned_data['content']
            blog_obj.title = title
            blog_obj.image = image
            blog_obj.content = content
            blog_obj.save()
            return HttpResponse('Your changes were saved successfully! <a href="/your-blogs/">Contine!</a>')

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'update_blog.html', context)


#Register View
def register_view(request):
    return render(request, 'register.html')

def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()

        if profile_obj:
            profile_obj.is_verifified = True
            profile_obj.save()
            return HttpResponse("Your Account has been Successfully Verified. <a href='/login'>Login to Continue</a>")

        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')

def account_info(request):
    user = request.user
    context = {'user' : user}
    return render(request, 'account-info.html', context)