from rest_framework import serializers
from .models import BookModel

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['book_id','title', 'author', 'publisher', 'summary', 'price', 'published_date']