from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm
from . import models


class SignupForm(ModelForm):
    password = forms.CharField(max_length=20, label='', widget=forms.PasswordInput(attrs={
        'class': 'account-form form-control-lg w-100 mb-3',
        'placeholder': '비밀번호'
    }))
    confirm_password = forms.CharField(max_length=20, label='', widget=forms.PasswordInput(attrs={
        'class': 'account-form form-control-lg w-100 mb-3',
        'placeholder': '비밀번호 확인'
    }))
    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'account-form form-control-lg w-100 mb-3',
                'placeholder': '이메일 주소'
            })
        }
        labels = {
            'email': ''
        }

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return password1

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'account-form form-control-lg w-100 mb-3',
        'placeholder': '이메일 주소'
    }))
    password = forms.CharField(max_length=20, label='', widget=forms.PasswordInput(attrs={
        'class': 'account-form form-control-lg w-100 mb-3',
        'placeholder': '비밀번호'
    }))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error('password', forms.ValidationError('비밀번호가 틀렸습니다.'))
        except User.DoesNotExist:
            self.add_error("email", forms.ValidationError('계정이 존재하지 않습니다.'))