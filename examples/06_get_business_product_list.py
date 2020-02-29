# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_product import PodProduct

try:
    pod_product = PodProduct(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        # "id": [49179, 49032],
        # "attributes": [{
        #     "code": "size",
        #     "value": "M"
        # }],
        # "attributeTemplateCode": "مانتو",
        # "businessId": 7867,
        # "guildCode": [GUILD_CODE],
        # "currencyCode": "USD",
        # "uniqueId": ["123"],
        # "relatedProductsId": [123,456],
        "size": 5,
        # "scope": PodProduct.SCOPE_DEALER_PRODUCT_PERMISSION,   # PodProduct.SCOPE_BUSINESS_PRODUCT (default) or
        #                                                        # PodProduct.SCOPE_PARENT_PRODUCT or
        #                                                        # PodProduct.SCOPE_DEALER_PRODUCT_PERMISSION
        #
        "attributeSearchQuery": [{
            "field": "name",
            "is": "reza"
        }],
        # "tags": ["tag1"],
        # "tagTrees": ["tag1"],
        # "tagTreeCategoryName": ["tag1"],
        # "orderByPrice": "asc",  #  asc or desc
        # "orderBySale": "asc",  #  asc or desc
        # "orderByLike": "asc",  #  asc or desc
    }

    products = pod_product.get_business_product_list(**params)

    print(products)
    print("Total :", pod_product.total_items())
    # OUTPUT
    # [
    #   {
    #     "id": 70226,
    #     "version": 0,
    #     "timelineId": 31226,
    #     "entityId": 30344,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 1566711032212,
    #     "enable": True,
    #     "hide": False,
    #     "business": {
    #       "id": 9371,
    #       "name": "رضا استور شماره 7",
    #       "numOfProducts": 103,
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       }
    #     },
    #     "rate": {
    #       "rate": 0,
    #       "rateCount": 0
    #     },
    #     "userPostInfo": {
    #       "postId": 70226,
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
    #     "name": "محصول تخفیف دار",
    #     "description": "محصول ثبت شده در رضا استور 7",
    #     "categoryList": [],
    #     "unlimited": True,
    #     "availableCount": 0,
    #     "price": 55,
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
    # Total : 1

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
