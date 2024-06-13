from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from main import url

urlpatterns = [
                  re_path(r'main/user/register/', CreateUserView.as_view(), name="register"),
                  re_path(r'main/token/refresh/', TokenRefreshView.as_view(), name="refresh"),
                  re_path(r'main/token/', TokenObtainPairView.as_view(), name="get_token"),
                  re_path(r'main-auth/', include("rest_framework.urls")),
                  re_path(r'main/', include("main.url")),
                  re_path(r'^admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
