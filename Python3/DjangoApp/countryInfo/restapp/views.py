from django.shortcuts import render
from django.http import HttpResponse
from requests import get
from json import dumps
from .models import *

def indexView(request):
    countries = CountryInfo.objects.all()
    context = {"countries":countries}
    return render(request, 'index.html', context)

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
        ci = CountryInfo(name=country['name'],capital=country['capital'], region=region,
                subRegion=subRegion, population=country['population'], currency=country['currencies'][0]['code'] or "null",
                languages=country['languages'][0]['name'] or "null", code=country['alpha3Code'], neighbours="_".join(country['borders']))
        ci.save()
    return HttpResponse('Done')

def allData(request):
    countries = CountryInfo.objects.all()
    countryL = list()
    for country in countries:
        countryL.append(country.toDict())
    return HttpResponse(dumps(countryL))

def allRegions(request):
    regions = Region.objects.all()
    regionL = [region.toDict() for region in regions]
    return HttpResponse(dumps(regionL))

def allSubRegions(request):
    subRegions = SubRegion.objects.all()
    subRegionL = [subRegion.toDict() for subRegion in subRegions]
    return HttpResponse(dumps(subRegionL))

def countryPer(request):
    region = request.GET.get('region', '')
    subRegion = request.GET.get('subregion', '')
    neighbours = request.GET.get('neighbours', '')
    if not region and not subRegion and not neighbours: return HttpResponse(dumps({'message' : 'please provide region or subregion name'}))
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
        neighbourCountryCodes = countryObj.neighbours.split("_")
        print (neighbourCountryCodes)
        if len(neighbourCountryCodes) == 1 and not len(neighbourCountryCodes[0]): return HttpResponse(dumps([{"message":False}]))
        allCountry = list()
        for i in neighbourCountryCodes:
            allCountry.append(CountryInfo.objects.get(code=i))
    allCountryL = [country.toDict() for country in allCountry]
    return HttpResponse(dumps(allCountryL)) 