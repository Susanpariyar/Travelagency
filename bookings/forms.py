from django import forms
from .models import Booking
from datetime import date


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            'travel_date',
            'travelers',
            'contact_phone',
            'emergency_contact',
            'special_requests',
        ]

        widgets = {

            'travel_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),

            'travelers': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                }
            ),

            'contact_phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter contact number'
                }
            ),

            'emergency_contact': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Emergency contact (optional)'
                }
            ),

            'special_requests': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Any special requests...'
                }
            ),
        }

    def clean_travel_date(self):

        travel_date = self.cleaned_data["travel_date"]

        if travel_date < date.today():

            raise forms.ValidationError(
                "Travel date cannot be in the past."
            )

        return travel_date
