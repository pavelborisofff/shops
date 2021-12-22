from django.urls import path
from app import views


urlpatterns = [
    path('cities/', views.cities_list, name='cities_list'),
]
# path('', views.index, name='index'),
# path('about/', views.about, name='about'),
# path('contact/', views.contact, name='contact'),
# path('login/', views.login, name='login'),
# path('logout/', views.logout, name='logout'),
# path('register/', views.register, name='register'),
# path('profile/', views.profile, name='profile'),
# path('profile/edit/', views.edit_profile, name='edit_profile'),
# path('profile/change_password/', views.change_password, name='change_password'),
# path('profile/change_email/', views.change_email, name='change_email'),
# path('profile/change_email/confirm/<str:token>/', views.change_email_confirm, name='change_email_confirm'),
# path('profile/change_email/cancel/', views.change_email_cancel, name='change_email_cancel'),
# path('profile/change_email/resend/', views.change_email_resend, name='change_email_resend'),
# path('profile/change_email/resend/<str:token>/', views.change_email_resend_confirm, name='change_email_resend_confirm'),
# path('profile/change_email/resend/<str:token>/cancel/', views.change_email_resend_cancel, name='change_email_resend_cancel'),
# path('profile/change_email/resend/<str:token>/resend/', views.change_email_resend_resend, name='change_email_resend_resend'),
# path('profile/change_email/resend/<str:token>/resend/<str:token2>/', views.change_email_resend_resend_confirm, name='change_email_resend_resend_confirm'),
# path('profile/change_email/resend/<str:token>/resend/<str:token2>/cancel/', views.change_email_resend_resend_cancel, name='change_email_resend_resend_cancel'),
# path('profile/change_email/resend/<str:token>/resend/<str:token2>/resend/', views.change_email_resend_resend_resend, name='change_email_resend_resend_resend'),
# path('profile/change_email/resend/<str:token>/resend/<str:token2>/resend/<str:token3>/', views.change_email_resend_resend_resend_confirm, name='change_email_resend_resend_resend_confirm'),
# path('profile/change_email/resend/<str:token>/resend/<str:token2>/resend/<str:token3>/cancel/', views.change_email_resend_resend_resend_cancel, name='change_email_resend_resend_resend_cancel'),
# path('profile/change_email/resend/<str:token>/resend/<str:token2>/resend/<str:token3>/resend/', views.change_email_resend_resend_resend_resend, name='change_email_resend_resend_resend_resend'),


