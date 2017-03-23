from django.utils import timezone
try:
    from urllib import quote_plus
except:
    pass
try:
    from urllib.parse import quote_plus
except:
    pass

# used for Comment Model
from django.contrib.contenttypes.models import ContentType
# for after success notification
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
#paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# views
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
#model
from .models import Post, Comment
from .forms import PostForm, CommentForm
from braces.views import LoginRequiredMixin


class SearchMixin(object):

    def get_queryset(self):
        queryset = super(SearchMixins, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q)|
                Q(content__icontains=q)|
                Q(user__first_name__icontains=q)|
                Q(user__last_nae__icontains=q)
                ).distinct()
        return queryset

class PostListView(SearchMixin, ListView):

    model = Post
    paginate_by = 3
    title = "List"

    def get_queryset(self):
        queryset = Post.objects.active()
        return queryset

class PostDetailView(DetailView):

    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):

    model = Post


def post_list(request):
    # if request.user.is_authenticated():
    today = timezone.now().date()
    queryset_list = Post.objects.active()

    q = request.GET.get("q")
    if q:
        queryset_list = queryset_list.filter(
                Q(title__icontains=q)|
                Q(content__icontains=q)|
                Q(user__first_name__icontains=q)|
                Q(user__last_name__icontains=q)
                ).distinct()

    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
       queryset = paginator.page(paginator.num_pages)

    return render(request,"posts/post_list.html",{
        "object_list": queryset,
        "title": "List"
        })

@login_required
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        tits = form.cleaned_data.get("title")
        print (tits)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
        messages.success(request, "Successfully Created")
    return render(request, "posts/post_form.html",{
                "form":form,
    })

def post_detail(request, slg=None):
    instance = get_object_or_404(Post,slg=slg)
    share_string = quote_plus(instance.content)
    
    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    if request.user.is_authenticated():
        comment_form = CommentForm(request.POST or None, initial=initial_data)
        if comment_form.is_valid():
            c_type = comment_form.cleaned_data.get("content_type")
            content_type = ContentType.objects.get(model=c_type)
            obj_id = comment_form.cleaned_data.get('object_id')
            parent_obj = None
            try:
                parent_id = int(request.POST.get("parent_id"))
            except:
                parent_id = None
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exist() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()

            content_data = comment_form.cleaned_data.get("content")
            new_comment, created = Comment.objects.get_or_create(
                    user = request.user,
                    content_type = content_type,
                    object_id = obj_id,
                    content = content_data,
                    parent = parent_obj
            )
            return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    else:
        comment_form = "Login to comment"
    comments = instance.comments

    return render(request, "posts/post_detail.html", {
    "title": instance.title,
    "instance":instance,
    "share_string":share_string,
    "comments": comments,
    "comment_form": comment_form,
    })


@login_required
def post_update(request, slg=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slg=slg)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
        # messages.success(request, "Saved", extra_tags='some-tags')

    return render(request, "posts/post_form.html", {
        "title": instance.title,
        "instance":instance,
        "form":form,
        })


@login_required
def post_delete(request, slg=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slg=slg)
    instance.delete()
    messages.success(request, "Deleted")
    
    return redirect("posts:list")

def search(request):
    error = False
    queryset_list = Post.objects.active()
    
    if 'q' in request.GET:
        q = request.GET.get("q")
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            queryset_list = queryset_list.filter(
                Q(title__icontains=q)|
                Q(content__icontains=q)|
                Q(user__first_name__icontains=q)|
                Q(user__last_name__icontains=q)
                ).distinct()

    return render(request, "posts/post_list.html",{
        "object_list":queryset_list 
        })