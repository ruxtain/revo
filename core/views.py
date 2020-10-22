from django.shortcuts import render
from datetime import datetime, timedelta

def home(request):
    return render(request, 'core/home.html', {'data':'data'})


def substitute(request):

    t0 = datetime.today()
    t1 = t0 - timedelta(days=1)
    t2 = t0 - timedelta(days=2)

    v_dates = {}
    v_dates['v_day'] = datetime.strftime(t1, '%Y%m%d')
    v_dates['v_last_day'] = datetime.strftime(t2, '%Y%m%d')
    for i in range(2, 101):
        t = t1 - timedelta(days=i)
        v_dates['${{v_last_{}_day}}'.format(i)] = datetime.strftime(t, '%Y%m%d')

    return render(request, 'core/substitute.html', {})