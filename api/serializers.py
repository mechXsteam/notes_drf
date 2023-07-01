from rest_framework.serializers import ModelSerializer

from .models import Note


class NotesSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        # we are specifying all fields here, actuall we don't have many fields to validate, so
        # I am passing down all the fields here. We obviously can specify fields explicitly using
        # an array ['title,'body'...]
