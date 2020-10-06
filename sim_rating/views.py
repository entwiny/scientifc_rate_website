from django.shortcuts import render
from sim_rating.models import Link, Article, Sim_rate, Topic, Source
from itertools import combinations
# Create your views here.

count = 0
articles = [0, 1, 2, 3]
def main(request):
    global articles, count
    num_articles = Article.objects.all().count()
    context = {'num_articles': num_articles}
    articles = Article.objects.order_by('?')[:4]
    count = 1
    return render(request, 'main.html', context=context)

def SimRateView1(request):

    global articles, count
    article_pairs = list(combinations([0 ,1, 2, 3], 2))
    article_pair = article_pairs[count - 1]
    article1 = articles[article_pair[0]]
    article2 = articles[article_pair[1]]
    count += 1
    
    if count >= 6:
        next_url = "end"
    else:
        next_url = chr(count+96)
    
    context = {'article1': article1, 'article2': article2, 'next_url': next_url}
    
    return render(request, 'article1_2.html', context)
    
def end(request):
    return render(request, 'end.html')
    
