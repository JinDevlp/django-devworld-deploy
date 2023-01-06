from rest_framework import serializers
from posts.models import Post, Comment, Rating
from users.models import Profile, Message, Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    technology = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'

    def get_technology(self,obj):
        tech = obj.technology_set.all()
        serializer = TechnologySerializer(tech,many=True)
        return serializer.data

class MessageSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer(many=False)
    recipient = ProfileSerializer(many=False)

    class Meta:
        model = Message
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    """Nested Serializer"""
    owner = ProfileSerializer(many=False) # bc only ONE Profile to ONE Post
    ratings = serializers.SerializerMethodField()

    comment = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_ratings(self,obj):
        ratings = obj.rating_set.all()
        serializer = RatingSerializer(ratings,many=True)
        return serializer.data

    def get_comment(self,obj):
        comments = obj.comment_set.all()
        serializer = CommentSerializer(comments,many=True)
        return serializer.data

