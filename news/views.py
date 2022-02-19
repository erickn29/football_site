from django.shortcuts import render, get_object_or_404
from news.models import News, Club
from news.scripts.scrapp.clubs_sql import get_club_info
from django.core.paginator import Paginator


clubs_dict = get_club_info()

sorted_clubs_dict = {}
list_keys = list(clubs_dict.keys())
list_keys.sort()
for i in list_keys:
    sorted_clubs_dict.get(i, clubs_dict[i])
    sorted_clubs_dict[i] = clubs_dict[i]


def index(request):
    news_list = News.objects.order_by('-id')
    paginator = Paginator(news_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news_list': page_obj,
        'clubs_dict': sorted_clubs_dict,
    }
    return render(request, 'news/news.html', context=context)


def article(request, news_slug):
    if news_slug in clubs_dict.keys():
        return get_club_news_list(request, news_slug)
    article = get_object_or_404(News, url=news_slug)
    clean_article = article.content.split('.')
    if 'здесь' in clean_article[-2]:
        del clean_article[-2]
    article.content = '.'.join(clean_article) + '.'
    return render(request, 'news/article.html', context={
        'article': article,
        'clubs_dict': sorted_clubs_dict
    })


def get_club_news_list(request, club):
    news_list = News.objects.filter(club__icontains=club).order_by('-id')
    paginator = Paginator(news_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    name_club = Club.objects.filter(name__icontains=club)[0].name.split(',')[1]
    logo_club = Club.objects.filter(name__icontains=club)[0].logo
    context = {
        'news_list': page_obj,
        'club': name_club,
        'club_logo': logo_club,
        'clubs_dict': sorted_clubs_dict
    }
    return render(request, 'news/news.html', context=context)


