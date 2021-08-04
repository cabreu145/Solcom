from django.forms import ModelForm, DateInput, Select
from calendarapp.models import Event, EventMember
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time','color']
        # datetime-local is a HTML5 input type
        array_choices= [
        ('#FF0000', 'Rojo'),
        ('#0000FF', 'Azul'),
        ('#FFFF00', 'Amarillo'),
        ('#800080', 'Morado'),
        ]



        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titulo del Evento'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del Evento'
            }),
            'start_time': DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'end_time': DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            

        }
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ['user']
