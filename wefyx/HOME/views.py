from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.db.models import Q
from django.db.models import F
from accounts.models import CustomUser


# -------- HOME PAGE VIEW --------
def home_page(request):
    posts = Post.objects.select_related('post_category', 'author').order_by('-created_at')
    categories = Category.objects.all().order_by('cat_name')
    return render(request, 'home.html', {
        'user_post': posts,
        'categories': categories,
        'current_category': None  # No category selected
    })

# -------- User profile PAGE VIEW --------
def profile_detail(request, username):
    user = get_object_or_404(CustomUser, username=username)
    user_posts = user.posts.all()
    return render(request, 'accounts/author_detail.html', {
        'profile_user': user,
        'user_posts': user_posts
    })


# -------- POST DETAIL VIEW --------
def post_detail(request, slug):
    post = get_object_or_404(Post, post_slug=slug)
    
    # Increment read count Session-based tracking
    session_key = f'viewed_post_{post.pk}'
    if not request.session.get(session_key, False):
        Post.objects.filter(pk=post.pk).update(read_count=F('read_count') + 1)
        request.session[session_key] = True
        post.refresh_from_db()

    return render(request, 'pages/post_detail.html', {'post': post})


# -------- CATEGORY FILTER VIEW --------
def posts_by_category(request, slug):
    post_category = get_object_or_404(Category, cat_slug=slug)
    posts = Post.objects.filter(post_category=post_category) \
        .select_related('post_category') \
        .order_by('-created_at')
    categories = Category.objects.all().order_by('cat_name')
    return render(request, 'home.html', {
        'user_post': posts,
        'categories': categories,
        'current_category': post_category
    })

# -------- SEARCH RESULTS VIEW --------
def search_results(request):
    query = request.GET.get('search_query')
    posts = Post.objects.select_related('post_category', 'author').order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(post_title__icontains=query) |
            Q(description__icontains=query) |
            Q(author__username__icontains=query) |
            Q(post_category__cat_name__icontains=query)
        )

    categories = Category.objects.all().order_by('cat_name')
    return render(request, 'home.html', {
        'user_post': posts,
        'categories': categories,
        'current_category': None,
        'search_query': query
    })


def explore_view(request):
    return render(request, 'pages/explore.html')  

def bookstore_view(request):
    return render(request, 'pages/bookstore.html')

def guides_view(request):
    return render(request, 'pages/guides.html')