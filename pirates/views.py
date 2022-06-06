from django.shortcuts import render
from django.views import View
from datetime import date
from django import forms
from django.urls.base import reverse
from django.http import HttpResponseRedirect
from .models import *
from django.shortcuts import redirect

class listar_tesouros(View):
   def get(self, request):
       tesouros = Tesouro.objects.all()
       valor_geral = 0
       for tesouro in tesouros:
           valor_geral = valor_geral + tesouro.valor_total
       return render(request, 'lista_tesouros.html', {"tesouros":tesouros, "valor_geral": valor_geral})
   
class TesouroForm(forms.ModelForm):
    class Meta:
        model = Tesouro
        fields = ['nome', 'quantidade', 'preco']
        labels = {"nome":"Nome do Tesouro", "quantidade":"Quantidade de Tesouros","preco":"Preco do tesouro"}

class salvar_tesouro(View):
    def get(self, request, id=None): 
        form = TesouroForm(request.POST, request.FILES)
        return render(request, "salvar_tesouro.html", {"form": form})
    
    def post(self, request, id=None):
        tesouro = Tesouro.objects.get(id=id) if id != None else None
        form = TesouroForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listar_tesouros'))
        else:
            return render(request,"salvar_tesouro.html",{"form":form})
        
        
class editar_tesouro(View):
    def get(self, request, id):
        tesouro = Tesouro.objects.get(id=id)
        form = TesouroForm(instance=tesouro)
        return render(request,"salvar_tesouro.html",{"form":form, "tesouro": tesouro})
    
    def post(self, request, id):
        tesouro = Tesouro.objects.get(id=id)
        form = TesouroForm(request.POST ,instance=tesouro)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listar_tesouros'))
        else:
            return render(request,"salvar_tesouro.html",{"form":form, "tesouro": tesouro})

class excluir_tesouros(View):
    def get(self, request, id):
        tesouro = Tesouro.objects.get(id=id)
        return render(request, "excluir_tesouro.html",{'tesouro':tesouro})
    def post(self, request, id):
        tesouro = Tesouro.objects.get(id=id)
        if request.method == "POST":
            tesouro.delete()
            return redirect('listar_tesouros')
        else:
            return render(request, "excluir_tesouro.html",{'tesouro':tesouro})