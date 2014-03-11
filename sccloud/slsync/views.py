from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
from slsync.models import Inst
def index(request):
    all_inst_list = Inst.objects.all()
    template = loader.get_template('slsync/index.html')
    context = RequestContext(request, {'all_inst_list': all_inst_list,})
    return HttpResponse(template.render(context))
    return HttpResponse(output)

def detail(request, inst_id):
    return HttpResponse("you are looking for: "%inst_id)
