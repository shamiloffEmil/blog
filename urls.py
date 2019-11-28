from django.template.backends import django
from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/like/', views.add_like_to_post, name='add_like_to_post'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),

    path('drafts/', views.post_draft_list, name='post_draft_list'),

    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('user/<int:pk>', views.about_list, name='about_list'),
	path('user/<int:pk>/about/', views.about_new, name='about_new'),

    # path('user/<int:pk>/update/', views.update_profile, name='update_profile'),


    # path(r'^accounts/login/$',  django.contrib.auth.views.login, name='login'),
	# path(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),

]
