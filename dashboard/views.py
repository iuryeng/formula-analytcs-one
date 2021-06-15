from django.shortcuts import render
from .models import Pilotos, Corridas, Circuitos


# Create your views here.

def index(request):
    return render(request, 'index.html')


def detalhe_pilotos(request, pk):
    pilotos = Pilotos.objects.get(pk=pk)
    pilotos_quantidade = Pilotos.objects.all()
    context = {
        'sobrenome': pilotos.ultimo_nome,
        'nome': pilotos.primeiro_nome,
        'referencia': pilotos.ref_piloto,
        'nascimento': pilotos.nascimento,
        'nacionalidade': pilotos.nacionalidade_piloto,
        'total': pilotos_quantidade.count,
    }
    return render(request, 'pilotos.html', context)


def detalhe_corridas(request, pk):
    corridas = Corridas.objects.get(pk=pk)
    corrida_fk = corridas.id_circuito;
    corridas_quantidade = Corridas.objects.all()
    context = {
        'ano': corridas.ano_corrida,
        'nome_circuito': corrida_fk.nome_circuito,
        'rodada': corridas.rodada,
        'nome': corridas.nome_corrida,
        'data': corridas.data_corrida,
        'tempo': corridas.tempo_corrida,
        'total': corridas_quantidade.count
    }
    return render(request, 'corridas.html', context)


def detalhe_piloto_por_nome(request, nome):
    pilotos = Pilotos.objects.get(primeiro_nome=nome)
    pilotos_quantidade = Pilotos.objects.all()
    context = {
        'sobrenome': pilotos.ultimo_nome,
        'nome': pilotos.primeiro_nome,
        'referencia': pilotos.ref_piloto,
        'nascimento': pilotos.nascimento,
        'nacionalidade': pilotos.nacionalidade_piloto,
        'total': pilotos_quantidade.count

    }
    return render(request, 'pilotos.html', context)

def pilotos(request):
    pilotos= Pilotos.objects.all()
    context = {
        'pilotos': pilotos
    }
    return render(request, 'pilotos.html', context)


