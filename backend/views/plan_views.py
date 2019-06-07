from django.shortcuts import render, redirect, HttpResponse
from repository import models
from backend.pager import PaginationPlan
from repository.forms.forms import PlanForm
from django.contrib.auth.decorators import login_required


@login_required
def index_plan(request):
    '''
    计划管理主页
    :param request:
    :return:
    '''
    user = request.user
    if user.has_perm("repository.view_plan"):
        obj = models.Plan.objects.all()
        current_page = request.GET.get('p')
        page_obj = PaginationPlan(obj.count(), current_page)
        data_list = obj[page_obj.start():page_obj.end()]
        return render(request, 'backend/plan/index_plan.html', {'data': data_list, 'page_obj': page_obj})
    else:
        return render(request, 'backend/404.html')

@login_required
def del_plan(request):
    '''
    删除计划
    :param request:
    :return:
    '''
    nid = request.GET.get('nid')
    models.Plan.objects.filter(id=nid).delete()
    return redirect('index_plan')


@login_required
def add_plan(request):
    '''
    增加演出计划
    :param request:
    :return:
    '''
    if request.method == 'GET':
        obj = PlanForm()
        return render(request, 'backend/plan/add_plan.html', {'obj': obj})
    elif request.method == 'POST':
        obj = PlanForm(request.POST)
        if obj.is_valid():
            cinema = request.POST.get('plan_cinema')
            movie = request.POST.get('plan_movie')
            start_time = request.POST.get('plan_start_time')
            t = int(start_time)
            time_list = [(0, '2019-5-28 8:00:00'), (1, '2019-5-28 10:30:00'), (2, '2019-5-28 13:00:00'),
                         (3, '2019-5-28 15:30:00')]
            plan_start_time = time_list[t][1]
            end_time = request.POST.get('plan_end_time')
            models.Plan.objects.create(plan_cinema_id=cinema, plan_movie_id=movie, plan_end_time=end_time,
                                       plan_start_time=plan_start_time)
            return redirect('index_plan')
        else:
            return render(request, 'backend/plan/add_plan.html', {'obj': obj})


@login_required
def search_plan(request):
    '''
    以影厅名称查找该影厅计划
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'backend/plan/search_plan.html')
    elif request.method == 'POST':
        name = request.POST.get('search_plan')
        if models.Plan.objects.filter(plan_cinema__cinema_name=name).count():
            plan = models.Plan.objects.filter(plan_cinema__cinema_name=name)
            return render(request, 'backend/plan/search_plan.html', {'plan': plan})
        else:
            return render(request, 'backend/plan/search_plan.html')
