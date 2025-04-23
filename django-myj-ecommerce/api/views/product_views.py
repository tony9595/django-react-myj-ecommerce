from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Category, Product
from api.serializers.product_serializers import ProductSerializer


@api_view(["GET", "POST"])
def products_api(request):

    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # 디시리얼라이져
    # if request.method == "POST":
    #     print(request.data)
    #     print("타입 : ", type(request.data))
    #     serializer = ProductSerializer(data=request.data)

    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data)

    # dev_33
    if request.method == "POST":

        # requset.data 는 기본적으로 불변임
        data = request.data.copy()
        category_data = data.pop("category")
        category_data = request.data["category"]

        if isinstance(category_data, list):
            category_data = category_data[0]

        category, _ = Category.objects.get_or_create(**category_data)

        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(category=category)

        return Response(serializer.data)


@api_view(["GET", "DELETE", "PUT"])
def product_api(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        product.delete()
        return Response("SUCCESS", status=status.HTTP_204_NO_CONTENT)
