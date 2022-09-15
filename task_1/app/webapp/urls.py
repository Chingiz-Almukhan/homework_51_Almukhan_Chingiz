from django.urls import path

from webapp.views import home_view, stats, change

urlpatterns = [
    path('', home_view),
    path('cat_stats/', stats),
    path('cat_stats/change_state/', change)
]