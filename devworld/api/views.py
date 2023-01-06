from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer, ProfileSerializer, MessageSerializer
from posts.models import Post, Comment, Rating
from users.models import Profile, Message

@api_view(['GET', 'POST'])
def getRoutes(request):

    routes=[
        {'GET':'/api/posts'},
        {'GET':'/api/posts/id'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True) # serializer.data == Json data
    return Response(serializer.data)

@api_view(['GET'])
def getPost(request,pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post,many=False) # serializer.data == Json data
    return Response(serializer.data)

@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMessage(request,pk):
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(message, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postRating(request,pk):
    post = Post.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    rating, created = Rating.objects.get_or_create(
        owner=user,
        post=post,
    )

    rating.value = data['value']
    rating.save()
    post.getVoteCount

    serializer = PostSerializer(post,many=False)
    return Response(serializer.data)