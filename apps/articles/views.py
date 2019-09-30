from django.http import HttpResponse

# Отображение url articles и articles/test/
def index(request):
	return HttpResponse("Привет Ксюша!")

def test(request):
	return HttpResponse("Это тестовая страница")
	# Тестовое изменение 