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
	url(r'^About/', 'testsite.views.about', name='about'),
	url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'testsite/login.html'}),
	url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	url(r'^register/', 'testsite.views.register', name='register'),
	url(r'^services/', 'testsite.views.services', name='serv'),
	url(r'^$', 'testsite.views.index', name='home1'),
)
