import functions_framework

from functions.my_function import hello_world
from functions.my_function_2 import hello_world_2

@functions_framework.http
def hello_world(request):
    return hello_world(request)

@functions_framework.http
def hello_world_2(request):
    return hello_world_2(request)