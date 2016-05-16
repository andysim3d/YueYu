from django.db import models

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    blog_title = models.TextField(max_length=256)
    blog_content = models.TextField(max_length=65535)


class payhistory(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
