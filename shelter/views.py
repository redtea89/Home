from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from shelter.models import Shelter
from django.contrib.auth.models import User
from django.views import generic

class ShelterView(generic.View):
    def get(self, request):
        num_shelters = Shelter.objects.count()
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        context = {
        'num_shelters': num_shelters,
        'num_visits': num_visits,
    }
        return render(request, 'shelter/shelter.html', context)
    def post(self, request):
        return HttpResponseRedirect("/shelter/region/"+str(request.POST['search']))

class ShelterListView(generic.ListView):
    model = Shelter  #이건 아래 두 줄의 축약임
    # context_object_name = 'object_list'
    # queryset = Shelter.objects.all()
    def get_queryset(self):
        return Shelter.objects.filter(address__contains="강남")
    def get_context_data(self, **kwargs):
        context = super(ShelterListView, self).get_context_data(**kwargs)
        context['some_data'] = "This is just some data"
        return context

class ShelterDetailView(generic.DetailView):
    context_object_name = 'shelters'
    queryset = Shelter.objects.all()

def region_shelter(request, region):
    context = {}
    if request.method=='POST':
        return HttpResponseRedirect("/shelter/region/"+str(request.POST['search']))
    data1 = Shelter.objects.filter(address__contains=f'{region}')
    data2 = Shelter.objects.filter(address2__contains=f'{region}')
    data = data1 | data2
    count = data.count()
    context['data'] = data
    context['region'] = region
    context['count'] = count
    return render(request, 'shelter/region.html',context)

def detail_shelter(request, shelter_id):
    context = {}
    data = Shelter.objects.get(id=shelter_id)
    context['data'] = data
    return render(request, 'shelter/detail.html',context)

@login_required(login_url='/accounts/login/')
def upload(request):
    if request.method=='POST':
        name = request.POST['name']
        address = request.POST['address']
        try:
            request.POST['pet']
            pet = True
        except:
            pet = False
        people = int(request.POST['people'])
        user = User.objects.get(id = request.user.id)
        post = Shelter(name=name,address=address,pet=pet,people=people,user=user)
        post.save()
    return render(request, 'shelter/upload.html')

# def manage_shelter(request,shelter_id):
#     context = {}
#     data = Shelter.objects.get(pk=shelter_id)
#     context['data'] = data
#     return render(request, 'shelter/manage_shelter.html',context)

# def update_shelter(request,shelter_id):
#     context={}
#     data = Shelter.objects.get(pk=shelter_id)
#     if request.method == 'POST':
#         data.toilet = request.POST['toilet']
#         try:  #pet을 체크하지 않는 경우 POST['pet']값이 null이라 에러가 뜨는 상황 예외처리
#             if request.POST['pet'] == 'on':
#                 data.pet = True 
#         except:
#             data.pet = False
#         data.save()
#         return HttpResponseRedirect('/shelter/'+str(data.id))
#     context['data'] = data
#     return render(request, 'shelter/update_shelter.html',context)