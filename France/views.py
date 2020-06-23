from django.shortcuts import render
from django.utils.translation import ugettext as _

# Create your views here.
def index(request):
    data = {
        'title': _('Petnet Direct')
    }
    return render(request, 'Welcome.html', data)