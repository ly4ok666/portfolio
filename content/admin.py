from django.contrib import admin
from content.models import Article
#from contacts.models import Contact
#from about_card.models import Card

class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'article_title',
        'article_text',
        'article_date',
        'article_image',
        'video',

    ]
    list_display = ('article_title', 'article_date', 'article_image', 'bit',)
    list_filter = [
        'article_date',
    ]
class ContactsAdmin(admin.ModelAdmin):
    fields = [
        'contacts_title',
        'contacts_text',


    ]
    list_display = ('contacts_title',)

#class CardAdmin(admin.ModelAdmin):
#    fields = [
#        'card_title',
#        'card_text',
#        'card_image',
#
#    ]
#    list_display = ('card_title', 'card_image', 'bit')

admin.site.register(Article, ArticleAdmin)
#admin.site.register(Contact, ContactsAdmin)
#admin.site.register(Card, CardAdmin)