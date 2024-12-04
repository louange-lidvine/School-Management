from django import forms
from .models import Facility, Booking

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'description', 'capacity']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time:
            if start_time >= end_time:
                raise forms.ValidationError("End time should be after start time.")

        return cleaned_data