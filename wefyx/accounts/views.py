# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CustomUser  # Use your model

from django.contrib.auth.decorators import login_required
from .forms import PostForm  # Make sure you have this form
from HOME.models import Post  # ✅
from .forms import CustomUserUpdateForm
from django.http import JsonResponse, HttpResponseBadRequest



def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            login(request, user)
            # messages.success(request, "Account created successfully.")
            return redirect('profile', username=request.user.username)

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


@login_required
def post_upload_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # ✅ Set author here
            form.save()
            messages.success(request, "Post uploaded successfully!")
            return redirect('postUpload')  # Replace with your desired URL name
    else:
        form = PostForm()

    return render(request, 'accounts/post_upload.html', {'form': form})


@login_required
def user_profile_view(request):
    profile_user = request.user  # logged-in user
    user_posts = Post.objects.filter(author=profile_user).order_by('-created_at')

    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
        'user_posts': user_posts
    })


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = CustomUserUpdateForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})

    

@login_required
def follow_toggle_view(request):
    if request.method == 'POST':
        target_username = request.POST.get('username')
        target_user = get_object_or_404(CustomUser, username=target_username)

        if request.user == target_user:
            return HttpResponseBadRequest("You can't follow yourself.")

        if request.user in target_user.followers.all():
            target_user.followers.remove(request.user)
            is_following = False
        else:
            target_user.followers.add(request.user)
            is_following = True

        return JsonResponse({
            'success': True,
            'is_following': is_following,
            'follower_count': target_user.followers.count(),
        })

    return HttpResponseBadRequest("Only POST allowed.")



@login_required
def logout_view(request):
    logout(request)
    # messages.success(request, "Logged out successfully.")
    return redirect('login')



@login_required
def settings_view(request):
    return render(request, 'accounts/settings.html')


@login_required
def help_view(request):
    return render(request, 'accounts/help.html')

@login_required
def edit_view(request):
    return render(request, 'accounts/profile_edit.html')
