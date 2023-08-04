from django.forms import ModelForm
from .models import store



class storeForm(ModelForm):
    class Meta:
        model = store
        fields='__all__'
