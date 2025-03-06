from django.urls import path
from analystics import views



urlpatterns = [
    path('dept/', views.dept, name='dept'),
    path('analytics/', views.analysis, name='analytics'),
    path('funding/', views.fund, name='funding'),
    path('deptview/', views.deptview, name='deptview'),
    path('fundingview/', views.fundingview, name='fundingview'),
    path('totalamount/',views.totalamount_view, name='totalamount_view'),
    path('deptcitations/', views.citations_by_department, name='deptcitations'),
    # path('staffcitations/', views.citations_by_staff, name='staffcitations'),
    # path('staffsearch/', views.staffsearch, name='staffsearch'),
    # path('staffgrapgh/<str:name>/', views.staffgraph, name='staffgraph'),
    path('citations_by_name/', views.citations_by_name, name='citations_by_name'),
    path('search_citations_by_name/', views.search_citations_by_name, name='search_citations_by_name'),

]
