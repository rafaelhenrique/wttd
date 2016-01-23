from eventex.subscriptions.models import Subscription

from django import forms
from django.core.exceptions import ValidationError


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = []
        for w in name.split():
            if len(w) > 2:
                words.append(w.capitalize())
            else:
                words.append(w)
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()

        if ((not self.cleaned_data.get('email') and
             not self.cleaned_data.get('phone'))):
            raise ValidationError('Informe seu e-mail ou telefone.')
        return self.cleaned_data
