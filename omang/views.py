from django.shortcuts import render, redirect
from rest_framework import viewsets, generics
from .models import Omang
from .serializers import OmangSerializer
from .forms import OmangForm
from django.views import View

class OmangViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Omang.objects.all()
    serializer_class = OmangSerializer

    def get_queryset(self):
        id_number = self.request.query.params.get('ID_Number', None)
        if id_number is not None:
            return Omang.objects.filter(ID_Number=id_number)
        return super().get_queryset()

class OmangListCreateView(generics.ListCreateAPIView):
    queryset = Omang.objects.all()
    serializer_class = OmangSerializer

class OmangRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Omang.objects.all()
    serializer_class = OmangSerializer
    lookup_field = 'ID_Number'

def success_view(request):
    return render(request, 'success.html')
def home(request):
    return render(request, 'home.html')
def omang_list(request):
    omang_objects = Omang.objects.all()
    context = {'omang_objects': omang_objects}
    return render(request, 'omang_list.html', context)

class OmangCreateView(View):
    template_name = 'omang_create.html' # Create an HTML template for the form
    form_class = OmangForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') # Redirect to a success page or a different view
        return render(request, self.template_name, {'form': form})