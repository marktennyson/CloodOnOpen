from django.shortcuts import render
from django.http import HttpResponse
from requests import get
from json import dumps
from .models import *
from .utils import Utils

utils:Utils = Utils()

def indexView(request):
    countries = CountryInfo.objects.all()
    context = {"countries":countries}
    return render(request, 'index.html', context)

def index2View(request):
    countries = CountryInfo.objects.all()
    context = {"countries":countries}
    return render(request, 'index2.html', context)

def apiIndexView(request):
    return utils.jsonify(message="Hello World!")

def putData(request):
    countries = get("https://restcountries.eu/rest/v2/all").json()
    regions = list()
    [regions.append(country['region']) for country in countries if country['region'] not in regions and country['region'] != '']
    for region in regions:
        reg = Region(name=region)
        reg.save()
    reg2 = Region(name="no-region")
    reg2.save()
    subRegions = list()
    [subRegions.append(country['subregion']) for country in countries if country['subregion'] not in subRegions and country['subregion'] != '']
    for subRegion in subRegions:
        subReg = SubRegion(name=subRegion)
        subReg.save()
    subReg2 = SubRegion(name="no-sub-region")
    subReg2.save()
    for country in countries:
        try: region = Region.objects.get(name=country['region'])
        except: region = Region.objects.get(name="no-region")
        try: subRegion = SubRegion.objects.get(name=country['subregion'])
        except: subRegion = SubRegion.objects.get(name="no-sub-region")
        ci = CountryInfo(name=country['name'],capital=country['capital'], region=region,flag=country['flag'],area=country['area'],
                subRegion=subRegion, population=country['population'], currency=country['currencies'][0]['code'] or "null",nativeName=country['nativeName'],
                languages=country['languages'][0]['name'] or "null", code=country['alpha3Code'], neighbours="_".join(country['borders']))
        ci.save()
    return utils.jsonify(message="Data inserted successfully.")

def allData(request):
    singleId = request.GET.get('id','')
    if singleId:
        try: return utils.jsonify(_=CountryInfo.objects.get(pk=singleId).toDict())
        except: return utils.jsonify(message="Country not found.")
    countries = CountryInfo.objects.all()
    countryL = list()
    for country in countries:
        countryL.append(country.toDict())
    return utils.jsonify(_=countryL)

def allRegions(request):
    regions = Region.objects.all()
    regionL = [region.toDict() for region in regions]
    return utils.jsonify(_=regionL)

def allSubRegions(request):
    subRegions = SubRegion.objects.all()
    subRegionL = [subRegion.toDict() for subRegion in subRegions]
    return utils.jsonify(_=subRegionL)

def countryPer(request):
    region = request.GET.get('region', '')
    subRegion = request.GET.get('subregion', '')
    neighbours = request.GET.get('neighbours', '')
    population = request.GET.get('population', '')
    if not region and not subRegion and not neighbours and not population: return HttpResponse(dumps({'message' : 'please provide a valid query param.'}))
    if region: 
        try: regionObj = Region.objects.get(name=region)
        except: return HttpResponse(dumps({'message':"please enter a valid region name"}))
        allCountry = CountryInfo.objects.filter(region=regionObj)
    elif subRegion: 
        try: subRegionObj = SubRegion.objects.get(name=subRegion)
        except: return HttpResponse(dumps({'message':"Please enter a valid sub region name."}))
        allCountry = CountryInfo.objects.filter(subRegion=subRegionObj)
    elif neighbours:
        countryObj = CountryInfo.objects.get(name=neighbours)
        try: neighbourCountryCodes = countryObj.neighbours.split("_")
        except: return HttpResponse(dumps([]))
        allCountry = list()
        for i in neighbourCountryCodes:
            allCountry.append(CountryInfo.objects.get(code=i))
    elif population:
        M = 1000000
        B = 1000000000
        if population == 'bel1m': allCountry = CountryInfo.objects.filter(population__lte=M)
        elif population == '1to10m': allCountry = CountryInfo.objects.filter(population__gte=M, population__lte=10*M)
        elif population == '10to30m': allCountry = CountryInfo.objects.filter(population__gte=10*M, population__lte=30*M)
        elif population == '30to100m': allCountry = CountryInfo.objects.filter(population__gte=30*M, population__lte=100*M)
        elif population == '100to300m': allCountry = CountryInfo.objects.filter(population__gte=100*M, population__lte=300*M)
        elif population == '300to500m': allCountry = CountryInfo.objects.filter(population__gte=300*M, population__lte=500*M)
        elif population == '500to700m': allCountry = CountryInfo.objects.filter(population__gte=500*M, population__lte=700*M)
        elif population == '700to1b': allCountry = CountryInfo.objects.filter(population__gte=700*M, population__lte=B)
        elif population == 'gth1b': allCountry = CountryInfo.objects.filter(population__gte=B)
    allCountryL = [country.toDict() for country in allCountry]
    return utils.jsonify(_=allCountryL)