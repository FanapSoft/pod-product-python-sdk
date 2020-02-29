# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_product import PodProduct

try:
    pod_product = PodProduct(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        # "q": "محصول",
        # "id": [49342],
        # "uniqueId": ["abc"],
        # "relatedProductsId": [],
        # "businessId": 7867,
        # "guildCode": ["CLOTHING_GUILD"],
        # "currencyCode": "IRR",
        # "attributes": [
        #     {
        #         "code": "size",
        #         "value": "M"
        #     },
        #     {
        #         "code": "size",
        #         "value": "L"
        #     }
        # ],
        # "attributeTemplateCode": "مانتو",
        # "tags": ["tag1"],
        # "tagTreeCategoryName": ["tagname1"],
        # "tagTrees": ["tagname"],
        # "orderByLike": "desc",  #  asc or desc
        # "orderBySale": "asc",  #  asc or desc
        # "orderByPrice": "asc",  #  asc or desc
        # "firstId": 0,
        # "lastId": 0,
        "page": 1,
        "size": 2
    }

    products = pod_product.search_product(**params)

    print(products)
    print("Total :", pod_product.total_items())
    # OUTPUT
    # {
    #   "products": [
    #     {
    #       "id": 43,
    #       "version": 20,
    #       "timelineId": 43,
    #       "entityId": 21,
    #       "numOfLikes": 0,
    #       "numOfDisLikes": 0,
    #       "numOfFavorites": 0,
    #       "numOfComments": 0,
    #       "timestamp": 1499664748377,
    #       "enable": true,
    #       "hide": false,
    #       "business": {
    #         "id": 207,
    #         "image": "http://templates24.org/web/uploads/defaults/profileImage.png",
    #         "numOfProducts": 1,
    #         "rate": {
    #           "rate": 0,
    #           "rateCount": 0
    #         },
    #         "sheba": "1291784017349074"
    #       },
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "userPostInfo": {
    #         "postId": 43,
    #         "liked": false,
    #         "favorite": false
    #       },
    #       "latitude": 0,
    #       "longitude": 0,
    #       "canComment": true,
    #       "canLike": true,
    #       "canRate": true,
    #       "tags": [],
    #       "tagTrees": [],
    #       "name": "محصول",
    #       "description": "یک محصول عالی",
    #       "categoryList": [
    #         "APPLIANCE_PRODUCT"
    #       ],
    #       "previewInfo": {
    #         "id": 298,
    #         "name": "Koala.jpg",
    #         "actualWidth": 1024,
    #         "actualHeight": 768,
    #         "width": 1024,
    #         "height": 768
    #       },
    #       "unlimited": false,
    #       "availableCount": 1414,
    #       "price": 790000,
    #       "discount": 0,
    #       "attributeValues": [],
    #       "allowUserInvoice": false,
    #       "allowUserPrice": false,
    #       "currency": {
    #         "name": "ریال",
    #         "code": "IRR"
    #       }
    #     },
    #     {
    #       "id": 2928,
    #       "version": 0,
    #       "timelineId": 2868,
    #       "entityId": 301,
    #       "numOfLikes": 0,
    #       "numOfDisLikes": 0,
    #       "numOfFavorites": 0,
    #       "numOfComments": 0,
    #       "timestamp": 1505131731480,
    #       "enable": true,
    #       "hide": false,
    #       "business": {
    #         "id": 23,
    #         "name": "فروشگاه عباسی",
    #         "image": "http://sandbox.fanapium.com:8080/nzh/image/?imageId=...",
    #         "numOfProducts": 133,
    #         "rate": {
    #           "rate": 3,
    #           "rateCount": 2
    #         },
    #         "phone": "02177337733"
    #       },
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "userPostInfo": {
    #         "postId": 2928,
    #         "liked": false,
    #         "favorite": false
    #       },
    #       "latitude": 0,
    #       "longitude": 0,
    #       "canComment": false,
    #       "canLike": false,
    #       "canRate": true,
    #       "tags": [],
    #       "tagTrees": [],
    #       "name": "محصول اجاره ای",
    #       "description": "this is a test",
    #       "categoryList": [],
    #       "unlimited": false,
    #       "availableCount": 5,
    #       "price": 1000,
    #       "discount": 0,
    #       "attributeValues": [],
    #       "allowUserInvoice": false,
    #       "allowUserPrice": false,
    #       "currency": {
    #         "name": "ریال",
    #         "code": "IRR"
    #       }
    #     },
    #     ...
    #   ],
    #   "guilds": [
    #     {
    #       "id": 44,
    #       "name": "آرایش و زیبایی",
    #       "code": "TOILETRIES_GUILD"
    #     },
    #     {
    #       "id": 45,
    #       "name": "بهداشت و درمان",
    #       "code": "HEALTH_GUILD"
    #     }
    #   ]
    # }
    # Total : 23

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
