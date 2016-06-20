from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
import time
from datetime import datetime, timedelta
from django.core.cache import cache
from django.db.models import Q
from core.models import Line
from django.conf import settings


URL = 'https://api.inthegra.strans.teresina.pi.gov.br/v1/'


def check_token():
    """
        { codigo token expirado
        "code": 108,
        "message": "api.error.token.expired"}
    """
    url = URL + 'signin'

    dados = {"email": settings.EMAIL, "password": settings.PASS}

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Accept-Language': "en",
        'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'X-Api-Key': settings.API_STRANS,
    }

    vality = cache.get('vality', None)
    token = cache.get('token', None)

    if vality is None \
        or token is None \
            or vality < datetime.now():
        r = requests.post(url, headers=headers, data=json.dumps(dados))
        resp = json.loads(r.text)
        dt = datetime.now() + timedelta(minutes=9)
        cache.set_many({'vality': dt, 'token': resp['token']})


def home(request):
    return render(request, 'home.html', {})


def auth(request):

    url = URL + 'signin'

    dados = {"email": "brunoxbk@gmail.com", "password": "88441608"}

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Accept-Language': "en",
        'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'X-Api-Key': 'ade1e4f2830f431ba776457ecb17b27f',
    }

    r = requests.post(url, headers=headers, data=json.dumps(dados))
    dados = json.loads(r.text)
    dados['vality'] = datetime.now() + timedelta(minutes=10)
    mimetype = "application/json;charset=UTF-8"
    return HttpResponse(dados, mimetype)


def bus_by_line(request):
    """
        { buscando onibus as vezes da isso
        "code": 130,
        "message": "Item not found"}
    """

    check_token()

    url = URL + 'veiculosLinha'

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Accept-Language': "en",
        'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'X-Api-Key': 'ade1e4f2830f431ba776457ecb17b27f',
        'X-Auth-Token': cache.get('token')
    }

    param = {'busca': request.GET.get('busca', '')}

    r = requests.get(url, headers=headers, params=param)
    mimetype = "application/json;charset=UTF-8"
    return HttpResponse(r.text, mimetype)


def all_bus(request):
    url = URL + 'veiculos'

    check_token()

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Accept-Language': "en",
        'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'X-Api-Key': 'ade1e4f2830f431ba776457ecb17b27f',
        'X-Auth-Token': cache.get('token')
    }

    param = {'busca': request.GET.get('busca', '')}

    r = requests.get(url, headers=headers, params=param)
    mimetype = "application/json;charset=UTF-8"
    return HttpResponse(r.text, mimetype)


def lines(request):
    url = URL + 'linhas'

    check_token()

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Accept-Language': "en",
        'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'X-Api-Key': 'ade1e4f2830f431ba776457ecb17b27f',
        'X-Auth-Token': cache.get('token')
    }

    param = {'busca': request.GET.get('busca', '')}

    r = requests.get(url, headers=headers, params=param)
    mimetype = "application/json;charset=UTF-8"
    return HttpResponse(r.text, mimetype)


def bus_stop(request):
    url = URL + 'paradas'

    check_token()

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Accept-Language': "en",
        'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'X-Api-Key': 'ade1e4f2830f431ba776457ecb17b27f',
        'X-Auth-Token': cache.get('token')
    }

    param = {'busca': request.GET.get('busca', '')}

    r = requests.get(url, headers=headers, params=param)
    mimetype = "application/json;charset=UTF-8"
    return HttpResponse(r.text, mimetype)


def stop_by_line(request):
    """
        { buscando onibus as vezes da isso
        "code": 130,
        "message": "Item not found"}
    """

    check_token()

    url = URL + 'paradasLinha'

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Accept-Language': "en",
        'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'X-Api-Key': 'ade1e4f2830f431ba776457ecb17b27f',
        'X-Auth-Token': cache.get('token')
    }

    param = {'busca': request.GET.get('busca', '')}

    r = requests.get(url, headers=headers, params=param)
    mimetype = "application/json;charset=UTF-8"
    return HttpResponse(r.text, mimetype)


def autocomplete(request):
    query = Q()

    if request.GET.get('term', False):
        query = Q(denomination__icontains=request.GET['term']) | \
            Q(code_line__icontains=request.GET['term'])

    lines = Line.objects.filter(query)

    lines_parsed = []
    for l in lines:
        lines_parsed.append({
            'id': l.code_line, 'name': "%s" % l.__str__()})

    data = json.dumps(lines_parsed, ensure_ascii=False).encode('utf8')
    mimetype = "application/json;charset=UTF-8"
    return HttpResponse(data, mimetype)
