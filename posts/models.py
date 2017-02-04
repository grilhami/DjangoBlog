from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from core.models import TimestampedModel



class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
    return "{}/{}".format(instance.id, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1) #blank=True, null=True
    title = models.CharField(max_length=120)
    slg = models.SlugField(unique=True)
#   image = models.FileField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True,
            width_field="width_field",
            height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __uncicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return "/posts/%s/" % (self.id)
        return reverse("posts:detail", kwargs={"slg":self.slg})

    def get_id_url(self):
        return reverse("posts:detail", kwargs={"id":self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]

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

# class Comment(models.Model):

#     user = models.ForeignKey(User, on_delete="CASCADE")
#     contents = models.TextField(max_length=200)

#     def __str__(self):
#         return self.content

#     def __unicode__(self):
#         return self.content
