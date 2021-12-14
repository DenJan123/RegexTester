from django.shortcuts import render, redirect
import re
from django.http import HttpResponse
from .models import Record
from django.views import View
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    if request.method == 'POST':
        patt = request.POST['regex']
        text = request.POST['text']
        res = re.search(patt, text)
        if res:
            res = True
        else:
            res = False
        res = Record.objects.create(regex=patt, text=text, result=res)
        # return HttpResponse(res)
        return redirect('result', pk=res.id)
    return render(request, 'record/index.html')


class ResultView(View):
    def get(self, request, *args, **kwargs):
        if kwargs and 'pk' in kwargs:
            result = get_object_or_404(Record, id=kwargs['pk'])
            return render(request, 'record/result.html', context={
                'record': result
            })


class HistoryView(View):
    def get(self, request, *args, **kwargs):
        result = Record.objects.all()
        return render(request, 'record/history.html', context={
            'records': result.order_by("-id")
        })
