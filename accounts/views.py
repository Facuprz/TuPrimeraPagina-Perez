# accounts/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignupForm, UserUpdateForm, ProfileForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu cuenta fue creada. Ya podés iniciar sesión.")
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileForm(instance=request.user.profile)
        return render(request, 'accounts/profile_edit.html', {'uform': uform, 'pform': pform})

    def post(self, request):
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('profile')
        messages.error(request, "Revisá los datos del formulario.")
        return render(request, 'accounts/profile_edit.html', {'uform': uform, 'pform': pform})