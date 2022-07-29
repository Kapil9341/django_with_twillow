from django import forms
from .models import Student
from .models import User

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name':'Enter Name','email':'Enter Email','password':'Enter pass'}
       
        error_messages = {'password':{'required':'Please Enter Your Password'},
                        'email':{'required':'Please Enter Your Email'}} 
        widgets = {
            'password':forms.PasswordInput,
            'email':forms.EmailInput,
            'name':forms.TextInput(attrs={'class':'myclass'})
        }