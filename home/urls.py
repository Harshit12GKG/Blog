from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('account-info/', views.account_info, name='account_info'),
    path('blog-detail/<slug>', views.blog_detail, name='blog_detail'),
    path('your-blogs/', views.see_blog, name='see_blog'),
    path('blog-delete/<id>', views.blog_delete, name='blog_delete'),
    path('blog-update/<slug>', views.blog_update, name='blog_update'),
    path('logout-view/', views.logout_view, name='logout_view'),
    path('verify/<token>', views.verify, name="verify"),
]
