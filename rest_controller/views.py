from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_controller.serializers import FileSerializer
from rest_controller.models import File


class CreateFileView (CreateAPIView):

    queryset = File.objects.all()
    serializer_class = FileSerializer


class RetrieveFileView (RetrieveAPIView):

    queryset = File.objects.all()
    serializer_class = FileSerializer


class RetrieveFilesView (ListAPIView):

    queryset = File.objects.all()
    serializer_class = FileSerializer
