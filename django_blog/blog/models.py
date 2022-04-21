from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               blank=True, null=True,
                               related_name='children')

    class Meta:
        verbose_name = "Комментария"
        verbose_name_plural = "Комментарии"
