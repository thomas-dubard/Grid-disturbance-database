from django.http import HttpResponse
from django.shortcuts import render

admins_and_passwords = [("a","x")]


def admin_co(request):
    return render(request, 'site_RTE/admin-co.html', {'admins_and_passwords':admins_and_passwords})

def home_page(request):
    return render(request, 'site_RTE/home.html', {})

def user_request(request):
    return render(request, 'site_RTE/user-request.html', {})

def admin_hist(request):
    return render(request, 'site_RTE/admin-hist.html', {})

def admin_input(request):
    return render(request, 'site_RTE/admin-input.html', {})

def admin_main(request):
    return render(request, 'site_RTE/admin-main.html', {})

def func_fault(request):
    return render(request, 'site_RTE/fault.html', {})

def grid_dist(request):
    return render(request, 'site_RTE/grid-dist.html', {})

def func_interrupt(request):
    return render(request, 'site_RTE/interrupt.html', {})

def user_interrupt(request):
    return render(request, 'site_RTE/user-interrupt.html', {})

def main(request):
    return render(request, 'site_RTE/main.html', {})

def func_outage(request):
    return render(request, 'site_RTE/outage.html', {})

def user_fault(request):
    return render(request, 'site_RTE/user-request.html', {})

def admin_grid_dist(request):
    return render(request, 'site_RTE/admin-grid-dist.html', {})

def home_interrupt(request):
    return render(request, 'site_RTE/home-interrupt.html', {})

def user_outage(request):
    return render(request, 'site_RTE/user-outagehtml', {})

def user_grid_dist(request):
    return render(request, 'site_RTE/user-grid-dist.html', {})
