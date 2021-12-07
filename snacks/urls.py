from django.urls import path

from snacks.views import SnackListView,SnackDeatailView,HomeView,SnackCreateView,SnackUpdateView,SnackDeleteView


urlpatterns=[ 
    path('snack/',SnackListView.as_view(),name='snack_list'),
    path('',HomeView.as_view(),name='home'),
    path('snack/<int:pk>/',SnackDeatailView.as_view(),name='snack_detail'),
    path('snack/snack_create',SnackCreateView.as_view(),name='snack_create'),
    path('snack/<int:pk>/snack_update',SnackUpdateView.as_view(),name='snack_update'),
    path('snack/<int:pk>/snack_delete',SnackDeleteView.as_view(),name='snack_delete')
]