from django.forms import ModelForm

from foodplay.models import CardInformations


class PaypalForm(ModelForm):
    class Meta:
        model = CardInformations
        fields = ['id', 'type', 'number',
                  'expire_month', 'expire_year',
                  'cvv2', 'first_name', 'last_name']


'''
id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    type=models.CharField(max_length=16)
    number=models.CharField(max_length=32)
    expire_month=models.IntegerField()
    expire_year = models.IntegerField()
    cvv2 = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    '''
