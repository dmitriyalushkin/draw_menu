
from django.urls import path
from draw_menu.views import CategoryListView, PostByCategoryView

urlpatterns = [
    path('category_list/', CategoryListView.as_view(), name='category-list'),
    path('post_list/<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
]