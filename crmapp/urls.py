from django.conf.urls import patterns, include, url
from django.contrib import admin

from marketing.views import HomePage

urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),

    # Marketing pages
    url(r'^$', HomePage.as_view(), name='home'),

    # Subscriber related URLs

    # Admin URL

    # Login/Logout URLs

    # Account related URLs

    # Contact related URLs

    # Communication related URLs

)


