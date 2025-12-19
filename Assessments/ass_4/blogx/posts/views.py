from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Post, Like, Comment
import json
from django.db.models import Count

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        user = User.objects.get(id=data['user_id'])

        post = Post.objects.create(
            author=user,
            title=data['title'],
            content=data['content']
        )

        return JsonResponse({
            "message": "Post created",
            "post_id": post.id
        })

    return JsonResponse({"error": "POST method required"}, status=400)


@csrf_exempt
def like_post(request, post_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=data['user_id'])
        post = Post.objects.get(id=post_id)

        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            return JsonResponse({"message": "Already liked"})

        return JsonResponse({"message": "Post liked"})

    return JsonResponse({"error": "POST method required"}, status=400)


@csrf_exempt
def add_comment(request, post_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=data['user_id'])
        post = Post.objects.get(id=post_id)

        Comment.objects.create(
            user=user,
            post=post,
            text=data['text']
        )

        return JsonResponse({"message": "Comment added"})

    return JsonResponse({"error": "POST method required"}, status=400)

def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.annotate(
            like_count=Count('likes'),
            comment_count=Count('comments')
        )

        data = []
        for post in posts:
            data.append({
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author.username,
                "likes": post.like_count,
                "comments": post.comment_count,
                "created_at": post.created_at
            })

        return JsonResponse(data, safe=False)
    
def post_detail(request, post_id):
    try:
        post = Post.objects.annotate(
            like_count=Count('likes'),
            comment_count=Count('comments')
        ).get(id=post_id)

        comments = post.comments.all()

        comments_data = []
        for comment in comments:
            comments_data.append({
                "user": comment.user.username,
                "text": comment.text,
                "created_at": comment.created_at
            })

        return JsonResponse({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "author": post.author.username,
            "likes": post.like_count,
            "comments_count": post.comment_count,
            "comments": comments_data,
            "created_at": post.created_at
        })

    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found"}, status=404)