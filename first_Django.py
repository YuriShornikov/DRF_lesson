#django-admin startproject lesson1 .    - создание своего проекта lesson1(название)  . - место создания, в данном случае это расположение место папки
#python manage.py runserver - запуск сервера
#./manage.py migrate - создание бд
#python manage.py startapp demo   запуск приложения с названием demo
#ctrl-Breake   - остановка работы сервера
#в созданном пакете через app в файле views.py прописывают функции для пользователя
#в пакете lesson1 в файле urls.py прописываются связи с views.py для отображения для пользователя в браузере (роутинг)
#python manage.py makemigrations в папке migrations создается файл с записями изменений
#python manage.py migrate - чтобы вступили в силу изменения
#python manage.py createsuperuser создание админки
#admin dbonlyfun@gmail.com Irregularlydgango
# views     models       urls     templates
#creatdb -U postgres (название бд)
#pip install psycopg2-binary
#pip install django_filter   в  settings INSTALLED_APPS прописываем 'django_filters', а так же для использования
#REST_FRAMEWORK = {
    #'DEFAULT_FILTER_BACKEND': [
        #'django.filters.rest_framework.DjangoFilterBackend'
    #]
#}


#auth
#В settigns в INSTALLED_APPS добавляем rest_framework.authtoken и после этого делаем миграцию python.manage.py migrate
#REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication'
#     ]
# }

#в http запросе передается Authorization: Token сам токен
#во view прописываем метод:
# def perform_create(self, serializer):
#     serializer.save(user=self.request.user)

#в serializers прописываем поле для чтения read_only_fields = ['user']
#для подтверждения пользователя используем class во views: permission_classes = [IsAuthenticated]
#для ограничения прав используем: файл permissions.py:
#создаем класс class IsOwnerOrReadOnly(BasePermission):
#создаем функцию для обозначения прав def has_object_permission(self, request, view, obj):
#if request.method == 'GET':
#return True на разрешение метода GET
#возвращаем при совпадении прав return request.user == obj.user


