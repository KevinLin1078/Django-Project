from django.urls import path, include
from django.conf.urls import url

from django.views.decorators.csrf import csrf_exempt

app_name='users'

from .views import Index, Login, Register, SignUp
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('register/', Register.as_view(), name='register'),
	path('signup/', SignUp.as_view(), name='signup'),
	path('login/', Login.as_view(), name='login'),

	path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', jwt_views.TokenObtainPairView.as_view(), name='token_refresh'),


]