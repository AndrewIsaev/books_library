from django import forms

from .models import Comments


class CommentsForm(forms.ModelForm):
    """
    A Django ModelForm for creating or updating comment records.

    This form is used to create or update comments associated with a specific
    model, typically for use in a web application. It is based on the 'Comments'
    model and includes a single field 'text' for entering the comment text.
    """

    class Meta:
        model = Comments
        fields = ["text"]
