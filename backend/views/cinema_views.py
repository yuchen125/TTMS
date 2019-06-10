from django.shortcuts import render, redirect
from repository import models
from repository.forms.forms import CinemaForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    '''
    后台主页，也是影厅管理主页
    :param request:
    :return:
    '''
    cinema_list = models.Cinema.objects.filter()
    return render(request, 'backend/cinema/index.html', {'cinema_list': cinema_list})


@login_required
def del_cinema(request):
    '''
    删除影厅
    :param request:
    :return:
    '''
    nid = request.GET.get('nid')
    models.Cinema.objects.filter(id=nid).delete()
    return redirect('index')


@login_required
def edit_cinema(request):
    '''
    编辑影厅
    :param request:
    :return:
    '''
    if request.method == 'GET':
        nid = request.GET.get('nid')
        cinema_list = models.Cinema.objects.filter(id=nid).first()
        return render(request, 'backend/cinema/edit_cinema.html', {'cinema_list': cinema_list})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        name = request.POST.get('cinema_name')
        cinema_row = int(request.POST.get('cinema_row'))
        cinema_column = int(request.POST.get('cinema_column'))
        detail = request.POST.get('cinema_detail')
        cinema_list = models.Cinema.objects.filter(id=nid).first()
        if len(name) >= 10 or len(detail) >= 50 or cinema_row > 10 or cinema_column > 10:
            return render(request, 'backend/cinema/edit_cinema.html',
                          {'cinema_list': cinema_list, 'message': '编辑输入格式不正确，请重新输入'})
        models.Cinema.objects.filter(id=nid).update(cinema_name=name, cinema_row=cinema_row,
                                                    cinema_column=cinema_column, cinema_detail=detail)
        models.Seat.objects.filter(seat_cinema_id=nid).delete()
        seat_list = []
        for j in range(1, cinema_row + 1):
            for k in range(1, cinema_column + 1):
                seat_list.append(models.Seat(seat_cinema_id=nid, seat_row=j, seat_column=k))
        models.Seat.objects.bulk_create(seat_list)
        return redirect('index')


@login_required
def search_cinema(request):
    '''
    搜索影厅
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'backend/cinema/search_cinema.html')

    elif request.method == 'POST':
        name = request.POST.get('search_cinema_name')
        if models.Cinema.objects.filter(cinema_name=name).count():
            cinema = models.Cinema.objects.filter(cinema_name=name).values()
            return render(request, 'backend/cinema/search_cinema.html', {'cinema': cinema})
        else:
            return render(request, 'backend/cinema/search_cinema.html')


@login_required
def add_cinema(request):
    '''
    增加影厅
    :param request:
    :return:
    '''
    if request.method == "GET":
        obj = CinemaForm()
        return render(request, 'backend/cinema/add_cinema.html', {'obj': obj})
    else:
        obj = CinemaForm(request.POST)
        if obj.is_valid():
            models.Cinema.objects.create(**obj.cleaned_data)
            i = obj.cleaned_data.get('id')
            r = obj.cleaned_data.get('cinema_row')
            c = obj.cleaned_data.get('cinema_column')
            seat_list = []
            for j in range(1, r + 1):
                for k in range(1, c + 1):
                    seat_list.append(models.Seat(seat_cinema_id=i, seat_row=j, seat_column=k))
            models.Seat.objects.bulk_create(seat_list)
            return redirect('index')
        else:
            return render(request, 'backend/cinema/add_cinema.html', {'obj': obj})
