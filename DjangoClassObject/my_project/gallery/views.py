from django.shortcuts import render,HttpResponse
from .forms import Image,ImageForm
from django.views.generic import ListView

# Create your views here.
def gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = ImageForm()
    return render(request, "gallery.html", {"form": form})


class ShowImg(ListView):
    model = Image
    template_name  ="viewimage.html"