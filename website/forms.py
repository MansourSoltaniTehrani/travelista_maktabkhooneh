from django import forms
from website.models import Contact


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=255)
#     message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    # author = forms.CharField(max_length=255)
    class Meta:
        model = Contact
        # fields = '__all__'
        exclude = ('published_date', )