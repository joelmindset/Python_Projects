from django.forms import ModelForm
from .models import Account, Transaction


# Account form all fields

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# transaction form all fields

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
