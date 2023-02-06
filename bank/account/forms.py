from django import forms  
from .models import User 
  
class UserForm(forms.ModelForm):  
    class Meta:  
        model = User  
        exclude = ('customer_id',)
        widgets = {
        'password': forms.PasswordInput(),
        }
        fields = "__all__"