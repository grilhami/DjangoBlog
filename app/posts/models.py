from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from app.core.models import TimestampedModel
from markdown_deux import markdown
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 



class PostManager(models.Manager):
    
    def active(self, *args, **kwargs):
        
        return super(
            PostManager, self).filter(
            draft=False).filter(
            publish__lte=timezone.now())


def upload_location(instance, filename):
    
    return "{}/{}".format(instance.id, filename)


class Post(TimestampedModel):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title = models.CharField(max_length=120)
    slg = models.SlugField(unique=True)
    # file = models.FileField(blank=True, null=True)
    image = models.ImageField(
            upload_to=upload_location,
            null=True, blank=True,
            width_field="width_field",
            height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    objects = PostManager()

    def __uncicode__(self):
    
        return self.title
	
    def __str__(self):
    
        return self.title

    def get_absolute_url(self):
        """
        You could get it both ways
        return "/posts/%s/" % (self.id)
        """
        return reverse("posts:detail", kwargs={"slg":self.slg})

    def get_likes(self):
    
        return self.likes.count()

    def get_id_url(self):
    
        return reverse("posts:detail", kwargs={"id":self.id})

    def get_markdown(self):
    
        content = self.content
        markdown_text = markdown(content)
        return markdown_text

    def like(self):
    
        pass


def create_slug(instance, new_slg=None):
    
    slg = slugify(instance.title)
    if new_slg is not None:
        slg = new_slg
    qs = Post.objects.filter(slg=slg).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slg = "%s-%s" % (slg, qs.first().id)
        return create_slug(instance, new_slg=new_slg)
    return slg


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    
    if not instance.slg:
        instance.slg = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)

"""
Another Models for comment and likes.
"""
class Comment(TimestampedModel):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    post = models.ForeignKey(Post)

    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField(max_length=200)

    def __str__(self):

        return self.user.username

    def __unicode__(self):
        
        return self.user.username
