# Copyright (C) 2016 CS-SI. All Rights Reserved.
# Author: Antoine Luong <antoine.luong@c-s.fr>

from pkg_resources import resource_filename

from prewikka import env, error, pluginmanager, template
from . import templates

class Twitter(pluginmanager.PluginBase):
    plugin_name = "Twitter notification"
    plugin_author = "Antoine Luong"
    plugin_license = "GPL"
    plugin_version = "1.0.0"
    plugin_copyright = "CSSI"
    plugin_description = "Twitter notification plugin"
    plugin_htdocs = (("twitter", resource_filename(__name__, 'htdocs')),)

    def __init__(self):
        pluginmanager.PluginBase.__init__(self)
        conf = getattr(env.config, "twitter", {})
        if not conf:
            raise error.PrewikkaUserError(None, "Twitter plugin disabled: not configured")

        self._account = conf.getOptionValue("account")
        self._widget_id = conf.getOptionValue("widget-id")
        if not self._account or not self._widget_id:
            raise error.PrewikkaUserError(None, "Twitter plugin disabled: not configured")

        env.hookmgr.register("HOOK_TOPLAYOUT_EXTRA_CONTENT", self._toplayout_extra_content_hook)

    def _toplayout_extra_content_hook(self, request, user, dataset):
        tmpl = template.PrewikkaTemplate(templates.Twitter)
        dset = dict(dataset)
        dset["account"] = self._account
        dset["widget_id"] = self._widget_id
        dataset["toplayout_extra_content"] += tmpl.render(searchList=[dset])
        # Authorize other plugins to the same hook, as it is triggered with all()
        return True
