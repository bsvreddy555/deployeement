"""curd_operations_by_html_forms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("insert_emp_details",views.insert_emp_view,name="insert_employee"),
    path("",views.Employee_details_view,name="home"),
    path("delete_data/<pk>",views.Delete_employee_Details,name="deletedata"),
    path("Update_data/<pk>",views.Update_Data,name="updata"),
    path("save_update_data/<pk>",views.Save_update_data,name="save_update_data")
]
