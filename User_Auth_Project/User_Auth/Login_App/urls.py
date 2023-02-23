from django.urls import path,re_path as url 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Login_App import views
app_name = 'Login_App'
urlpatterns = [
    path('',views.home,name='home'),
    path('register_user/',views.register_user,name='register_user'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
