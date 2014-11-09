from django import template
import re
import logging
logger = logging.getLogger(__name__)
register = template.Library()

@register.simple_tag
def active(request, pattern='', view=''):
    path = request.path[1:] # Strip the leading /

    if view != '':
        for urlpattern in urls.urlpatterns:
            # Skip include()s, they don't have the _callback_str attribute.
            if isinstance(urlpattern, RegexURLResolver):
                continue

            if view == urlpattern._callback_str:
                pattern = urlpattern.regex
                break

    if pattern == '':
        return ''

    if re.search(pattern, path):
        return 'active'
    else:
        return ''

@register.filter
def calculate_pot(chipins):
	return str(sum([chipin.amount for chipin in chipins]))
