from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Article(models.Model):

    title = models.CharField( max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author =models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    class Meta:
        verbose_name = ("article")
        verbose_name_plural = ("articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})



class Comment(models.Model):

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        )      
    comment = models.CharField( max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )
    

    class Meta:
        verbose_name = ("comment")
        verbose_name_plural = ("comments")

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})
