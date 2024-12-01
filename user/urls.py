from django.urls import path
# from .views import UserUpdateView, UserCreateView
from .views import RegisterView
from django.views.generic import TemplateView


app_name = 'user_management'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('profile/', UserUpdateView.as_view(), name='user_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TemplateView.as_view(template_name='home.html'), name="login")
]