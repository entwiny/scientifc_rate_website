from django.shortcuts import render
from sim_rating.models import Link, Article, Sim_rate, Topic, Source
from itertools import combinations
from .forms import SimForm
import random
from django.shortcuts import redirect
# Create your views here.

art_count = 0
count = 0
articles = [0, 1, 2, 3]
page_count = 0

def main(request):
    global articles, count, page_count, art_count
    num_articles = Article.objects.all().count()
    context = {'num_articles': num_articles}
    articles = random.sample(list(Article.objects.all()), 4)
    count = 1
    page_count = 0
    art_count = 0
    return render(request, 'main.html', context=context)

def ArticleView(request):

    global articles, art_count

    if art_count < 3:
        article1 = articles[art_count]
        art_count += 1
        next_url = 'article' + str(art_count+1)
        context = {'article1': article1, 'next_url': next_url}
        return render(request, 'articles_extend.html', context)

    else:
        article1 = articles[art_count]
        next_url = 'sim_rates/a'
        context = {'article1': article1, 'next_url': next_url}
        return render(request, 'articles_extend.html', context)


def SimRateView1(request):

    global articles, count
    
    if count <= 6:
        article_pairs = list(combinations([0 ,1, 2, 3], 2))
        article_pair = article_pairs[count - 1]
        article1 = articles[article_pair[0]]
        article2 = articles[article_pair[1]]
        
        if request.method == 'POST':
            form = SimForm(request.POST)
            # check data is valid to post
            if form.is_valid():
                similarity = form.data["similarity"]
                add_rate = Sim_rate(similarity=similarity, article1=article1, article2=article2)
                add_rate.save()
                count += 1
                return redirect(SimRateView1)
        else:
            form = SimForm()
        context = {'article1': article1, 'article2': article2, 'form':form}
        
        return render(request, 'article1_2.html', context)
    else:
        return render(request, 'end.html')
    
    

def end(request):
    return render(request, 'end.html')
    
