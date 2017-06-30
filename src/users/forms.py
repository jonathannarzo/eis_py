from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, Select
from django.contrib.auth.models import User
from .models import Profile, Role, Position, Department

class AppLogin(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'password': PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }
    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

class ProfileForm(forms.ModelForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(), empty_label="(-Select Role-)", widget=Select(attrs={'class':'form-control'}))
    position = forms.ModelChoiceField(queryset=Position.objects.all(), empty_label="(-Select Position-)", widget=Select(attrs={'class':'form-control'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="(-Select Department-)", widget=Select(attrs={'class':'form-control'}))
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    civil_status_choices = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
    )
    gender = forms.ChoiceField(choices=gender_choices, widget=Select(attrs={'class':'form-control'}))
    civil_status = forms.ChoiceField(choices=civil_status_choices, widget=Select(attrs={'class':'form-control'}))
    class Meta:
        model = Profile
        exclude = ['user','created_at','updated_at']
        widgets = {
            'first_name': TextInput(attrs={'placeholder':'First name','class':'form-control'}),
            'middle_name': TextInput(attrs={'placeholder':'Middle name','class':'form-control'}),
            'last_name': TextInput(attrs={'placeholder':'Last name','class':'form-control'}),
            'birthdate': TextInput(attrs={'placeholder':'Birthdate','class':'form-control'}),
            'tel_no': TextInput(attrs={'placeholder':'Telephone Number','class':'form-control'}),
            'mobile_no': TextInput(attrs={'placeholder':'Mobile Number','class':'form-control'}),
            'address': TextInput(attrs={'placeholder':'Address','class':'form-control'}),
            'religion': TextInput(attrs={'placeholder':'Religion','class':'form-control'}),
            'nationality': TextInput(attrs={'placeholder':'Nationality','class':'form-control'}),
            'bank_name': TextInput(attrs={'placeholder':'Bank Name','class':'form-control'}),
            'bank_no': TextInput(attrs={'placeholder':'Bank Acct No.','class':'form-control'}),
            'basic_salary': TextInput(attrs={'placeholder':'Basic Salary','class':'form-control'}),
            'monthly_allowance': TextInput(attrs={'placeholder':'Monthly Allowance','class':'form-control'}),
            'tin_no': TextInput(attrs={'placeholder':'TIN No.','class':'form-control'}),
            'sss_no': TextInput(attrs={'placeholder':'SSS No.','class':'form-control'}),
            'gsis_no': TextInput(attrs={'placeholder':'GSIS No.','class':'form-control'}),
            'pagibig_no': TextInput(attrs={'placeholder':'PagIbig No.','class':'form-control'}),
            'philhealth_no': TextInput(attrs={'placeholder':'PhilHealth No.','class':'form-control'}),
            'entry_date': TextInput(attrs={'placeholder':'Entry date','class':'form-control'}),
            'end_date': TextInput(attrs={'placeholder':'End date','class':'form-control'}),
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        exclude = ['created_at','updated_at']
        widgets = {
            'code': TextInput(attrs={'placeholder':'Code','class':'form-control'}),
            'description': TextInput(attrs={'placeholder':'Description','class':'form-control'}),
        }
