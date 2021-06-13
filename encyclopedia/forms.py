from django import forms


class newPageForm(forms.Form):
    name = forms.CharField(
        label="Page Name:", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    content = forms.CharField(
        label="Content:", widget=forms.Textarea(attrs={"class": "form-control"})
    )
