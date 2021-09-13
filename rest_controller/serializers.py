from rest_framework.serializers import ModelSerializer
from rest_controller.models import File


class FileSerializer (ModelSerializer):

    # file = SerializerMethodField('get_file')

    class Meta:
        
        model = File
        fields = ('id','file')
