from .models import AcademicSession, AcademicTerm

class SiteWideConfig:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_session = AcademicSession.objects.get(current=True)
        current_term = AcademicTerm.objects.get(curent=True)

        request.current_session = current_session
        request.current_term = current_term

        response = self.get_response(request)

        return response