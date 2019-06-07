from django.shortcuts import render, redirect, HttpResponse
from repository import models
from repository.forms.forms import MovieForm
from backend.pager import PaginationMovie
from django.contrib.auth.decorators import login_required


@login_required
def index_movie(request):
    '''
    影片管理主页
    :param request:
    :return:
    '''
    user = request.user
    if user.has_perm("repository.view_movie"):
        obj = models.Movie.objects.all()
        current_page = request.GET.get('p')
        page_obj = PaginationMovie(obj.count(), current_page)
        data_list = obj[page_obj.start():page_obj.end()]
        return render(request, 'backend/movie/index_movie.html', {'data': data_list, 'page_obj': page_obj})
    else:
        return render(request, 'backend/404.html')


def del_movie(request):
    '''
    删除电影
    :param request:
    :return:
    '''
    nid = request.GET.get('nid')
    models.Movie.objects.filter(id=nid).delete()
    return redirect('index_movie')


@login_required
def add_movie(request):
    '''
    增加电影
    :param request:
    :return:
    '''
    if request.method == 'GET':
        obj = MovieForm()
        return render(request, 'backend/movie/add_movie.html', {'obj': obj})
    elif request.method == 'POST':
        obj = MovieForm(request.POST)
        if obj.is_valid():
            name = obj.cleaned_data.get('movie_name')
            detail = obj.cleaned_data.get('movie_detail')
            price = obj.cleaned_data.get('movie_price')
            models.Movie.objects.create(movie_name=name, movie_detail=detail, movie_price=price)
            return redirect('index_movie')
        else:
            return render(request, 'backend/movie/add_movie.html', {'obj': obj})


@login_required
def edit_movie(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        movie_list = models.Movie.objects.filter(id=nid).first()
        return render(request, 'backend/movie/edit_movie.html',
                      {'movie_list': movie_list, 'error_name': '注意：影片名称不能重复，且长度不能大于20'})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        name = request.POST.get('movie_name')
        detail = request.POST.get('movie_detail')
        price = request.POST.get('movie_price')
        movie_list = models.Movie.objects.filter(id=nid).first()
        n = models.Movie.objects.filter(id=nid).first().movie_name
        if name != n:
            if models.Movie.objects.filter(movie_name=name).count() or len(n) > 20:
                return render(request, 'backend/movie/edit_movie.html',
                              {'movie_list': movie_list, 'error_name': '影片名称输入错误'})
            elif len(detail) >= 50:
                return render(request, 'backend/movie/edit_movie.html',
                              {'movie_list': movie_list, 'error_detail': '影片描述长度不能超过50'})
        else:
            if len(detail) >= 50:
                return render(request, 'backend/movie/edit_movie.html',
                              {'movie_list': movie_list, 'error_detail': '影片描述长度不能超过50'})
            models.Movie.objects.filter(id=nid).update(movie_name=name, movie_detail=detail, movie_price=price)
            return redirect('index_movie')


@login_required
def search_movie(request):
    '''
    搜索影片
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'backend/movie/search_movie.html')

    elif request.method == 'POST':
        name = request.POST.get('search_movie')
        if models.Movie.objects.filter(movie_name=name).count():
            movie = models.Movie.objects.filter(movie_name=name).values()
            return render(request, 'backend/movie/search_movie.html', {'movie': movie})
        else:
            return render(request, 'backend/movie/search_movie.html')
