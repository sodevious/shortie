# from django.urls import include, path
# from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'entries', views.EntryViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

urlpatterns = [
    path('', views.api_root),

    path('entries/', views.EntryList.as_view(), name='entry-list'),
    path('entries/<int:pk>/', views.EntryDetail.as_view(), name='entry-detail'),
    path('api-auth/', include('rest_framework.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)