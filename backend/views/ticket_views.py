from django.shortcuts import render, redirect, HttpResponse
from repository import models
from backend.pager import PaginationTicket
from repository.forms.forms import TicketForm
from django.contrib.auth.decorators import login_required


@login_required
def index_ticket(request):
    '''
    票务管理主页
    :param request:
    :return:
    '''
    user = request.user
    if user.has_perm("repository.view_ticket"):
        obj = models.Ticket.objects.all()
        current_page = request.GET.get('p')
        page_obj = PaginationTicket(obj.count(), current_page)
        data_list = obj[page_obj.start():page_obj.end()]
        return render(request, 'backend/ticket/index_ticket.html', {'data': data_list, 'page_obj': page_obj})
    else:
        return render(request, 'backend/404.html')

@login_required
def del_ticket(request):
    '''
    退票
    :param request:
    :return:
    '''
    nid = request.GET.get('nid')
    models.Ticket.objects.filter(id=nid).delete()
    return redirect('index_ticket')


@login_required
def add_ticket(request):
    '''
    售票
    :param request:
    :return:
    '''
    if request.method == 'GET':
        obj = TicketForm()
        return render(request, 'backend/ticket/add_ticket.html', {'obj': obj})
    elif request.method == 'POST':
        obj = TicketForm(request.POST)
        if obj.is_valid():
            plan = obj.cleaned_data.get('ticket_plan')
            row = obj.cleaned_data.get('ticket_row')
            column = obj.cleaned_data.get('ticket_column')
            models.Ticket.objects.create(ticket_plan=plan, ticket_column=column, ticket_row=row)
            return redirect('index_ticket')
        else:
            return render(request, 'backend/ticket/add_ticket.html', {'obj': obj})


@login_required
def search_ticket(request):
    '''
    根据影厅名称搜索票
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'backend/ticket/search_ticket.html')

    elif request.method == 'POST':
        name = request.POST.get('search_ticket')
        if models.Ticket.objects.filter(ticket_plan__plan_cinema__cinema_name=name).count():
            ticket = models.Ticket.objects.filter(ticket_plan__plan_cinema__cinema_name=name)
            return render(request, 'backend/ticket/search_ticket.html', {'ticket': ticket})
        else:
            return render(request, 'backend/ticket/search_ticket.html')


