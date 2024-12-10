from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.graficos.views import AggregatesViewSet

app_name = 'graficos'

urlspatters = [
    path("graficos/aggregates/", AggregatesViewSet.as_view(), name="aggregates"),
]