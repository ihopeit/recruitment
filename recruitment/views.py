from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from captcha.fields import CaptchaField # 导入模块
from django.shortcuts import render

from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

import logging

logger = logging.getLogger(__name__)

class CaptchaLoginForm(AuthenticationForm):
    # username = forms.CharField(label='用户名')
    # password = forms.CharField(widget=forms.PasswordInput, label='密码')
    captcha = CaptchaField(label='验证码')

def login_with_captcha(request):
    if request.POST:
        form = CaptchaLoginForm(data=request.POST)
        #form = AuthenticationForm(data=request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            logger.info(" ===== validate ok %s" % (form.cleaned_data["username"]) )
            # authenticate user with credentials
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                # attach the authenticated user to the current session
               login(request,user)
               return HttpResponseRedirect(reverse_lazy('admin:index'))
        else:
            logger.warning(" ----- not valid")
            messages.add_message(request, messages.INFO, 'Not a valid request')
    else:
        form = CaptchaLoginForm(request.POST)
        #form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})