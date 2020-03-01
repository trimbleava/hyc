from django import template
from django.urls import reverse
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return None

@register.filter
@stringfilter
def lower(value):
    return value.lower()


@register.simple_tag
def nav_css_class(page_class):
    if not page_class:
        return None
    else:
        return page_class

