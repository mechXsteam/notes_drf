from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NotesSerializer

# Create your views here.

"""GET THE LIST OF ALL NOTES"""


@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all().order_by('-updated_at')
    serializer = NotesSerializer(notes, many=True)
    return Response(serializer.data)


# Let's get hold of the idea what we are doing here...
# We are creating a functional version of APIview (because it's more intutive to me, specially having a coding
# background in django) in which we are retreiving all the notes from the Note model and then serializing it using our
# custom NoteSerializer, the argument many=True indicates that there are more than one object to serialize. After that
# we are returning a JSON response. Why serializer.data and why not only serializer ? It is because serializer is an
# instance of the NotesSerializer class (makes sense when comfortable with OOPs concept) and it contains some extra
# information in addition to data, therefore to access it we use serializer.data.

""" GET THE SPECIFIC NOTE """


@api_view(['GET'])
def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    serialzer = NotesSerializer(note, many=False)
    return Response(serialzer.data)


""" CREATE A NOTE """


@api_view(['POST'])
def create_note(request):
    data = request.data
    # creating the note
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NotesSerializer(data=note, many=False)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


""" UPDATE A NOTE """


@api_view(['PUT'])
def update_note(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NotesSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


""" DELETE A NOTE """


@api_view(['DELETE'])
def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note deleted Successfuy!!!")
