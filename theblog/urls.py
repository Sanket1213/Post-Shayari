from django.urls import path
from .views import HomeView, ArticleDetails, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, PassView, WalgarAddPostView, WalgarUpdatePostView, WalgarDeletePostView, WalgarHomeView

urlpatterns = [
    path('', HomeView.as_view(),name="home"),
    path('article/<int:pk>', ArticleDetails.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category_list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('password/', PassView, name='password'),
    path('walgar/', WalgarHomeView.as_view(), name="w_home"),
    path('w_add_post/', WalgarAddPostView.as_view(), name="w_add_post"),
    path('w_article/edit/<int:pk>', WalgarUpdatePostView.as_view(), name="w_update_post"),
    path('w_article/<int:pk>/remove', WalgarDeletePostView.as_view(), name="w_delete_post"),
]