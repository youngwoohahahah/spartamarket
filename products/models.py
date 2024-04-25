from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        #"accounts.User"이라고 써도 동작하지만... 
        on_delete=models.CASCADE, 
        related_name="articles")
        #user.article_set.all() 대신 user.articles.all() 쓸 수 있음

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


#python manage.py makemigrations
#python manage.py migrate