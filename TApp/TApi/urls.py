from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'merchants', views.MerchantViewSet)
router.register(r'plans', views.PlanViewSet)
router.register(r'schemes', views.SchemeViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'termsInfo', views.TermsInfoViewSet)
router.register(r'redempInfo', views.RedemptionInfoViewSet)
router.register(r'cancelInfo', views.CancellationInfoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('query1/<int:user_id>', views.activePlansMerchant, name= "activePlansMerchant"),
    path('query2/<int:user_id>', views.totalActivePlansMerchant, name= "totalActivePlansMerchant"),
    path('query3/<int:user_id>', views.totalVoidedPlansMerchant, name= "totalVoidedPlansMerchant"),  
    path('query1/<str:user>', views.activePlansMerchant, name= "activePlansMerchant"),
    path('query2/<str:user>', views.totalActivePlansMerchant, name= "totalActivePlansMerchant"),
    path('query3/<str:user>', views.totalVoidedPlansMerchant, name= "totalVoidedPlansMerchant"),   
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]