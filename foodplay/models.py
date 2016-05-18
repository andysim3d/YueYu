from django.db import models


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    blog_title = models.TextField(max_length=256)
    blog_content = models.TextField(max_length=65535)


class Items(models.Model):
    name = models.CharField(max_length=255)
    sku = models.AutoField(primary_key=True)
    price = models.FloatField()
    currency = "USD"
    quantity = 1
    description = models.TextField()


class Payhistory(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=16, choices=(('visa', 'visa'),
                                                    ('American Express', "amex"),
                                                    ('discover', 'discover'),
                                                    ('Master', 'master'),))
    number = models.CharField(max_length=32)
    expire_month = models.IntegerField()
    expire_year = models.IntegerField()
    cvv2 = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    item = models.ForeignKey(Items)
