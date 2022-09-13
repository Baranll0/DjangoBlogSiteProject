from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Kullanıcı")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Tarih")
    post_image=models.FileField(blank=True,null=True,verbose_name="Posta fotoğraf ekleyin")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete = models.CASCADE,verbose_name="Post",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="İsim")
    comment_content=models.CharField(max_length=250,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering=['-comment_date']