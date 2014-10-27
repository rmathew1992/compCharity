from django import template
import re
import logging
logger = logging.getLogger(__name__)

register = template.Library()

@register.simple_tag
def active(request, pattern):
    if pattern in request.path:
        return 'active'
    else:
        return ''
