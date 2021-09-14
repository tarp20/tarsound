from django.shortcuts import render


def google_login(request):
    '''
    enter via google
    '''
    return render(request, 'oauth/google_login.html')