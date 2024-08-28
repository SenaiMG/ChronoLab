from django.shortcuts import render
from notifications.service import EmailService
from users.service import UserService
from .service import ProductService

# Create your views here.

EmailService.send_email_with_attachment(
    subject="Novo produto adicionado",
    message="Confira as Novidades do nosso site como o novo lançamento",
    recipient_list=UserService.list_all_email_users,
    attachment_path='',
)