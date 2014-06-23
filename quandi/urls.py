from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quandi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'testsite.views.index', name='home1'),
	url(r'^About/', 'testsite.views.about', name='about'),
	url(r'^services/', 'testsite.views.services', name='serv'),
	url(r'^submit/', 'testsite.views.submission', name='submit'),
	url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'testsite/login.html'}, name='login'),
	url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	url(r'^register/', 'testsite.views.register', name='register'),
	url(r'^profile/', 'testsite.views.profile', name='profile'),
	url(r'^password_change_done/', 'testsite.views.pwchangedone', name='password_change_done'),
	url(r'^password_change_form/', 'django.contrib.auth.views.password_change', {'template_name': 'testsite/password_change_form.html', 'post_change_redirect': '/password_change_done'}),
	
)
