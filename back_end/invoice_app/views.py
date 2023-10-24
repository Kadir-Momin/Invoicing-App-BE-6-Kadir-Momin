from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .data import *
from .serializers import *
import json
import jwt


# Create your views here.

class UserSignup(APIView):
    def post(self, request):
        user_data = json.loads(request.body)
        user_data["user_id"] = len(users) + 1
        serializer = UserSerializer(data = user_data)

        if serializer.is_valid():
            users.append(serializer.data)
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status=401)

class UserLogin(APIView):
    def post(self, request):
        user_data = json.loads(request.body)
        for user in users:
            if user_data["email"] == user["email"] and user_data["password"] == user["password"]:
                token = jwt.encode({"email" : user["email"], "user_id" : user["user_id"]}, "secret", algorithm="HS256")
                return Response({"message" : "User Logged in successfuly", "token" : str(token)}, status=201)
        return Response({"message" : "User ID or password does not match"}, status= 401)


class InvoiceView(APIView):
    def get(self, request):
        serializer = InvoiceSerializer(invoice_data, many=True).data
        return Response(serializer)

    def post(self, request):
        data = json.loads(request.body)
        data["invoice_id"] = len(invoice_data) + 1
        serializer = InvoiceSerializer(data = data)
        if serializer.is_valid():
            invoice_data.append(serializer.data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SpecificInvoice(APIView):
    def get(self, request, id):
        for val in invoice_data:
            if val["invoice_id"] == id:
                serializer = InvoiceSerializer(val).data
                return Response(serializer)
        return Response({"message" : "Invoice not found"}, status=404)


class AddItemView(APIView):
    def post(self, request, invoice_id):
        for val in invoice_data:
            if val["invoice_id"] == invoice_id:
                data = json.loads(request.body)
                serializer = ItemSerializer(data = data)
                if serializer.is_valid():
                    val["items"].append(serializer.data)
                    return Response(serializer.data, status=201)
                return Response(serializer.errors, status=400)
        return Response({"message" : "Invoice not found"}, status=404)

