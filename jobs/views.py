from django.shortcuts import render, redirect
from .models import Cost
from .forms import CostForm
from django.urls import reverse

def costView(request):
    lastResult = Cost.objects.all().last()
    highestCost = Cost.objects.all().order_by('-costModel').first()
    highestIncome = Cost.objects.all().order_by('-incomeModel').first()

    if request.method == 'POST':
        form = CostForm(request.POST)
        if form.is_valid():
            setDate = request.POST.get('dateValue')
            setCost = request.POST.get('costValue')
            setIncome = request.POST.get('incomeValue')
            newData = Cost(dateModel=setDate, costModel=setCost, incomeModel=setIncome)
            newData.save()
            return redirect(reverse('cost'))
    else:
        form = CostForm()
    context = {'form':form, 'lastData':lastResult, 'topCost':highestCost,
                'topIncome': highestIncome}

    return render(request, 'jobs/cost.html', context)
