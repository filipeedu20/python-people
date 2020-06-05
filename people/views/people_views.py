from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


from ..models import Pessoa, Endereco, Departamento, Cargo

@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá, requisição feita com sucesso!")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	lista = Pessoa.objects.all()
	html = "<ul>"
	for p in lista:
		html+=f"<li>{p.nome} (id={p.id})</li>"
	html+= "</ul>"
	return HttpResponse(html)

def detalhar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	return HttpResponse(f"Detalhou {pessoa.nome} (id={pessoa.id})")

def excluir(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.delete()		
		return HttpResponse(f"Excluiu {pessoa.nome} (id={pessoa.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def cadastrar(request):
	p = Pessoa(nome="Matheus", idade=21)
	p.save()
	return HttpResponse(f"{p.nome} cadastrado com sucesso (id={p.id})")

def cadastrar_departamento(request):
	d = Departamento(nomeDep="Recursos Humanos")
	d.save()
	return HttpResponse(f"{d.nomeDep} Departamento cadastrado com sucesso (id={d.id})")

def listar_dep(request):
	lista = Departamento.objects.all()
	html = "<ul>"
	for p in lista:
		html+=f"<li>{p.nomeDep} (id={p.id})</li>"
	html+= "</ul>"
	return HttpResponse(html)

def detalhar_dep(request, id_dep):
	dep = Departamento.objects.get(id=id_dep)
	return HttpResponse(f"Detalhou Departamento: {dep.nomeDep} (id={dep.id})")

def excluir_dep(request, id_dep):
	try:
		dep = Departamento.objects.get(id=id_dep)
		dep.delete()		
		return HttpResponse(f"Excluiu {dep.nomeDep} (id={dep.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Departamento não encontrada")

def cadastrar_cargo(request):
	c = Cargo(nomeCargo="Analista Financeiro")
	c.save()
	return HttpResponse(f"{c.nomeCargo} Cargo cadastrado com sucesso (id={c.id})")

def detalhar_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	return HttpResponse(f"Detalhou Cargo: {cargo.nomeCargo} (id={cargo.id})")

def listar_cargo(request):
	lista = Cargo.objects.all()
	html = "<ul>"
	for p in lista:
		html+=f"<li>{p.nomeCargo} (id={p.id})</li>"
	html+= "</ul>"
	return HttpResponse(html)

def excluir_cargo(request, id_cargo):
	try:
		cargo = Cargo.objects.get(id=id_cargo)
		cargo.delete()		
		return HttpResponse(f"Excluiu {cargo.nomeCargo} (id={cargo.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Cargo não encontrado")