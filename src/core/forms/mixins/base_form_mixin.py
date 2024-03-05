# -*- coding: utf-8 -*-#
from core.forms.mixins.html5_mixin import Html5Mixin
from django import forms


class BaseFormMixin(Html5Mixin, forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseFormMixin, self).__init__(*args, **kwargs)
