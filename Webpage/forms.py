from django import forms
from . import models


class FavoriteForm(forms.ModelForm):

    class Meta:
        model = models.Favorite
        exclude = (
            'content_type', 'object_id', 'content_object', 'count')