from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView

from . import forms
from accountapp.forms import SignupForm


class SignupView(FormView):
    form_class = SignupForm
    template_name = 'accountapp/signup.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'accountapp/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


# is_valid 문제 생김: id에서 User with this already exists. 발생
# def LoginView(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         id = request.POST['id']
#         password = request.POST['password']
#         user = authenticate(request, username=id, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('signup')
#         else:
#             return HttpResponse('로그인 실패.')
#         if form.is_valid():
#             user = form.save(commit=False)
#             id = user.id
#             password = user.password
#             is_user = authenticate(request, username=id, password=password)
#             if is_user is not None:
#                 login(request, is_user)
#                 return redirect('signup')  # 이름 확인
#             else:
#                 return HttpResponse('로그인 실패.')
#         else:
#             return render(request, 'accountapp/test.html', {'form': form})
#     else:
#         form = LoginForm()
#         return render(request, 'accountapp/login.html', {'form': form})
