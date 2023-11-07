from django.urls import path, include
#from .views import PostsList
from news.views import NewsList, PostDetail, Posts, PostCreateView, PostUpdateView, PostDeleteView, IndexView 

app_name = 'news'

urlpatterns = [
    #path('admin/', admin.site.urls), 
    path('posts/', NewsList.as_view()), 
    path('<int:pk>', PostDetail.as_view()),
    path('news_page/', Posts.as_view()),
    path('post/create/', PostCreateView.as_view(), name='post_create'), # Ссылка на создание поста
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='product_update'), # Ссылка на редактирование поста
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='product_delete'), # Ссылка на удаеление поста
    path('', IndexView.as_view())
    ]