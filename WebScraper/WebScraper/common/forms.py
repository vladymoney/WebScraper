from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label="Enter the URL to scrape", max_length=200)