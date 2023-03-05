from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()
from ..models import Post, Visual
from django.utils.safestring import mark_safe
import markdown


@register.simple_tag
def total_posts():
    return Post.objects.all().count()


@register.inclusion_tag('post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.all().order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('post/show_carousel.html')
def show_carousel():
    visuals = Visual.objects.order_by('index').all()
    return {'visuals': visuals}


@register.inclusion_tag('post/show_posts.html')
def show_posts():
    posts = Post.objects.all()
    return {'posts': posts}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))