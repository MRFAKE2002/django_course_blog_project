from django.urls import path
from . import views


urlpatterns =[
    path('', views.HomePostListView.as_view(), name= 'home_page'),
    path('<int:pk>/', views.DetailPostListView.as_view(), name= 'detail_page'),
    path('create/', views.CreateBlogPost.as_view(), name= 'create_page'),
    path('<int:pk>/update', views.UpdatePostView.as_view(), name= 'update_post'),
    path('<int:pk>/delete', views.DeletePostListView.as_view(), name= 'delete_post'),
]
