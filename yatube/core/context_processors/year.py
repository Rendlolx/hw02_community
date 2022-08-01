from datetime import datetime

def year(request):
    """Добавляет переменную с текущим годом.""" 
    a = datetime.now()
    a = int(a.strftime('%Y'))
    print(a)
    return {
        'year': a,
    }