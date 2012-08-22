# Create your views here.
from picman.models import Pic, PicForm

from django.shortcuts import render_to_response
from django.template import RequestContext

def form(request):
    if request.method == 'POST':
        form = PicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # TODO: return HttpResponseRedirect(Foo.get_absolute_url())
        else:
            pass # TODO: error
    else:
        form = PicForm()
    objs = Pic.objects.all()
    variables = RequestContext(request, { 'form' : form, 'objs' : objs })
    return render_to_response('index.html', variables)
