from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import index, sign_up, user_account, show_categories, create_category, delete_category  # , show_order


app_name = 'application'  # namespace

urlpatterns = [
    path('', index, name='index'),
    path('categories/page<int:page>/', login_required(show_categories), name='show_categories'),
    # path('notes/page<int:page>/', login_required(show_notes), name='show_notes'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('registration/sign_up', sign_up, name='sign_up'),
    path('user_account', login_required(user_account), name='user_account'),
    path('create_category/', login_required(create_category), name='create_category'),
    # path('order<int:id>/', show_order, name='show_order'),
    path('delete_category/id<int:id>/', login_required(delete_category), name='delete_category'),
    # path('delete_category/', login_required(delete_category), name='delete_category'),
]
