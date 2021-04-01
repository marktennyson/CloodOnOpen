from django.http import JsonResponse
from datetime import datetime
from json import dumps

class Utils:
    def timestamp(self, someTime:datetime=None) -> str:
        defaultFormat = '%d-%m-%Y <=> %H:%M:%S'
        if not someTime: return datetime.strftime(datetime.now(), defaultFormat)
        else: return datetime.strftime(someTime, defaultFormat)

    def jsonify(self, **kwargs) -> JsonResponse:
        print ("Aniket")
        print (type(kwargs))
        if len(kwargs)==1 and "_" in list(kwargs.keys()): return JsonResponse(kwargs.get("_"), safe=False)
        kwargs.update({'timestamp':self.timestamp()})
        return JsonResponse(kwargs)