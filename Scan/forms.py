from django import forms

class WebURLForm(forms.Form):
    website_name = forms.URLField(help_text='Enter the website URL which is to be scanned')