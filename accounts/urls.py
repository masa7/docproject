from django.urls import path
from . import views
#viewsをインポートしてauth_viewという名前で利用
from django.contrib.auth import views as auth_views

#put the name in order to find relevant URL pattern
app_name = 'accounts'
urlpatterns = [
    # call signup page view
    # access to [https://<host name>/signup/]
    # instance of SingUpView based on views module
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # call signup completion page view 
    # access to [https://<host name>/signup_success/]
    # instance of SingUpSuccessView based on views module
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    # ログインページの表示
    # access to [https://<host name>/login/]
    # django.contrib.auth.views.LoginViewをインスタンス化して利用
    # login.htmlテンプレートをレンダリング
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # ログアウトの実行
    # access to [https://<host name>/logout/]
    # django.contrib.auth.views.LogoutViewをインスタンス化して利用
    # logout.htmlテンプレートをレンダリング
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]