from django.forms import ModelForm

from foodplay.models import payhistory


class PaypalForm(ModelForm):
    class Meta:
        model = payhistory
        fields = []
