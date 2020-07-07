from django.urls import path, include

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import Register

app_name='users'

urlpatterns = [
	path('', Register.as_view(), name='index'),

]