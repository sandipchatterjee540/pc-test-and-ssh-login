from django.shortcuts import render
from django.http import HttpResponse
from . import check_disc

# Create your views here.
def disk(request):
    chd=check_disc.disc_use()
    chd["mem"]=check_disc.mem_use()
    return render(request,'disk_use.html',chd)

def ram(request):
    mem=check_disc.mem_use()
    #mem["mem"]=check_disc.mem_use()
    return render(request,'mem.html', mem)
