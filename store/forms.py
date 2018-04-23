from django.forms import ModelForm
from store.models import Item, Fan


class ItemUpdateForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'seller', 'total_amount', 'amount_paid', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['seller'].required = False
        self.fields['total_amount'].required = False
        self.fields['amount_paid'].required = False
        self.fields['quantity'].required = False
