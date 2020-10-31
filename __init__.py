from django import apps 
from django.utils.translation import gettext_lazy as _


class CustomerConfig(apps.AppConfig):
    name = 'sw_customer'
    verbose_name = _('Покупці')
    verbose_name_plural = verbose_name
    

default_app_config = 'sw_customer.CustomerConfig'

