from django.urls import path
from .views import UserSignup, UserLogin, InvoiceView, SpecificInvoice, AddItemView

urlpatterns = [
    path('user/login', UserLogin.as_view(), name='login'),
    path('user/register', UserSignup.as_view(), name='register'),
    path('invoices', InvoiceView.as_view(), name='invoice'),
    path('invoices/<int:id>', SpecificInvoice.as_view(), name="specific-invoice"),
    path('invoices/<int:invoice_id>/items', AddItemView.as_view(), name="add-item")
]
