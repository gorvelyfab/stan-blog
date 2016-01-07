from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Your name', max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }
        ))
    email = forms.EmailField(label='Enter email', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your email address'
        }
    ))
    subject = forms.CharField(
        label='Subject', max_length=255, widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'subject'
            }
        ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your text here'
        }
    ))
