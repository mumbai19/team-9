from django.shortcuts import render
# from django.shortcuts import render_to_response

def login(request):
    return render(request, 'authenticate/login.html')
    # return render_to_response('authenticate/login.html')

def register(request):
    return render(request, 'authenticate/registration.html')
