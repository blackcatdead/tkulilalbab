"""quesioner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from tkulilalbab import views as tk
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', tk.home, name='home'),
    path('blog', tk.blog, name='blog'),
    path('blog/page-<int:page>', tk.blog, name='blog'),
    path('artikel/<str:judul>_<int:id>', tk.artikel, name='artikel'),
    path('pengurusyayasan', tk.pengurusyayasan, name='pengurusyayasan'),
    path('gallery', tk.gallery, name='gallery'),
    path('download', tk.download, name='download'),
    # url(r'^mendaftar/', jurica.register, name='mendaftar'),
    # url(r'^masukadmin/?', jurica.loginadmin, name='masukadmin'),
    # url(r'^masuk/?', jurica.login, name='masuk'),
    # url(r'^keluaradmin/', jurica.logoutadmin, name='keluaradmin'),
    # url(r'^keluar/', jurica.logout, name='keluar'),
    # url(r'^selesai/', jurica.finish, name='selesai'),
    # url(r'^pertanyaan/?', jurica.questionnaire, name='pertanyaan'),
    # url(r'^mulaimengerjakan/', jurica.start, name='mulaimengerjakan'),
    # url(r'^admin/responden/', jurica.responden, name='responden'),
    # url(r'^admin/tambahresponden/', jurica.addresponden, name='tambahresponden'),
    # url(r'^admin/ubahresponden/$', jurica.editresponden, name='ubahresponden'),
    # url(r'^admin/hapusresponden/$', jurica.removeresponden, name='hapusresponden'),
    # url(r'^admin/resetresponden/$', jurica.resetresponden, name='resetresponden'),
    # url(r'^admin/detailresponden/$', jurica.detailresponden, name='detailresponden'),
    # url(r'^admin/exportexcel/$', jurica.exportexcel, name='exportexcel'),
    # url(r'^admin/export_xls/$', jurica.export_xls2, name='export_xls'),
    
    # url(r'^admin/', jurica.admin, name='admin'),
    # url(r'^ajax/table_responden/', jurica.table_responden, name='table_responden'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)