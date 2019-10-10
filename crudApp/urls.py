from django.urls import path, include
from .views import *
from rest_framwork.routers import DefaultRouter
from . import views

appname='crudApp'
router = DefaultRouter()
router.regiester('product', views.ProductViewSet)


urlpatterns = [
    # path('home/',home,name='home'),
    # path('create_post/',create_post,name='create_post'),
    # path('edit_post/<int:post_pk>',edit_post,name='edit_post'),
    # path('delete_post/<int:post_pk>',delete_post,name='delete_post'),
    # path('detail_post/<int:post_pk>',detail_post,name='detail_post'),
    
    # path('home/', Home.as_view(), name= 'home'),
    # path('create_post/', Create_post.as_view(), name = 'create_post'),
    # path('edit_post/<int:pk>',Edit_post.as_view(), name = 'edit_post'),
    # path('delete_post/<int:pk>',Delete_post.as_view(), name = 'delete_post'),
    # path('detail_post/<int:pk>',Detail_post.as_view(), name = 'detail_post'),
    # path('detail_post2/<int:pk>',Detail_post.as_view(), name = 'detail_post2'),
    path('', include(router.urls)),
    
]