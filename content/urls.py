from django.conf.urls import url
from content.views import articles, article, start
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf.urls.static import static
#from django.conf import settings
#from contacts.views import contacts
#from about_card.views import cards

urlpatterns = [
    #стартовая страница
    url(r'^$', start, name='start'),
    #конкретная статья
    url(r'^article/get/(?P<article_id>\d+)/$', article, name='статья'),
    #Все статьи
    url(r'^articles/$', articles, name='articles'),
    #Статьи по страницам
    url(r'^articles/page/(\d+)/$', articles),
    #Страница с контактами
#    url(r'^contacts/$', contacts, name='contacts'),
    #Cтраница с about_card
#    url(r'^articles/cards/$', cards, name='card'),

     ]
# url(r'^articles/all/$', articles),
#if settings.DEBUG:
#    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)