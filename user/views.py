from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q, Count


# Authentication Views
def login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('user:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # Try to authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # Set session expiry
            if not remember:
                request.session.set_expiry(0)  # Session expires on browser close

            messages.success(request, f'Welcome back, {user.username}!')

            # Redirect to next page or dashboard
            next_url = request.GET.get('next', 'user:dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'user/login.html')


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('core:home')


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('user:dashboard')

    return render(request, 'user/register.html')


# User Profile Views
def dashboard(request):
    """User dashboard view"""
    return render(request, 'user/dashboard.html')


def profile(request, username):
    """Public profile view"""
    try:
        user = User.objects.get(username=username)
        context = {'profile_user': user}
        return render(request, 'user/profile.html', context)
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('user:index')


def editprofile(request):
    """Edit profile view"""
    return render(request, 'user/editprofile.html')


def settings(request):
    """User settings view"""
    return render(request, 'user/settings.html')


# User Directory
def index(request):
    """User directory - browse community members"""
    search_query = request.GET.get('search', '')
    filter_by = request.GET.get('filter', 'recent')

    users = User.objects.select_related('profile').annotate(
        skill_count=Count('skill', distinct=True),
        exchange_count=Count('exchange_user1', distinct=True) + Count('exchange_user2', distinct=True)
    )

    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(profile__bio__icontains=search_query)
        )

    if filter_by == 'active':
        users = users.order_by('-exchange_count', '-skill_count')
    elif filter_by == 'alphabetical':
        users = users.order_by('username')
    else:
        users = users.order_by('-date_joined')

    context = {
        'users': users,
        'search_query': search_query,
        'filter_by': filter_by,
        'total_users': User.objects.count(),
        'active_users': User.objects.filter(is_active=True).count(),
    }
    return render(request, 'user/index.html', context)