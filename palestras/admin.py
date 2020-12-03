from django.contrib import admin
from palestras.models import Palestra, Ouvinte, Inscricao

# Register your models here.
class Palestras(admin.ModelAdmin):
    list_display = ('id', 'title', 'local', 'datetimeStart', 'datetitmeEnd')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20 

admin.site.register(Palestra, Palestras)



class Ouvintes(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20
    
admin.site.register(Ouvinte, Ouvintes)



class Inscricoes(admin.ModelAdmin):
    list_display = ('id', 'palestrafk', 'ouvintefk')
    list_display_links = ('id',)
admin.site.register(Inscricao, Inscricoes)


# class Cursos(admin.ModelAdmin):
#     list_display = ('id', 'codigo_curso', 'descricao')
    # list_display_links = ('id', 'codigo_curso')
    # search_fields = ('codigo_curso',)
# admin.site.register(Curso, Cursos)
