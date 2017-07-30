# Copyright (C) 2016-2017 CS-SI. All Rights Reserved.
# Author: Antoine Luong <antoine.luong@c-s.fr>

from __future__ import absolute_import, division, print_function, unicode_literals

import pkg_resources

from prewikka import version, view, template, hookmanager, error, resource

"""A Twitter plugin"""

class Twitter(view.View):
    plugin_name = "Twitter notification"
    plugin_author = "Antoine Luong"
    plugin_license = version.__license__
    plugin_version = version.__version__
    plugin_copyright = version.__copyright__
    plugin_description = N_("Twitter notification plugin")
    plugin_htdocs = (("twitter", pkg_resources.resource_filename(__name__, 'htdocs')),)

    def __init__(self):
        view.View.__init__(self)
        if not env.config.get('twitter', {}) or not env.config.twitter.get('account') or not env.config.twitter.get('widget-id'):
            raise error.PrewikkaUserError(N_("Twitter configuration"), N_("Twitter plugin disabled: not configured"))

        hookmanager.register("HOOK_TOPLAYOUT_EXTRA_CONTENT", self._toplayout_extra_content_hook)

    def _toplayout_extra_content_hook(self):
        return resource.HTMLSource(template.PrewikkaTemplate(__name__, "templates/twitter.mak").render())
