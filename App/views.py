from django.shortcuts import render
from django.http import HttpResponse
import requests
                                                                      
def file_list(request):
    '''
    Функция для получения списка файлов на Яндекс диске
    Для её написания использовалась документация по REST API: https://yandex.ru/dev/disk-api/doc/ru/reference/public
    '''                   
    # Запрос на получение метаинформации опубликованного ресурса 
    Meta_info = 'https://cloud-api.yandex.net/v1/disk/public/resources'       

    # Получаем публичную ссылку как параметр введённого GET-запроса
    public_link = request.GET.get('public_link')
    # Если ссылка не введена, получаем ошибку 400 (синтаксис запроса)                        
    if not public_link:                                                
        return HttpResponse('Требуется публичная ссылка', status=400)
    
    # Запрос на получение страницы с помощью библиотеки requests
    response = requests.get(f"{Meta_info}?public_key={public_link}")
    # Если запрос не успешен, выводим ошибку с соответствующим кодом
    if response.status_code!=200:
        return HttpResponse('Ошибка извлечения файла из Яндекс диска', status=response.status_code)
    
    # Получаем информацию в формате JSON и извлекаем список 'items', каждый элемент которого является вложенным в папку ресурсом     
    files = response.json().get('_embedded', {}).get('items', [])

    # Выводим на экран информацию с помощью html-файла, в который передаём необходимые данные в словаре
    return render(request, 'file_list.html', {'files':files})

