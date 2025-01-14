from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import UserProfile
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                user_type=form.cleaned_data.get('user_type'),
                profile_picture=form.cleaned_data.get('profile_picture'),
                address_line1=form.cleaned_data.get('address_line1'),
                city=form.cleaned_data.get('city'),
                state=form.cleaned_data.get('state'),
                pincode=form.cleaned_data.get('pincode')
            )
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    user_profile = request.user.userprofile
    context = {
        'user_profile': user_profile
    }
    return render(request, 'users/dashboard.html', context)