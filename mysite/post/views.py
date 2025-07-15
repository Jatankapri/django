from django.shortcuts import render
def post_home(request):
    """
    Render the home page for the post app.
    """
    return render(request, 'post/post_home.html')
# Create your views here.
