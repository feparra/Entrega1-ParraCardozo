# thegoodtraderpage
 entregaintermediaproyecto final
# tradingbook Evolution Marketing

En este repo van a encontrar el codigo fuente para la creacion de la pagina web de thegoodtrader

Conflicto

Instalar django

```shell
python -m pip install django
```

Aplicar cambios en base de datos

```shell
python manage.py makemigrations
python manage.py migrate
```

Iniciar servidor

```shell
python manage.py runserver
```

Crear usuario administrador

```shell
python manage.py createsuperuser
```

Tenemos una vista principal 
tenemos tres modelos (trades,mercados y notas)
con sus respectivas vistas 
los formatos han sido heredados en el HTML 
y se utilizaron los formatos forms para su ejecucion tenemos dos formas de buscar los datos uno directamente desde la vista de tradingbook 


la otra desde dashboard

se pueden agregar
- Trades 
- mercados
- y notas 
las cuales pueden ser visualizadas
