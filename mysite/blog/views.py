from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        return render(request, 'blog/login_content.html')
    return render(request, 'blog/login.html')