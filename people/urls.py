from django.urls import path

from .views import people_views as pv

urlpatterns = [
	path('', pv.home, name="index"),
	path('listar/', pv.listar, name="listar"),
	path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
	path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
	path('cadastrar/', pv.cadastrar, name="cadastrar"),
	path('cadastrar_departamento/', pv.cadastrar_departamento, name="cadastrar_departamento"),
	path('listar_dep/', pv.listar_dep, name="listar_dep"),
	path('detalhar_dep/<int:id_dep>/', pv.detalhar_dep, name="detalhar_dep"),
	path('excluir_dep/<int:id_dep>/', pv.excluir_dep, name="excluir_dep"),
	path('cadastrar_cargo/', pv.cadastrar_cargo, name="cadastrar_cargo"),
	path('listar_cargo/', pv.listar_cargo, name="listar_cargo"),
	path('detalhar_cargo/<int:id_cargo>/', pv.detalhar_cargo, name="detalhar_cargo"),
	path('excluir_cargo/<int:id_cargo>/', pv.excluir_cargo, name="excluir_cargo")
]
