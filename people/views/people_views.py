from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from ..models import Pessoa, Endereco, Departamento, Cargo
@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá, requisição feita com sucesso!")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	result = Pessoa.objects.all()
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	context = {'pessoa':pessoa}
	return render(request, 'detalhe.html', context)

def excluir(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.delete()		
		return HttpResponse(f"Excluiu {pessoa.nome} (id={pessoa.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

	def cadastro(request):
		sexos = ['Masculino','Feminino']
		template = loader.get_template('cadastrar.html')
		context = {
			'sexos': sexos,
		}
		return HttpResponse(template.render(context, request))

def cadastrar(request):
	dtNascimento = datetime.strptime(request.POST['dtNascimento'], "%d/%m/%Y").date()
	p = Pessoa.objects.nova(request.POST['nome'],
			request.POST['idade'],
			dtNascimento,
			request.POST['cpf'],
			request.POST['logradouro'],
			request.POST['numero'],
			request.POST['bairro'],
			request.POST['cep'])

	return HttpResponse(f"{p} cadastrado com sucesso")

def alterar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	context = {'pessoa':pessoa}
	return render(request, 'editar.html', context)

@csrf_exempt
@require_http_methods(["POST","GET"])
def salvar_alt(request):
	p = Pessoa.objects.salvar_alt(
			request.POST['id'],
			request.POST['nome'],
			request.POST['idade'],
			request.POST['cpf'])
	return HttpResponse(f"{p} alterado com sucesso")
## Manipulação de departamento 
def cadastrar_departamento(request):
	d = Departamento(nomeDep="Recursos Humanos")
	d.save()
	return HttpResponse(f"{d.nomeDep} Departamento cadastrado com sucesso (id={d.id})")

def listar_dep(request):
	result = Departamento.objects.all()
	template = loader.get_template('listar_departamento.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar_dep(request, id_dep):
	dep = Departamento.objects.get(id=id_dep)
	context = {'dep':dep}
	return render(request, 'detalhe_dep.html', context)

def excluir_dep(request, id_dep):
	try:
		dep = Departamento.objects.get(id=id_dep)
		dep.delete()		
		return HttpResponse(f"Excluiu {dep.nomeDep} (id={dep.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Departamento não encontrado")


# Manipulação de Cargos
def cadastrar_cargo(request):
	template = loader.get_template('cadastrar_cargo.html')
	context = {}
	return HttpResponse(template.render(context, request))

def salvar_cargo(request):
	c = Cargo(nomeCargo = request.POST['nomeCargo'],descricaoCargo = request.POST['descricaoCargo'])
	c.save()
	return HttpResponse(f"{c} Cargo cadastrado com sucesso")

def detalhar_cargo(request, id_cargo):
	result = Cargo.objects.get(id=id_cargo)
	template = loader.get_template('detalhar_cargo.html')
	context = {
		'cargo' : result,
	}
	return HttpResponse(template.render(context, request))

def alterar_cargo(request,id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	context = {'cargo':cargo}
	return render(request, 'editar_cargo.html', context)
	
def listar_cargo(request):
	result = Cargo.objects.all()
	template = loader.get_template('listar_cargo.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def excluir_cargo(request, id_cargo):
	try:
		cargo = Cargo.objects.get(id=id_cargo)
		cargo.delete()		
		return HttpResponse(f"Excluiu {cargo.nomeCargo} (id={cargo.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Cargo não encontrado")

@csrf_exempt
@require_http_methods(["POST","GET"])
def salva_alt_cargo(request):
	c = Cargo.objects.get(id=request.POST['id'])
	c.nomeCargo 		= request.POST['nomeCargo']
	c.descricaoCargo 	= request.POST['descricaoCargo']
	c.save()
	return HttpResponse("Cargo alterado com sucesso!")