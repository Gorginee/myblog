from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from user.forms import RegisterForm


# is registered
from user.models import User


def is_registered(request):
    if request.is_ajax():
        if User.objects.filter(username=request.POST.get('username')).first():
            return JsonResponse({'code': 1, 'msg': '用户名已存在！'})
        return JsonResponse({'code': 0, 'msg': 'unregistered'})


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        encoded_pwd = make_password(password)
        User.objects.create(username=username, password=encoded_pwd).save()
    else:
        print(form.errors)
        return render(request, 'index.html', {'form_errors': form.errors})
    return JsonResponse({'code': 0, 'msg': 'success'})
