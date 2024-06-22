from rest_framework import serializers
from .models import ReviewModel

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['review_id','book_id', 'user_name', 'rating', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        if data['rating'] < 1 or data['rating'] > 10:
            raise serializers.ValidationError("Rating must be between 1 and 10")
        return data
