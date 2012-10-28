from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^services/books/$', 'books.views.list', name='booklist'),
    url(r'^services/book/new/$', 'books.views.new_book', name='newbook'),
	url(r'^services/book/(?P<book_id>\d+)/chapter/(?P<chapter_id>\d+)/add/$', 'books.views.add_chapter', name='home'),
	url(r'^services/book/(?P<book_id>\d+)/chapter/(?P<chapter_id>\d+)/$', 'books.views.chapter', name='home'),
	url(r'^services/book/(?P<book_id>\d+)/chapter/$','books.views.chapterOne'),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
