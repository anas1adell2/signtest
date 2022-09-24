from django.urls import path
from django.views.generic import TemplateView

app_name= "login"
urlpatterns = [
    path('', TemplateView.as_view(template_name='login/signin.html'), name="signin"),
    path('signup/', TemplateView.as_view(template_name='login/signup.html'), name="signup"),
]

