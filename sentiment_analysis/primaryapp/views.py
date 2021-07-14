from django.shortcuts import render

from primaryapp.models import Sentiment

def index(request):
    """ View function for home page of site. """

    num_sentiments = Sentiment.objects.all().count()
    num_positve_sentiment = Sentiment.objects.filter(emotion__exact = 1).count()
    num_negative_sentiment = Sentiment.objects.filter(emotion__exact = 0).count()

    context = {
        'num_sentiments': num_sentiments,
        'num_positve_sentiment': num_positve_sentiment,
        'num_negative_sentiment': num_negative_sentiment,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context = context)

from django.views import generic

class SentimentListView(generic.ListView):
    model = Sentiment
    paginate_by = 10

class SentimentDetailView(generic.DetailView):
    model = Sentiment
    paginate_by = 10

import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from primaryapp.forms import NewSentimentForm

#import translate as trs
import primaryapp.translate as trs

def new_sentiment(request):    
    #If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding)
        form = NewSentimentForm(request.POST)

        #sentence = form['sentence']
        sentence = form.data['sentence']
        sentence_str = str(sentence)
        sentence_lower = sentence_str.lower()
        answer = trs.translate(sentence_lower)
        #answer = form.data['sentence']
        print('Oración traducida:',answer)
        import primaryapp.analisis_sentimientos as anse
        #sentimientoI = anse.classifySentiment(answer)
        sentimientoI = 1
        sentimientoS = 'Neutral'
        PATH = 'Direccion'

        if sentimientoI:
            sentimientoS = 'positivo'
            PATH = 'imgs/happy_icon.png'            
        else:
            sentimientoS = 'negativo'
            PATH = 'imgs/sad_icon.png'

        predeterminado = 'Escribe tu emoción'
        form = NewSentimentForm(initial = {'sentence' : predeterminado})
        context = {
            'form': form,
            'sentimientoI': sentimientoI,
            'sentimientoS': sentimientoS,
            'path': PATH,
        }
        
        return render(request, 'primaryapp/sentiment_new.html', context)
    else:
        predeterminado = 'Escribe tu emoción'
        form = NewSentimentForm(initial = {'sentence' : predeterminado})
        context = {
            'form': form,
        }
        return render(request, 'primaryapp/sentiment_new.html', context)