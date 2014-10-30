from django import template
import re
import logging
logger = logging.getLogger(__name__)

register = template.Library()

@register.simple_tag
def active(request, pattern):
    logger.debug('pattern type %s' % (pattern))
    if pattern in request.path:
        return 'active'
    else:
        return ''
