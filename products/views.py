from django.shortcuts import get_object_or_404, render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def articles(request):
    articles = Article.objects.all().order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "products/articles.html", context)


#@login_required
def create(request):
    if request.method == "POST":
        form=ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("products:article_detail", article.pk)
    else:
        form =ArticleForm()
                
    context = {"form":form}
    return render(request, "products/create.html", context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all().order_by("-pk")
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
        }
    return render(request, "products/article_detail.html", context)


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("products:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "products/update.html", context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect("products:articles")


@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect("products:article_detail", article.pk)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article =  get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('products:article_detail', article.pk)
    return redirect('accounts:login')

#python manage.py runserver