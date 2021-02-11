from django import forms

class IletisimForm(forms.Form):
    email = forms.EmailField(max_length=50)
    isim_soyisim = forms.CharField(max_length=25)
    mesaj = forms.CharField(widget=forms.Textarea)