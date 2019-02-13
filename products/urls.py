from django.urls import path
from .views import list_products, create_products, update_product, delete_product, contact_upload, list_tabela, list_tabela2

urlpatterns = [
    path('', list_products, name='list_products'),
    path('tabela', list_tabela, name='list_tabela'),
    path('tabela2', list_tabela2, name='list_tabela2'),
    path('new', create_products, name='create_products'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    path('upload-csv/', contact_upload, name='contact_upload'),

]