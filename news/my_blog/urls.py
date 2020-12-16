from django.urls import path
from . import views

urlpatterns = [
         path('show_all_blog/',views.Show_blog.as_view(),name='show-all-blog'),
         path('new_blog/',views.New_blog_create.as_view(),name='new-blog'),
         path('blog/<int:pk>',views.BlogDetailView.as_view(), name='blog-detail'),
         path('blog/<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog-update'),
         path('blog/<int:pk>/delete/', views.blogDeleteView.as_view(), name='blog-delete'),
]