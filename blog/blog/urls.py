from django.contrib import admin
from django.urls import path
from feed.views import Home,CreateFeed,FeedDetailedView,CreateComment,UpdateFeed,DeleteFeed,Login,Logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("create-post/", CreateFeed.as_view(), name="create_post"),
    path("login/",Login.as_view(), name="login"),
    path("logout/",Logout.as_view(), name="logout"),
    path('post-detail/<int:pk>/', FeedDetailedView.as_view(), name='post_detail'),
    path('update-post/<int:pk>/', UpdateFeed.as_view(), name='update_post'),
    path('create-comment/<int:pk>/',FeedDetailedView.as_view(), name='create_comment'),
    path('delete-post/<int:pk>/', DeleteFeed.as_view(), name='delete_post'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
