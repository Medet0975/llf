import io

from rest_framework.parsers import JSONParser
from rest_framework import serializers
from announcements.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        # fields = '__all__'
        exclude = ("author", )

#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie", "content" = "Actores"} ')
#     data = JSONParser().parse(stream)
#     serializer = AnnouncementSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)