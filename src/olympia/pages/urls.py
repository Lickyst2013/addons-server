from django.conf import settings
from django.conf.urls import patterns, url
from django.http import HttpResponsePermanentRedirect as perma_redirect
from django.views.generic.base import TemplateView

from olympia.amo.urlresolvers import reverse

from . import views


urlpatterns = patterns(
    '',
    url('^about$',
        TemplateView.as_view(template_name='pages/about.lhtml'),
        name='pages.about'),
    url('^credits$', views.credits, name='pages.credits'),
    url('^faq$',
        TemplateView.as_view(template_name='pages/faq.html'),
        name='pages.faq'),
    url('^google1f3e37b7351799a5\.html$',
        TemplateView.as_view(
            template_name='pages/google_webmaster_verification.html')),

    url('^compatibility_firstrun$',
        TemplateView.as_view(template_name='pages/acr_firstrun.html'),
        name='pages.acr_firstrun'),
    url('^developer_faq$',
        TemplateView.as_view(template_name='pages/dev_faq.html'),
        name='pages.dev_faq'),
    url('^review_guide$',
        TemplateView.as_view(template_name='pages/review_guide.html'),
        name='pages.review_guide'),

    url('^shield-study-2/',
        TemplateView.as_view(template_name='pages/shield_study_2.html'),
        name='pages.shield_study_2'),
    url('^shield_study_3$',
        TemplateView.as_view(template_name='pages/shield_study_3.html'),
        name='pages.shield_study_3'),
    url('^shield_study_4$',
        TemplateView.as_view(template_name='pages/shield_study_4.html'),
        name='pages.shield_study_4'),
    url('^shield_study_5$',
        TemplateView.as_view(template_name='pages/shield_study_5.html'),
        name='pages.shield_study_5'),
    url('^shield_study_6$',
        TemplateView.as_view(template_name='pages/shield_study_6.html'),
        name='pages.shield_study_6'),
    url('^shield_study_7$',
        TemplateView.as_view(template_name='pages/shield_study_7.html'),
        name='pages.shield_study_7'),
    url('^shield_study_8$',
        TemplateView.as_view(template_name='pages/shield_study_8.html'),
        name='pages.shield_study_8'),

    url('^pages/compatibility_firstrun$',
        lambda r: perma_redirect(reverse('pages.acr_firstrun'))),
    url('^pages/developer_faq$',
        lambda r: perma_redirect(reverse('pages.dev_faq'))),
    url('^pages/review_guide$',
        lambda r: perma_redirect(reverse('pages.review_guide'))),
    url('^pages/developer_agreement$',
        lambda r: perma_redirect(reverse('devhub.docs',
                                         args=['policies/agreement']))),
    url('^pages/validation$',
        lambda r: perma_redirect(settings.VALIDATION_FAQ_URL)),

    url('^sunbird$',
        TemplateView.as_view(template_name='pages/sunbird.html'),
        name='pages.sunbird'),
    url('^sunbird/', lambda r: perma_redirect(reverse('pages.sunbird'))),
)
