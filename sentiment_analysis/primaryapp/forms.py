from django import forms

class NewSentimentForm(forms.Form):
    sentence = forms.CharField(help_text="Expresa tus sentimiento y dejame decirte que sentimiento es.", max_length=220)