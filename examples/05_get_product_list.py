# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_product import PodProduct

try:
    pod_product = PodProduct(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        "id": [49179, 49032],
        # "attributes": [{
        #     "code": "size",
        #     "value": "M"
        # }],
        # "businessId": 7867,
        # "guildCode": [GUILD_CODE],
        # "currencyCode": "USD",
        # "uniqueId": ["123"],
        # "relatedProductsId": [123,456],
        "size": 5,
        # "tags": ["tag1"],
        # "tagTrees": ["tag1"],
        # "tagTreeCategoryName": ["tag1"],
        # "orderByPrice": "asc",  #  asc or desc
        # "orderBySale": "asc",  #  asc or desc
        # "orderByLike": "asc",  #  asc or desc
    }

    products = pod_product.get_product_list(**params)
    print(products)

    print("Total :", pod_product.total_items())
    # OUTPUT
    # [
    #   {
    #     "id": 94500,
    #     "version": 3,
    #     "timelineId": 55000,
    #     "entityId": 49032,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 1581142814790,
    #     "enable": True,
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
    #     "rate": {
    #       "rate": 0,
    #       "rateCount": 0
    #     },
    #     "userPostInfo": {
    #       "postId": 94500,
    #       "liked": False,
    #       "favorite": False
    #     },
    #     "latitude": 0,
    #     "longitude": 0,
    #     "canComment": True,
    #     "canLike": True,
    #     "canRate": True,
    #     "tags": [],
    #     "tagTrees": [],
    #     "name": "محصول تستی ویرایش شده",
    #     "description": "این محصول رو ویرایش کردیم",
    #     "categoryList": [],
    #     "unlimited": True,
    #     "availableCount": 0,
    #     "price": 150.08,
    #     "discount": 0,
    #     "attributeValues": [],
    #     "allowUserInvoice": False,
    #     "allowUserPrice": False,
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     },
    #     "preferredTaxRate": 0.09
    #   },
    #   {
    #     "id": 94679,
    #     "version": 0,
    #     "timelineId": 55169,
    #     "entityId": 49179,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 1581252520198,
    #     "enable": True,
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
    #     "rate": {
    #       "rate": 0,
    #       "rateCount": 0
    #     },
    #     "userPostInfo": {
    #       "postId": 94679,
    #       "liked": False,
    #       "favorite": False
    #     },
    #     "latitude": 0,
    #     "longitude": 0,
    #     "canComment": False,
    #     "canLike": False,
    #     "canRate": True,
    #     "tags": [],
    #     "tagTrees": [],
    #     "name": "محصول ثبت گروهی ۲",
    #     "description": "توضیحات محصول شماره ۲",
    #     "categoryList": [],
    #     "unlimited": True,
    #     "availableCount": 0,
    #     "price": 10000,
    #     "discount": 0,
    #     "attributeValues": [],
    #     "allowUserInvoice": False,
    #     "allowUserPrice": False,
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     }
    #   }
    # ]
    # Total : 2

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
