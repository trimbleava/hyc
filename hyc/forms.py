from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Content:"


    def send_email(self):
        # send email using the self.cleaned_data dictionary
        # send_mail(
        #     self.cleaned_data['subject'],
        #     self.cleaned_data['message'],
        #     self.cleaned_data.get('email', 'noreply@mysite.com'),
        #     ['email@mysite.com']
        # )
        pass


    def clean(self):
        """This is where you should be checking for required
        fields and making sure the submitted data is safe."""
        pass