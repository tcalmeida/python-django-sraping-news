from django.shortcuts import render
from news.utils.collect_gamerant_news import collect_gamerant_data


def news_view(request):
    context = {
        'data_list': collect_gamerant_data('https://gamerant.com/', '//div[@class="w-display-card-content"]', './h5/a', './h5/a')
    }
    return render(request, 'home.html', context)


