from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

# from posts.models import Posts


class IndexView(TemplateView):

    template_name = "home.html"

    # def get_context_data(self, **kwargs):

        # context = super(IndexView, self).get_context_data(**kwargs)
        # context['latest_post'] = Post.objects.all()[:5]
        # return context

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
