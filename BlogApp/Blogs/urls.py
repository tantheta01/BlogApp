from django.urls import path
from . import views
# from BlogApp.core import views as core_views

urlpatterns = [
	path('', views.loginpage, name = 'loginpage'),
	path(r'dashboard/<user_name>/', views.dashboard, name = 'dashboard'), 
	path('edit/<int:pk>/', views.postedit, name = 'post_edit'),
	path(r'user_login/', views.user_login, name = 'user_login'),
	path(r'addpost/', views.addpost, name = 'addpost'),
	path(r'log_out/', views.user_logout, name = 'logout'), 
	path(r'register/', views.register, name = 'register'), 
	path(r'viewposts/<genre>/', views.viewposts, name = 'viewpost')
	]