compCharity
===========

When pulling from master, make sure to run
pip install -r requirements.txt

When editing HTML, use two spaces for tabs.
When editing python, use four spaces for tabs.

To read the logs, run in a free terminal:
tail -f goodbets.log

To print log statements from python:
import logging
logger = logging.getLogger(__name__)
logger.debug('any varable: %s' % anyVariable)

logs look like:
[30/Oct/2014 04:36:32] DEBUG [goodbets.templatetags.tags:10] any varable: 1
