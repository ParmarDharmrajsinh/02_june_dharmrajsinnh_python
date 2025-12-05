from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Follow
from .models import Post, Comment, Follow
from .forms import CommentForm

User = get_user_model()

# ------------------------------
# Home / Feed
# ------------------------------
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
    }
    return render(request, "home.html", context)


# ------------------------------
# Post Creation
# ------------------------------
@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            user=request.user,
            title=title,
            content=content
        )
        return redirect('insta:home')

    return render(request, "create_post.html")


# ------------------------------
# Post Detail
# ------------------------------
def post_detail(request, id):
    post = Post.objects.get(id=id)
    liked = False
    if request.user.is_authenticated:
        liked = request.user in post.likes.all()
    context = {'post': post, 'liked': liked}
    return render(request, 'post_detail.html', context)

    # Likes
    user_liked = False
    if request.user.is_authenticated:
        user_liked = post.likes.filter(id=request.user.id).exists()

    context = {
        "post": post,
        "comments": comments,
        "comment_form": form,
        "is_following": is_following,
        "user_liked": user_liked,
        "like_count": post.likes.count(),
    }

    return render(request, "post_detail.html", context)


# ------------------------------
# Add Comment
# ------------------------------
@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=post,
                user=request.user,
                text=form.cleaned_data["text"]
            )
            messages.success(request, "Comment added!")
        else:
            messages.error(request, "Invalid comment.")

    return redirect("insta:post_detail", id=post.id)


# ------------------------------
# Delete Comment
# ------------------------------
@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if comment.user != request.user:
        return HttpResponseForbidden("You cannot delete this comment.")

    comment.delete()
    messages.success(request, "Comment deleted!")

    return redirect("insta:post_detail", id=comment.post.id)


# ------------------------------
# Like / Unlike Toggle
# ------------------------------

def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Example logic: toggle like for simplicity
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return redirect('insta:post_detail', id=id)


# ------------------------------
# Follow / Unfollow Toggle
# ------------------------------
@login_required
def follow_toggle(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user == user_to_follow:
        return redirect('insta:home')
    
    follow_obj = Follow.objects.filter(follower=request.user, following=user_to_follow)
    if follow_obj.exists():
        follow_obj.delete()
    else:
        Follow.objects.create(follower=request.user, following=user_to_follow)
    return redirect('insta:home')

# ------------------------------
# View Followers
# ------------------------------
def followers_list(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, id=user_id)

    followers = Follow.objects.filter(following=user)

    return render(request, "followers.html", {
        "user": user,
        "followers": followers,
    })


# ------------------------------
# View Following
# ------------------------------
def following_list(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, id=user_id)

    following = Follow.objects.filter(follower=user)

    return render(request, "following.html", {
        "user": user,
        "following": following,
    })


# ------------------------------
# User Authentication
# ------------------------------
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("insta:home")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("insta:login")


def register(request):
    User = get_user_model()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created! Please login.")
            return redirect("insta:login")
    return render(request, "register.html")
