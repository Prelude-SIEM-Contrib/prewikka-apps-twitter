# Copyright (C) 2016-2017 CS-SI. All Rights Reserved.
# Author: Antoine Luong <antoine.luong@c-s.fr>

from __future__ import absolute_import, division, print_function, unicode_literals

import pkg_resources

from prewikka import error, hookmanager, pluginmanager, resource, template


"""A Twitter plugin"""

class Twitter(pluginmanager.PluginBase):
    plugin_name = "Twitter notification"
    plugin_author = "Antoine Luong"
    plugin_license = "GPL"
    plugin_version = "5.0.0"
    plugin_copyright = "CSSI"
    plugin_description = "Twitter notification plugin"
    plugin_htdocs = (("twitter", pkg_resources.resource_filename(__name__, 'htdocs')),)

    def __init__(self):
        self._account = env.config.twitter.get("account")
        self._widget_id = env.config.twitter.get("widget-id")
        if not self._account or not self._widget_id:
            raise error.PrewikkaUserError("Missing configuration", "Twitter plugin disabled: not configured")

        pluginmanager.PluginBase.__init__(self)

    @hookmanager.register("HOOK_TOPLAYOUT_EXTRA_CONTENT")
    def _toplayout_extra_content_hook(self):
        tmpl = template.PrewikkaTemplate(__name__, "templates/twitter.mak")
        return resource.HTMLSource(tmpl.render(account=self._account, widget_id=self._widget_id))
