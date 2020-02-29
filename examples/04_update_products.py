# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_product import PodProduct

try:
    pod_product = PodProduct(api_token=API_TOKEN, server_type=SERVER_MODE)

    products = [{
        "entityId": 49032,
        "name": "محصول تستی ویرایش شده - گروهی",
        "price": 1607,
        "description": "این محصول رو به صورت گروهی هم ویرایش کردیم",
        "availableCount": 10000,
        "catRate": True,
    }, {
        "entityId": 49179,
        "name": "اینم ویرایش شد",
        "price": 16007,
        "description": "این را نیز ویرایش کردیم",
        "unlimited": False,
        "canComment": True,
        "canLike": True
    }]

    print(pod_product.update_products(products=products))
    # OUTPUT
    # {
    #   "id": 94500,
    #   "version": 1,
    #   "timelineId": 55000,
    #   "entityId": 49032,
    #   "numOfLikes": 0,
    #   "numOfDisLikes": 0,
    #   "numOfFavorites": 0,
    #   "numOfComments": 0,
    #   "timestamp": 1581142814790,
    #   "enable": True,
    #   "hide": False,
    #   "business": {
    #     "id": 7867,
    #     "name": "شرکت رضا",
    #     "numOfProducts": 404,
    #     "rate": {
    #       "rate": 8,
    #       "rateCount": 1
    #     },
    #     "sheba": "640170000000000000000000"
    #   },
    #   "rate": {
    #     "rate": 0,
    #     "rateCount": 0
    #   },
    #   "userPostInfo": {
    #     "postId": 94500,
    #     "liked": False,
    #     "favorite": False
    #   },
    #   "latitude": 0,
    #   "longitude": 0,
    #   "canComment": True,
    #   "canLike": True,
    #   "canRate": True,
    #   "tags": [],
    #   "tagTrees": [],
    #   "name": "محصول تستی ویرایش شده",
    #   "description": "این محصول رو ویرایش کردیم",
    #   "categoryList": [],
    #   "unlimited": True,
    #   "availableCount": 0,
    #   "price": 150.08,
    #   "discount": 0,
    #   "attributeValues": [],
    #   "allowUserInvoice": False,
    #   "allowUserPrice": False,
    #   "currency": {
    #     "name": "ریال",
    #     "code": "IRR"
    #   },
    #   "preferredTaxRate": 0.09
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
