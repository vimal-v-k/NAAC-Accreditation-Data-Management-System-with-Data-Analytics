
from View.models import Details3_1_1, Citations

import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.shortcuts import render,redirect
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Sum
import numpy as np




def analysis(request):
    return render(request,'analystics/analyticspage.html')


def dept(request):
    return render(request,'analystics/department.html')

def fund(request):
    return render(request,'analystics/fundingagency.html')

def deptview(request):
    yeartype = request.POST.get('yeartypes')
    year = request.POST.get('years')

    if year and yeartype:
        if yeartype == "finantial":
            start_year = datetime.strptime(year+"-04-01", "%Y-%m-%d")
            end_year = start_year+relativedelta(years=+1, months=-1)
        elif yeartype == "academic":
            start_year = datetime.strptime(year+"-05-01", "%Y-%m-%d")
            end_year = start_year+relativedelta(years=+1, months=-1)
        else:
            return HttpResponse('Invalid year type selected')

        data = Details3_1_1.objects.filter(Year_of_Award__gte=start_year, Year_of_Award__lte=end_year)
        dept_amounts = {}
        for item in data:
            if item.Department_of_Principal_Investigator not in dept_amounts:
                dept_amounts[item.Department_of_Principal_Investigator] = item.Amount_Sanctioned
            else:
                dept_amounts[item.Department_of_Principal_Investigator] += item.Amount_Sanctioned

        # create pie chart
        labels = dept_amounts.keys()
        sizes = dept_amounts.values()
        fig, ax1 = plt.subplots(figsize=(18, 8))
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,textprops=dict(color='w'))
        ax1.axis('equal')
        plt.title('Contribution of Each Department ({0} - {1})'.format(start_year.strftime("%Y-%b"), end_year.strftime("%Y-%b")))
        ax1.legend(labels,loc='best')
        plt.tight_layout()

        # return chart as image response
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close(fig)
        response = HttpResponse(buffer.getvalue(), content_type='image/png')
        return response

    else:
        return HttpResponse('Fields are empty')




def fundingview(request):
    yeartype = request.POST.get('yeartypes')
    year = request.POST.get('years')

    if year and yeartype:
        if yeartype == "finantial":
            start_year = datetime.strptime(year+"-04-01", "%Y-%m-%d")
            end_year = start_year+relativedelta(years=+1, months=-1)
        elif yeartype == "academic":
            start_year = datetime.strptime(year+"-05-01", "%Y-%m-%d")
            end_year = start_year+relativedelta(years=+1, months=-1)
        else:
            return HttpResponse('Invalid year type selected')

        data = Details3_1_1.objects.filter(Year_of_Award__gte=start_year, Year_of_Award__lte=end_year)
        agency_amounts = {}
        for item in data:
            if item.Name_of_the_Funding_Agency not in agency_amounts:
                agency_amounts[item.Name_of_the_Funding_Agency] = item.Amount_Sanctioned
            else:
                agency_amounts[item.Name_of_the_Funding_Agency] += item.Amount_Sanctioned

        # create bar chart
        fig = Figure()
        ax1 = fig.add_subplot(111)
        x = agency_amounts.keys()
        y = agency_amounts.values()
        ax1.bar(x, y)
        plt.xticks(rotation=90)
        ax1.set_title('Amount Sanctioned by Each Funding Agency ({0} - {1})'.format(start_year.strftime("%Y-%b"), end_year.strftime("%Y-%b")))
        ax1.set_xlabel('Agencies')
        ax1.set_ylabel('Amount Sanctioned')
        plt.tight_layout()

        # return chart as image response
        canvas = FigureCanvas(fig)
        buffer = BytesIO()
        canvas.print_png(buffer)
        plt.close(fig)
        response = HttpResponse(buffer.getvalue(), content_type='image/png')
        return response

    else:
        return HttpResponse('Fields are empty')


def totalamount_view(request):
    if request.method == 'POST':
        year = request.POST.get('years')
        total_amount = Details3_1_1.objects.filter(Year_of_Award__year=year).aggregate(Sum('Amount_Sanctioned'))['Amount_Sanctioned__sum']
        context = {'year': year, 'total_amount': total_amount}
        return render(request, 'analystics/totalamountview.html', context)
    else:
        return render(request, 'analystics/totalamount.html')

def citations_by_department(request):
    departments = ["Automobile Engineering", "Basic Science and Humanities", "Civil Engineering", "Computer Science & Engineering", "Electrical & Electronics Engineering", "Electronics & Communication Engineering", "Mechanical Engineering"]
    data = []
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i, department in enumerate(departments):
        citations_by_year = []
        for year in ["2018", "2019", "2020", "2021", "2022", "2023"]:
            queryset = Citations.objects.filter(Department=department, year=year)
            total_citations = queryset.aggregate(Sum('Citations'))['Citations__sum'] or 0
            citations_by_year.append(total_citations)
        data.append({'department': department, 'citations_by_year': citations_by_year, 'color': colors[i]})

    # create line chart
    fig = Figure(figsize=(18, 8))
    ax1 = fig.add_subplot(111)
    for d in data:
        x = ["2018", "2019", "2020", "2021", "2022", "2023"]
        y = d['citations_by_year']
        ax1.plot(x, y, label=d['department'], color=d['color'])
    ax1.set_title('Number of Citations by Department')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Citations')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

    # adjust plot area and legend position
    fig.subplots_adjust(right=0.8)
    ax1.set_position([0.1, 0.1, 0.7, 0.8])
    legend = ax1.legend()
    legend.set_bbox_to_anchor((1.2, 0.5))

    # return chart as image response
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)
    response = HttpResponse(buffer.getvalue(), content_type='image/png')
    return response

#
# def citations_by_staff(request):
#     return render(request, 'analystics/citations.html')
#
#
# def staffsearch(request):
#     query = request.GET['name']
#     stdata = Citations.objects.filter(Name__icontains=query)
#     return render(request,'analystics/citations.html',{'stdata': stdata})
#
# #
#
# def staffgraph(request,name):
#     srdta = Citations.objects.get(Name=name)
#     print(srdta)
#     # Extract the years and citation counts from the data
#     years = [srdta.year]
#     citations = [srdta.Citations]
#
#     # Create a line plot of the citation counts over time
#     plt.plot(years, citations)
#     plt.xlabel('Year')
#     plt.ylabel('Citations')
#     plt.title(f'Citation Count for {srdta.Name}')
#
#     # Create a buffer for the image
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#
#     # Return the image as an HTTP response
#     return HttpResponse(buffer.getvalue(), content_type='image/png')
#
#
from django.shortcuts import render
from django.db.models import Sum
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def citations_by_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
        queryset = Citations.objects.filter(Name__icontains=name)
    else:
        queryset = Citations.objects.all()

    data = []
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    names = set(queryset.values_list('Name', flat=True))
    for i, name in enumerate(names):
        citations_by_year = []
        for year in ["2018", "2019", "2020", "2021", "2022", "2023"]:
            year_queryset = queryset.filter(Name=name, year=year)
            total_citations = year_queryset.aggregate(Sum('Citations'))['Citations__sum'] or 0
            citations_by_year.append(total_citations)
        data.append({'name': name, 'citations_by_year': citations_by_year, 'color': colors[i % len(colors)]})

    fig = Figure(figsize=(18, 8))
    ax1 = fig.add_subplot(111)
    for d in data:
        x = ["2018", "2019", "2020", "2021", "2022", "2023"]
        y = d['citations_by_year']
        ax1.plot(x, y, label=d['name'], color=d['color'])
    ax1.set_title('Number of Citations by Name')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Citations')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

    fig.subplots_adjust(right=0.8)
    ax1.set_position([0.1, 0.1, 0.7, 0.8])
    legend = ax1.legend()
    legend.set_bbox_to_anchor((1.2, 0.5))

    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)
    response = HttpResponse(buffer.getvalue(), content_type='image/png')
    return response


def search_citations_by_name(request):
    return render(request, 'analystics/citations.html')



