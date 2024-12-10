from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.views.generic.base import TemplateView


class AggregatesViewSet(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'graficos/templates/index.html'
    title = "Aggregates"

    def get_context(self, **kwargs):
        pass


