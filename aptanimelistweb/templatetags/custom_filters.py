# custom_filters.py
from django import template

register = template.Library()

@register.filter
def slice_string(value, length):
    return value[:length]
