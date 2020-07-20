from django.urls import path,include
from .views import (
	UserProfileView,
	recover,
	recover_email,
	profile,
	import_xlsx,
	# login_form,
	# logout_func,
	# signup_form,
	)

app_name='accounts'

urlpatterns = [
	path('', UserProfileView, name='profileview'),
	path('profile', profile, name='profile'),
	# path('login/', login_form, name='login'),
 #    path('logout/', logout_func, name='logout'),
 #    path('signup/', signup_form, name='signup'),
	path('recover/', recover, name='recover'),
	path('recover_email',recover_email,name='recover_email'),
	path('import',import_xlsx,name='import'),
]
