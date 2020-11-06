from django.forms import ModelForm

from .models import Link, Article, Topic, Sim_rate, Source


class SimForm(ModelForm):
    class Meta:
        model = Sim_rate
        fields = ('similarity',)
        fields_required = False