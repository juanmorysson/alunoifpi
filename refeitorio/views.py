from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def inicio(request):
    return render(request, 'refeitorio/index.html')

# CLASSSSSSSSSSSS.
def aluno_list(request):
    if not request.user.has_perm('aluno.list_aluno'):
        raise PermissionDenied
    alunos = Aluno.objects.all()
    return render(request, 'refeitorio/aluno_list.html', {'alunos': alunos})

def aluno_detail(request, pk):
    if not request.user.has_perm('aluno.view_aluno'):
        raise PermissionDenied
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'refeitorio/aluno_detail.html', {'aluno': aluno})
    
def aluno_new(request):
    if not request.user.has_perm('aluno.add_aluno'):
        raise PermissionDenied
    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.save()
            return redirect('aluno_detail', pk=aluno.pk)
    else:
        form = AlunoForm()
    return render(request, 'refeitorio/aluno_edit.html', {'form': form})
    
def aluno_edit(request, pk):
    if not request.user.has_perm('aluno.change_aluno'):
        raise PermissionDenied
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.save()
            return redirect('aluno_detail', pk=aluno.pk)
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'refeitorio/aluno_edit.html', {'form': form})
    
def aluno_remove(request, pk):
    if not request.user.has_perm('aluno.delete_aluno'):
        raise PermissionDenied
    aluno = get_object_or_404(Aluno, pk=pk)
    aluno.delete()
    return redirect('aluno_list')   


# CLASSSSSSSSSSSS.
def curso_list(request):
    if not request.user.has_perm('aluno.list_curso'):
        raise PermissionDenied
    cursos = Curso.objects.all()
    return render(request, 'refeitorio/curso_list.html', {'cursos': cursos})

def curso_detail(request, pk):
    if not request.user.has_perm('aluno.view_curso'):
        raise PermissionDenied
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'refeitorio/curso_detail.html', {'curso': curso})
    
def curso_new(request):
    if not request.user.has_perm('aluno.add_curso'):
        raise PermissionDenied
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            return redirect('curso_detail', pk=curso.pk)
    else:
        form = CursoForm()
    return render(request, 'refeitorio/curso_edit.html', {'form': form})
    
def curso_edit(request, pk):
    if not request.user.has_perm('aluno.change_curso'):
        raise PermissionDenied
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            return redirect('curso_detail', pk=curso.pk)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'refeitorio/curso_edit.html', {'form': form})
    
def curso_remove(request, pk):
    if not request.user.has_perm('aluno.delete_curso'):
        raise PermissionDenied
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('curso_list')   


# CLASSSSSSSSSSSS.
def turno_list(request):
    if not request.user.has_perm('aluno.list_turno'):
        raise PermissionDenied
    turnos = Turno.objects.all()
    return render(request, 'refeitorio/turno_list.html', {'turnos': turnos})

def turno_detail(request, pk):
    if not request.user.has_perm('aluno.view_turno'):
        raise PermissionDenied
    turno = get_object_or_404(Turno, pk=pk)
    return render(request, 'refeitorio/turno_detail.html', {'turno': turno})
    
def turno_new(request):
    if not request.user.has_perm('aluno.add_turno'):
        raise PermissionDenied
    if request.method == "POST":
        form = TurnoForm(request.POST, request.FILES)
        if form.is_valid():
            turno = form.save(commit=False)
            turno.save()
            return redirect('turno_detail', pk=turno.pk)
    else:
        form = TurnoForm()
    return render(request, 'refeitorio/turno_edit.html', {'form': form})
    
def turno_edit(request, pk):
    if not request.user.has_perm('aluno.change_turno'):
        raise PermissionDenied
    turno = get_object_or_404(Turno, pk=pk)
    if request.method == "POST":
        form = TurnoForm(request.POST, request.FILES, instance=turno)
        if form.is_valid():
            turno = form.save(commit=False)
            turno.save()
            return redirect('turno_detail', pk=turno.pk)
    else:
        form = TurnoForm(instance=turno)
    return render(request, 'refeitorio/turno_edit.html', {'form': form})
    
def turno_remove(request, pk):
    if not request.user.has_perm('aluno.delete_turno'):
        raise PermissionDenied
    turno = get_object_or_404(Turno, pk=pk)
    turno.delete()
    return redirect('turno_list')   


# CLASSSSSSSSSSSS.
def turma_list(request):
    if not request.user.has_perm('aluno.list_turma'):
        raise PermissionDenied
    turmas = Turma.objects.all()
    return render(request, 'refeitorio/turma_list.html', {'turmas': turmas})

def turma_detail(request, pk):
    if not request.user.has_perm('aluno.view_turma'):
        raise PermissionDenied
    turma = get_object_or_404(Turma, pk=pk)
    return render(request, 'refeitorio/turma_detail.html', {'turma': turma})
    
def turma_new(request):
    if not request.user.has_perm('aluno.add_turma'):
        raise PermissionDenied
    if request.method == "POST":
        form = TurmaForm(request.POST, request.FILES)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.save()
            return redirect('turma_detail', pk=turma.pk)
    else:
        form = TurmaForm()
    return render(request, 'refeitorio/turma_edit.html', {'form': form})
    
def turma_edit(request, pk):
    if not request.user.has_perm('aluno.change_turma'):
        raise PermissionDenied
    turma = get_object_or_404(Turma, pk=pk)
    if request.method == "POST":
        form = TurmaForm(request.POST, request.FILES, instance=turma)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.save()
            return redirect('turma_detail', pk=turma.pk)
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'refeitorio/turma_edit.html', {'form': form})
    
def turma_remove(request, pk):
    if not request.user.has_perm('aluno.delete_turma'):
        raise PermissionDenied
    turma = get_object_or_404(Turma, pk=pk)
    turma.delete()
    return redirect('turma_list')   


# CLASSSSSSSSSSSS.
def servidor_list(request):
    if not request.user.has_perm('aluno.list_servidor'):
        raise PermissionDenied
    servidors = Servidor.objects.all()
    return render(request, 'refeitorio/servidor_list.html', {'servidors': servidors})

def servidor_detail(request, pk):
    if not request.user.has_perm('aluno.view_servidor'):
        raise PermissionDenied
    servidor = get_object_or_404(Servidor, pk=pk)
    return render(request, 'refeitorio/servidor_detail.html', {'servidor': servidor})
    
def servidor_new(request):
    if not request.user.has_perm('aluno.add_servidor'):
        raise PermissionDenied
    if request.method == "POST":
        form = ServidorForm(request.POST, request.FILES)
        if form.is_valid():
            servidor = form.save(commit=False)
            servidor.save()
            return redirect('servidor_detail', pk=servidor.pk)
    else:
        form = ServidorForm()
    return render(request, 'refeitorio/servidor_edit.html', {'form': form})
    
def servidor_edit(request, pk):
    if not request.user.has_perm('aluno.change_servidor'):
        raise PermissionDenied
    servidor = get_object_or_404(Servidor, pk=pk)
    if request.method == "POST":
        form = ServidorForm(request.POST, request.FILES, instance=servidor)
        if form.is_valid():
            servidor = form.save(commit=False)
            servidor.save()
            return redirect('servidor_detail', pk=servidor.pk)
    else:
        form = ServidorForm(instance=servidor)
    return render(request, 'refeitorio/servidor_edit.html', {'form': form})
    
def servidor_remove(request, pk):
    if not request.user.has_perm('aluno.delete_servidor'):
        raise PermissionDenied
    servidor = get_object_or_404(Servidor, pk=pk)
    servidor.delete()
    return redirect('servidor_list')   


# CLASSSSSSSSSSSS.
def refeicao_list(request):
    if not request.user.has_perm('aluno.list_refeicao'):
        raise PermissionDenied
    refeicaos = Refeicao.objects.all()
    return render(request, 'refeitorio/refeicao_list.html', {'refeicaos': refeicaos})

def refeicao_detail(request, pk):
    if not request.user.has_perm('aluno.view_refeicao'):
        raise PermissionDenied
    refeicao = get_object_or_404(Refeicao, pk=pk)
    return render(request, 'refeitorio/refeicao_detail.html', {'refeicao': refeicao})
    
def refeicao_new(request):
    if not request.user.has_perm('aluno.add_refeicao'):
        raise PermissionDenied
    if request.method == "POST":
        form = RefeicaoForm(request.POST, request.FILES)
        if form.is_valid():
            refeicao = form.save(commit=False)
            refeicao.save()
            return redirect('refeicao_detail', pk=refeicao.pk)
    else:
        form = RefeicaoForm()
    return render(request, 'refeitorio/refeicao_edit.html', {'form': form})
    
def refeicao_edit(request, pk):
    if not request.user.has_perm('aluno.change_refeicao'):
        raise PermissionDenied
    refeicao = get_object_or_404(Refeicao, pk=pk)
    if request.method == "POST":
        form = RefeicaoForm(request.POST, request.FILES, instance=refeicao)
        if form.is_valid():
            refeicao = form.save(commit=False)
            refeicao.save()
            return redirect('refeicao_detail', pk=refeicao.pk)
    else:
        form = RefeicaoForm(instance=refeicao)
    return render(request, 'refeitorio/refeicao_edit.html', {'form': form})
    
def refeicao_remove(request, pk):
    if not request.user.has_perm('aluno.delete_refeicao'):
        raise PermissionDenied
    refeicao = get_object_or_404(Refeicao, pk=pk)
    refeicao.delete()
    return redirect('refeicao_list')   


# CLASSSSSSSSSSSS.
def tipoRefeicao_list(request):
    if not request.user.has_perm('aluno.list_tipoRefeicao'):
        raise PermissionDenied
    tipoRefeicaos = TipoRefeicao.objects.all()
    return render(request, 'refeitorio/tipoRefeicao_list.html', {'tipoRefeicaos': tipoRefeicaos})

def tipoRefeicao_detail(request, pk):
    if not request.user.has_perm('aluno.view_tipoRefeicao'):
        raise PermissionDenied
    tipoRefeicao = get_object_or_404(TipoRefeicao, pk=pk)
    return render(request, 'refeitorio/tipoRefeicao_detail.html', {'tipoRefeicao': tipoRefeicao})
    
def tipoRefeicao_new(request):
    if not request.user.has_perm('aluno.add_tipoRefeicao'):
        raise PermissionDenied
    if request.method == "POST":
        form = TipoRefeicaoForm(request.POST, request.FILES)
        if form.is_valid():
            tipoRefeicao = form.save(commit=False)
            tipoRefeicao.save()
            return redirect('tipoRefeicao_detail', pk=tipoRefeicao.pk)
    else:
        form = TipoRefeicaoForm()
    return render(request, 'refeitorio/tipoRefeicao_edit.html', {'form': form})
    
def tipoRefeicao_edit(request, pk):
    if not request.user.has_perm('aluno.change_tipoRefeicao'):
        raise PermissionDenied
    tipoRefeicao = get_object_or_404(TipoRefeicao, pk=pk)
    if request.method == "POST":
        form = TipoRefeicaoForm(request.POST, request.FILES, instance=tipoRefeicao)
        if form.is_valid():
            tipoRefeicao = form.save(commit=False)
            tipoRefeicao.save()
            return redirect('tipoRefeicao_detail', pk=tipoRefeicao.pk)
    else:
        form = TipoRefeicaoForm(instance=tipoRefeicao)
    return render(request, 'refeitorio/tipoRefeicao_edit.html', {'form': form})
    
def tipoRefeicao_remove(request, pk):
    if not request.user.has_perm('aluno.delete_tipoRefeicao'):
        raise PermissionDenied
    tipoRefeicao = get_object_or_404(TipoRefeicao, pk=pk)
    tipoRefeicao.delete()
    return redirect('tipoRefeicao_list')   


# CLASSSSSSSSSSSS.
def reserva_list(request):
    if not request.user.has_perm('aluno.list_reserva'):
        raise PermissionDenied
    reservas = Reserva.objects.all()
    return render(request, 'refeitorio/reserva_list.html', {'reservas': reservas})

def reserva_detail(request, pk):
    if not request.user.has_perm('aluno.view_reserva'):
        raise PermissionDenied
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'refeitorio/reserva_detail.html', {'reserva': reserva})
    
def reserva_new(request):
    if not request.user.has_perm('aluno.add_reserva'):
        raise PermissionDenied
    if request.method == "POST":
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.save()
            return redirect('reserva_detail', pk=reserva.pk)
    else:
        form = ReservaForm()
    return render(request, 'refeitorio/reserva_edit.html', {'form': form})
    
def reserva_edit(request, pk):
    if not request.user.has_perm('aluno.change_reserva'):
        raise PermissionDenied
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ReservaForm(request.POST, request.FILES, instance=reserva)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.save()
            return redirect('reserva_detail', pk=reserva.pk)
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'refeitorio/reserva_edit.html', {'form': form})
    
def reserva_remove(request, pk):
    if not request.user.has_perm('aluno.delete_reserva'):
        raise PermissionDenied
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.delete()
    return redirect('reserva_list')   