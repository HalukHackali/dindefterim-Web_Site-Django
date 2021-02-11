from django import forms

class IletisimForm(forms.Form):
    email = forms.EmailField(label='E-posta', max_length=50)
    isim_soyisim = forms.CharField(label='İsim Soyisim',max_length=25)
    mesaj = forms.CharField(label='Mesajınız',widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))