from django.views.generic import TemplateView


class NewsletterView(TemplateView):
    template_name = 'newsletter-subscribe.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['sample'] = 'some-data'

        return context
