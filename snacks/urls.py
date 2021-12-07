from django.urls import path

from snacks.views import SnackListView,SnackDeatailView


urlpatterns=[ 
    path('',SnackListView.as_view(),name='snack_list'),
    path('<int:pk>',SnackDeatailView.as_view(),name='snack_detail')
]