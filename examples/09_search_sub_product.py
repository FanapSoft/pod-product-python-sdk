# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_product import PodProduct

try:
    pod_product = PodProduct(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        # "q": "اطلاعات",
        # "tags": ["tag1"],
        # "tagTrees": ["tagname"],
        "orderByAttributeCode": "size",  # asc or desc
        "orderByDirection": "desc",  # asc or desc
        "page": 1,
        "size": 2
    }

    products = pod_product.search_sub_product(product_group_id=[3915], **params)

    print(products)
    print("Total :", pod_product.total_items())
    # OUTPUT
    # [
    #   {
    #     "id": 0,
    #     "version": 0,
    #     "timelineId": 0,
    #     "entityId": 49144,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 0,
    #     "enable": False,
    #     "hide": False,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 404,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000000"
    #     },
    #     "latitude": 0,
    #     "longitude": 0,
    #     "name": "محصول تستی با اطلاعات کامل‌",
    #     "description": "Unit Test Production",
    #     "categoryList": [],
    #     "preview": "https://miro.medium.com/max/2600/0*WkY7VuAwNf0K5YRz.png",
    #     "unlimited": False,
    #     "availableCount": 1000,
    #     "price": 150.08,
    #     "discount": 0,
    #     "attributeValues": [
    #       {
    #         "code": "gender",
    #         "name": "جنسیت",
    #         "value": "زن"
    #       },
    #       {
    #         "code": "size",
    #         "name": "اندازه",
    #         "value": "M"
    #       },
    #       {
    #         "code": "color",
    #         "name": "رنگ",
    #         "value": "سبز"
    #       }
    #     ],
    #     "guild": {
    #       "id": 561,
    #       "name": "سرویس دهندگان",
    #       "code": "API_GUILD"
    #     },
    #     "allowUserInvoice": True,
    #     "allowUserPrice": True,
    #     "templateCode": "مانتو",
    #     "productGroup": {
    #       "id": 3915,
    #       "sharedAttributeCodes": [
    #         "size"
    #       ]
    #     },
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     },
    #     "preferredTaxRate": 0.09
    #   },
    #   {
    #     "id": 0,
    #     "version": 0,
    #     "timelineId": 0,
    #     "entityId": 49159,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 0,
    #     "enable": False,
    #     "hide": False,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 404,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000000"
    #     },
    #     "latitude": 0,
    #     "longitude": 0,
    #     "name": "زیر محصول",
    #     "categoryList": [],
    #     "unlimited": False,
    #     "availableCount": 500,
    #     "price": 1200,
    #     "discount": 0,
    #     "attributeValues": [
    #       {
    #         "code": "gender",
    #         "name": "جنسیت",
    #         "value": "زن"
    #       },
    #       {
    #         "code": "size",
    #         "name": "اندازه",
    #         "value": "L"
    #       },
    #       {
    #         "code": "color",
    #         "name": "رنگ",
    #         "value": "سبز"
    #       }
    #     ],
    #     "allowUserInvoice": False,
    #     "allowUserPrice": False,
    #     "templateCode": "مانتو",
    #     "productGroup": {
    #       "id": 3915,
    #       "sharedAttributeCodes": [
    #         "size"
    #       ]
    #     },
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     },
    #     "preferredTaxRate": 0.09
    #   }
    # ]
    # Total : 23

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
