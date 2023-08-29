from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    # 유저모델 참조하는 3가지 방법
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

