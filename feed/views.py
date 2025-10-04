from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post, Comment, Like, Share
from accounts.models import User

@login_required
def feed_view(request):
    posts = Post.objects.filter(tenant=request.user.tenant).select_related('user').prefetch_related('likes', 'comments', 'shares')
    
    for post in posts:
        post.user_has_liked = post.likes.filter(user=request.user).exists()
    
    context = {
        'posts': posts,
        'user': request.user,
    }
    return render(request, 'feed/feed.html', context)

@login_required
@require_POST
def create_post(request):
    conteudo = request.POST.get('conteudo', '').strip()
    arquivo = request.FILES.get('imagem')
    
    imagem = None
    video = None
    
    if arquivo:
        content_type = arquivo.content_type
        if content_type.startswith('video/'):
            video = arquivo
        elif content_type.startswith('image/'):
            imagem = arquivo
    
    if conteudo or imagem or video:
        Post.objects.create(
            tenant=request.user.tenant,
            user=request.user,
            conteudo=conteudo,
            imagem=imagem,
            video=video
        )
    
    return redirect('feed:feed')

@login_required
@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id, tenant=request.user.tenant)
    
    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user,
        tenant=request.user.tenant
    )
    
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'total_likes': post.total_likes()
    })

@login_required
@require_POST
def comment_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id, tenant=request.user.tenant)
    conteudo = request.POST.get('conteudo', '').strip()
    
    if conteudo:
        comment = Comment.objects.create(
            tenant=request.user.tenant,
            post=post,
            user=request.user,
            conteudo=conteudo
        )
        
        return JsonResponse({
            'success': True,
            'comment': {
                'user': comment.user.username,
                'conteudo': comment.conteudo,
                'criado_em': comment.criado_em.strftime('%d/%m/%Y %H:%M')
            },
            'total_comments': post.total_comments()
        })
    
    return JsonResponse({'success': False}, status=400)

@login_required
@require_POST
def share_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id, tenant=request.user.tenant)
    
    Share.objects.create(
        post=post,
        user=request.user,
        tenant=request.user.tenant
    )
    
    return JsonResponse({
        'success': True,
        'total_shares': post.total_shares()
    })
