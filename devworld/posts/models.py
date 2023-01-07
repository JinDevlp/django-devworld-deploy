from django.db import models
from users.models import Profile
# Create your models here.

CATEGORY = [
    ('General','GENERAL'),
    ('Discussion','DISCUSSION'),
    ('Question','QUESTION'),
    ('Jobs','JOBS'),
    ('Projects','PROJECTS'),
]

class Post(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True )
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, upload_to='posts/', default="post_default.jpg")
    category = models.CharField(
        max_length=10,
        choices=CATEGORY,
        default=None,
    )
    total_vote = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    demo_link = models.CharField(max_length=300, null=True, blank=True)
    source_link = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def raters(self):
        queryset = self.rating_set.all().values_list('owner__id',flat=True)
        return queryset

    @property
    def getVoteCount(self):
        ratings = self.rating_set.all()
        upVotes = ratings.filter(vote='up').count()
        totalVotes = ratings.count()

        try:
            ratio = int((upVotes / totalVotes)) * 100
            self.total_vote = totalVotes
            self.vote_ratio = ratio
            self.save()
        except ZeroDivisionError:
            self.save()


class Comment(models.Model):
    commenter = models.ForeignKey(Profile,null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created']


class Rating(models.Model):
    VALUES= (
        ('up','UP'),
        ('down','DOWN'),
    )
    owner = models.ForeignKey(Profile,null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote = models.CharField(max_length=100, choices=VALUES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner','post']



    def __str__(self):
        return self.vote

