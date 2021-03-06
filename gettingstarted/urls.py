from django.conf.urls import patterns, include, url
from django.contrib import admin

import hello.views


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello.views.index, name='index'),
    url(r'^game/', hello.views.game, name='game'),
    url(r'^scores/', hello.views.scores, name='scores'),
    url(r'^connectfour/', hello.views.connect, name='connect'),
)
