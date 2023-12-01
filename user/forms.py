from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets

class UyeGiris(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields["username"].widget.attrs['class']= "register-input"
        self.fields["password"].widget=widgets.PasswordInput(attrs={'class':'register-input'}) 

