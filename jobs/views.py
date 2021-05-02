from django.shortcuts import render, redirect
from .models import Cost
from .forms import CostForm
from django.urls import reverse

def costView(request):
    lastResult = Cost.objects.all().last()
    costList = Cost.objects.all().order_by('-costModel')
    incomeList = Cost.objects.all().order_by('-incomeModel')

    # generate highest profit:
    profitList = []
    for datas in Cost.objects.all():
        x1 = datas.incomeModel
        y1 = datas.costModel
        z1 = datas.dateModel
        profitList.append([x1-y1, z1])
    orderedProfitList = sorted(profitList, reverse=True)

    # main form statements:
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
    context = {'form':form, 'lastData':lastResult, 'listOfCost':costList,
                'listOfIncome': incomeList, 'listOfProfit': orderedProfitList}

    return render(request, 'jobs/cost.html', context)
