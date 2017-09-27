from django.shortcuts import render
from .models import Image
from .forms import UploadForm

# Create your views here.

def get_all_images():
    ret = []
    images = Image.objects.all()
    for img in images:
        print(img.docfile.url)
        ret.append(str(img.docfile.url).replace('/nfs/2013/c/cdivry/DJANGO/d08/media', ''))
        print(img.docfile.url)
    return (ret)

def upload(request):

    form = UploadForm()
    img = None
    images = get_all_images()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        print("LOL !")
        if form.is_valid():
            print("LOL @")
            img = Image(docfile=request.FILES['docfile'])
            img.save()
            images = get_all_images()
            return render(request, 'ex00/upload.html', {'images': images, 'form': form, 'uploaded': True })
    print("LOL #")
    return render(request, 'ex00/upload.html', {'images': images, 'form': form })
