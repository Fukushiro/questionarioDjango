from django.utils.safestring import mark_safe
from django.template import Library

register = Library()

@register.filter(name='chr')
def chr(value):
    return chr(value + 65)