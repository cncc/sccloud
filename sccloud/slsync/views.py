from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404

# Create your views here.
from slsync.models import Inst
def index(request):
    all_inst_list = Inst.objects.all()
    template = loader.get_template('slsync/index.html')
    context = RequestContext(request, {'all_inst_list': all_inst_list,})
    return HttpResponse(template.render(context))

def detail(request, inst_id):
    inst_detail = get_object_or_404(Inst,pk=inst_id)
    return render(request,'slsync/detail.html',{'inst': inst_detail})
