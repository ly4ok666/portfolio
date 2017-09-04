from django.shortcuts import render
#from django.http.response import HttpResponse
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
from content.models import Article
#from article.models import Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def start(request):
    """Домашняя страница нашего приложения Article"""
    return render(request, 'start.html')



def articles(request):
    """Вывод всех статей и пагинация (2 статьи на страницу)"""
    all_Articles = Article.objects.all()
    paginator = Paginator(all_Articles, 2)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render_to_response('content/articles.html', {'articles': articles })

def article(request, article_id=1):
    """Вывод одной конкретной статьи """
    return render_to_response('content/article.html', {'article': Article.objects.get(id=article_id),
                                               #'comments': Comments.objects.filter(comments_article_id=article_id),
                                               })

