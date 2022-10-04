from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Name :','email':'Enter Email :' , 'password':'Enter Password'}
        error_messages = {'name':{'required':'Enter Your Full Name'},'email':{'required':'Enter Email'}, 'password':{'required':'Enter Password'}}
        widgets = {'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Your Name Here'}),'email':forms.EmailInput(attrs={'placeholder':'Your@gmail.com'}),
        'password':forms.PasswordInput(attrs={'placeholder':'Enter Password'})
        }