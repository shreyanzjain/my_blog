from django import forms
from .models import Comments

class EditComment(forms.ModelForm):
    model = Comments
    content = forms.Textarea()

    class Meta:
        model = Comments
        fields = ['content']