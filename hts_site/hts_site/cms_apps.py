from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ManagementAppHook(CMSApp):
    name = _('Management')

    def get_urls(self, page=None, language=None, **kwargs):
        return ['management.urls']


apphook_pool.register(ManagementAppHook)
