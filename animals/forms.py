import sys
from django.forms import ModelForm

from animals.models import Animal


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        exclude = ['user']
        fields = ['name', 'breed', 'birth_date', 'microchip_id', 'about', 'private', ]

    def throw(self):
        print >>sys.stderr, 'Form Throw!!!!'
