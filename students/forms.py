from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'email', 'course', 'age']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter full name'
                }
            ),
            'roll_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter roll number'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email address'
                }
            ),
            'course': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter course name'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter age'
                }
            ),
        }
