import sys
import os
import django
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'thebus.settings'
django.setup()

from core.models import Line


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


json_data = open(BASE_DIR + '/seeds/lines.json').read()
data = json.loads(json_data)


for item in data:
    line = Line(
        code_line=item['CodigoLinha'],
        denomination=item['Denomicao'],
        origin=item['Origem'],
        line_return=item['Retorno'],
        circle=item['Circular']
    )
    print(line.__dict__)
    line.save()
