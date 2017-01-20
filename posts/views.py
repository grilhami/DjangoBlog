from django.utils import timezone
from urllib import quote_plus
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required


#paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


# views
from django.views.generic import ListView, CreateView, DetailView, DeleteView

#model
from .models import Post
from .forms import PostForm


@login_required:
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

    # context = {
    #    "object_list": queryset,
    #    "title": "List"
    #   }
    return render(request,"posts/post_list.html",{
        "object_list": queryset,
        "title": "List"
        })

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
    context = {
                "form":form,
    }
    return render(request, "posts/post_form.html", context)

def post_detail(request, slg=None):
    #instance = Post.objects.get(Post, id="3")
    instance = get_object_or_404(Post,slg=slg)
    share_string = quote_plus(instance.content)
    context = {
    "title": instance.title,
    "instance":instance,
    "share_string":share_string,
    }
    return render(request, "posts/post_detail.html", context)

def post_update(request, slg=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slg=slg)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
        messages.success(request, "Saved", extra_tags='some-tags')
    context={
	"title": instance.title,
        "instance":instance,
        "form":form,
    }
    return render(request, "posts/post_form.html", context)

def post_delete(request, slg=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slg=slg)
    instance.delete()
    messages.success(request, "Deleted")
    return redirect("posts:list")
