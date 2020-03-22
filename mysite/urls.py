from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
] 
# urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # 배포 전 media root를 이용해서 이미지 저장하고 탐색했음.