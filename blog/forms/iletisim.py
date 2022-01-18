from django import forms
from blog.models import IletisimModel
from django.core.mail import send_mail

class IletisimForm(forms.ModelForm):
    class Meta:
        model =IletisimModel
        fields = ('email', 'isim_soyisim', 'mesaj')


    def send_email(self, mesaj):
        send_mail(
            subject='İletişim Formundan Yeni Mesaj Var!',
            message=mesaj,
            from_email=None,
            recipient_list=['haluk.hckl@gmail.com'],
            fail_silently=False
        )

