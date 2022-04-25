from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login_id, name = 'login'),
    path('logout', views.logout_request, name = 'logout'),
    path('register', views.register, name = 'register'),
    path('home', views.home_page, name = 'home'),
    path('home/loan', views.get_loan, name = 'loan'),
    path('home/profile', views.profile, name = 'profile'),
    path('home/profile/update', views.update, name = 'update'),
    path('home/transfer', views.transaction, name = 'transfer'),
    path('home/remove', views.remove_account, name = 'remove'),
    # path('/book/<int:book_id>', views.book_by_id),
    # path('customer/<int:cuss_id>', views.account_id),
    # path('account/<int:cuss_id>/<string:type>/<int:acc_id>', views.account_id),
]

# if settings.DEBUG:
#     urlpatterns += statistics(
#         settings.STATIC_URL,
#         document_root=settings.STATIC_ROOT
#         )
#     urlpatterns += Statistic(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#         )

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Change Site Title, Index Title and Site Title
admin.site.site_header = "Dragon Bank Administration"
admin.site.site_title = "Dragon Bank Administration"
admin.site.index_title = "Welcome to Dragon Bank Administration Admin Panel"