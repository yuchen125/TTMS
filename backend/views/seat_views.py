from django.shortcuts import render, redirect, HttpResponse
from repository import models
from backend.pager import Pagination
from django.contrib.auth.decorators import login_required


@login_required
def index_seat(request):
    '''
    座位管理主页
    :param request:
    :return:
    '''
    user = request.user
    if user.has_perm("repository.view_seat"):
        obj = models.Seat.objects.order_by('seat_cinema_id', 'seat_cinema', 'seat_row', 'seat_column')
        current_page = request.GET.get('p')
        page_obj = Pagination(obj.count(), current_page)
        data_list = obj[page_obj.start():page_obj.end()]
        return render(request, 'backend/seat/index_seat.html', {'data': data_list, 'page_obj': page_obj})
    else:
        return render(request, 'backend/404.html')


@login_required
def del_seat(request):
    '''
    删除座位
    :param request:
    :return:
    '''
    nid = request.GET.get('nid')
    models.Seat.objects.filter(id=nid).delete()
    return redirect('index_seat')


@login_required
def search_seat(request):
    '''
    根据影厅名称搜索该影厅所有座位
    :param request:
    :return:
    '''
    name = request.POST.get('search_seat_name')
    if models.Cinema.objects.filter(cinema_name=name).count():
        obj = models.Seat.objects.filter(seat_cinema__cinema_name=name).order_by('seat_cinema_id', 'seat_cinema',
                                                                                 'seat_row', 'seat_column')
        return render(request, 'backend/seat/search_seat.html', {'data': obj, 'search_seat_name': name})

    else:
        return render(request, 'backend/seat/search_seat.html', {'search_seat_name': name})
