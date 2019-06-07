from django.conf.urls import url
from backend.views import login_views as v0
from backend.views import cinema_views as v1
from backend.views import seat_views as v2
from backend.views import movie_views as v3
from backend.views import plan_views as v4
from backend.views import ticket_views as v5

urlpatterns = [

    url(r'^index/', v1.index, name='index'),
    url(r'^del_cinema/', v1.del_cinema, name='del_cinema'),
    url(r'^edit_cinema/', v1.edit_cinema, name='edit_cinema'),
    url(r'^search_cinema/', v1.search_cinema, name='search_cinema'),
    url(r'^add_cinema/', v1.add_cinema, name='add_cinema'),

    url(r'^index_seat/', v2.index_seat, name='index_seat'),
    url(r'^del_seat/', v2.del_seat, name='del_seat'),
    url(r'^search_seat/', v2.search_seat, name='search_seat'),

    url(r'^index_movie/', v3.index_movie, name='index_movie'),
    url(r'^del_movie/', v3.del_movie, name='del_movie'),
    url(r'^add_movie/', v3.add_movie, name='add_movie'),
    url(r'^edit_movie/', v3.edit_movie, name='edit_movie'),
    url(r'^search_movie/', v3.search_movie, name='search_movie'),
    url(r'^search_movie/', v3.search_movie, name='search_movie'),

    url(r'^index_plan/', v4.index_plan, name='index_plan'),
    url(r'^del_plan/', v4.del_plan, name='del_plan'),
    url(r'^add_plan/', v4.add_plan, name='add_plan'),
    url(r'^search_plan/', v4.search_plan, name='search_plan'),

    url(r'^index_ticket', v5.index_ticket, name='index_ticket'),
    url(r'^del_ticket', v5.del_ticket, name='del_ticket'),
    url(r'^add_ticket', v5.add_ticket, name='add_ticket'),
    url(r'^search_ticket', v5.search_ticket, name='search_ticket'),
    url(r'^login/$', v0.do_login, name='login'),
    url(r'^logout/$', v0.do_logout, name='logout'),
]
