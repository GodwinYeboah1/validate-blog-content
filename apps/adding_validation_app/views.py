from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import Blog


def  home(request):
    print('Welcome to the home page ')
    #grab all the blogs
    list_blog = Blog.objects.all()
    # set it to req . context
    context = {}
    context['blog_list'] = list_blog
    #pass it to the render function so the template file can use the data
    return render(request, 'index.html',context)

def create_blog(request):
    new_blog = Blog.objects.blog_creater(request.POST)
    print("Create Blog helper:" , new_blog )
    return redirect('/')

def  update_page(request, id):
    print("Just landed on the update page")
    context = {
        'spec_blog': Blog.objects.get(pk=id)
    }

    print("Update page helper:" , context )

    return render(request,'update_page.html', context)

def  update(request, id):
    if request.method == 'POST':
        print("upated helper: " , request.POST)
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = Blog.objects.basic_validator(request.POST)
            # check if the errors object has anything in it

        if len(errors):
            # if the errors object contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/blog/edit/'+id)
        else:
            # if the errors object is empty, that means there were no errors!
            # retrieve the blog to be updated, make the changes, and save
            blog = Blog.objects.get(id = id)
            blog.name = request.POST['name']
            blog.desc = request.POST['desc']
            blog.save()
            messages.success(request, "Blog successfully updated")
            # redirect to a success route
            return redirect('/blogs')

def destory(request, id):
    del_blog = Blog.objects.get(pk=id)
    del_blog.delete()
    return redirect('/')
    