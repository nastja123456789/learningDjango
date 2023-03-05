from django.urls import path, include
from . import views
from .feeds import LatestPostsFeed

app_name = 'polls'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('login/', views.user_login, name='login'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path("products", views.products, name="products"),
    path('<slug:category_slug>/', views.products, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path("recipe", views.recipe, name="recipe"),
    path('chart/filter-options/', views.get_filter_options, name='chart-filter-options'),
    path('chart/sales/<int:year>/', views.get_sales_chart, name='chart-sales'),
    path('polls/<int:question_id>/', views.detail, name='detail_question'),
    path('question/<int:question_id>/results/', views.results, name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('prediction', views.home, name='home'),
    path('logout', views.user_logout, name='logout'),
    path('ml', views.indexx, name="ml"),
    path('predictImage', views.predictImage, name="predictImage"),
    path('viewDataBase',views.viewDataBase,name="viewDataBase"),
]