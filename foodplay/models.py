from django.db import models

class Blog(models.Model):
    blog_title = models.AutoField(primary_key=True)
    blog_content = models.TextField(max_length=65535)
