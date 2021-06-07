from django import forms


class newPageForm(forms.Form):
    name = forms.CharField(label="Page Name:")
    content = forms.CharField(label="Content:", widget=forms.Textarea)
