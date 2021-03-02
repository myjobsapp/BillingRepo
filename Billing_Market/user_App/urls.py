from django.urls import path
from . import views
urlpatterns=[

    path('reg/',views.RegisterView.as_view(), name='register'),
    path('login/',views.loginView, name='login'),
    path('logout/',views.logoutView, name='logout'),
    #path('logout/',views.logoutView),
    #path('var/',views.demoView)
]