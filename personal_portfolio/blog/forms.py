from django import forms


class CommentForm(forms.Form):
    auther = forms.CharField(
        max_length=60, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'yourname'
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'placeholder': 'leave a Comment'
        })
    )
