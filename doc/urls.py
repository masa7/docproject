from django.urls import path
from . import views
#put the name in order to find relevant URL pattern
app_name = 'doc'
urlpatterns = [
    # Use indexView in View module in order to access docApp
    path('', views.IndexView.as_view(), name='index'),

    # 写真登録ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    
    # 登録完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),

    # カテゴリー一覧ページへ
    # docs/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('docs/<int:category>', views.CategoryView.as_view(), name='docs_cat'),

    # ユーザーの登録一覧ページ
    # docs/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>', views.UserView.as_view(), name = 'user_list'),

    # 詳細ページ
    # photo-detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('doc-detail/<int:pk>', views.DetailView.as_view(), name = 'doc_detail'),
    
    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    # 投稿写真の削除
    # photo/<Photo postsテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('doc/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name = 'photo_delete'),
]