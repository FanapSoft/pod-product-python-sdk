# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_product import PodProduct

try:
    pod_product = PodProduct(api_token=API_TOKEN, server_type=SERVER_MODE)

    print(pod_product.add_product(name="محصول تستی", price=150.08, description="توضیحات لازم برای این محصول"))
    # OUTPUT
    # {
    #   "id": 94500,
    #   "version": 0,
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
    #     "numOfProducts": 397,
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
    #   "name": "محصول تستی",
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

    other_params = {
        "description": "Python Test",
        "unlimited": False,  # default : True
        "canComment": True,
        "canLike": True,
        "enable": True,
        "discount": 0,
        "guildCode": GUILD_CODE,
        # "parentProductId": 42098,
        "uniqueId": "1234567890",
        "metaData": {"test": "yes"},
        "allowUserInvoice": True,  # default : False
        "allowUserPrice": True,  # default : False
        "currencyCode": "IRR",
        "attTemplateCode": "مانتو",
        "attributes":
            [
                {
                    "code": "gender",
                    "value": "زن",
                    "group": False,
                },
                {
                    "code": "color",
                    "value": "سبز",
                    "group": False,
                },
                {
                    "code": "size",
                    "value": "M",
                    "group": True,
                }
            ],
        "lat": 43.787568,
        "lng": 74.9890685,
        "tags": ["tag1", "tag2"],
        "content": "تست محتوای مخفی برای یک محصول",
        "previewImage": "https://miro.medium.com/max/2600/0*WkY7VuAwNf0K5YRz.png",
        # "tagTrees": ["Tag tree level 01"],
        # "tagTreeCategoryName": "TestTagCategory5dd13cef16902",
        "preferredTaxRate": 0.09,
        "quantityPrecision": 2
    }
    product = pod_product.add_product(name="محصول تستی با اطلاعات کامل و زیر محصول", price=150.08, available_count=1000,
                                      **other_params)
    print(product)
    # OUTPUT
    # {
    #   "id": 94645,
    #   "version": 0,
    #   "timelineId": 55145,
    #   "entityId": 49144,
    #   "numOfLikes": 0,
    #   "numOfDisLikes": 0,
    #   "numOfFavorites": 0,
    #   "numOfComments": 0,
    #   "timestamp": 1581234195441,
    #   "enable": True,
    #   "hide": False,
    #   "business": {
    #     "id": 7867,
    #     "name": "شرکت رضا",
    #     "numOfProducts": 398,
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
    #     "postId": 94645,
    #     "liked": False,
    #     "favorite": False
    #   },
    #   "latitude": 43.787568,
    #   "longitude": 74.9890685,
    #   "uniqueId": "1234567890",
    #   "canComment": True,
    #   "canLike": True,
    #   "canRate": True,
    #   "tags": [
    #     "tag1",
    #     "tag2"
    #   ],
    #   "tagTrees": [],
    #   "name": "محصول تستی با اطلاعات کامل و زیر محصول‌",
    #   "description": "Unit Test Production",
    #   "categoryList": [],
    #   "preview": "https://miro.medium.com/max/2600/0*WkY7VuAwNf0K5YRz.png",
    #   "unlimited": False,
    #   "availableCount": 1000,
    #   "price": 150.08,
    #   "discount": 0,
    #   "attributeValues": [
    #     {
    #       "code": "gender",
    #       "name": "جنسیت",
    #       "value": "زن"
    #     },
    #     {
    #       "code": "size",
    #       "name": "اندازه",
    #       "value": "M"
    #     },
    #     {
    #       "code": "color",
    #       "name": "رنگ",
    #       "value": "سبز"
    #     }
    #   ],
    #   "guild": {
    #     "id": 561,
    #     "name": "سرویس دهندگان",
    #     "code": "API_GUILD"
    #   },
    #   "allowUserInvoice": True,
    #   "allowUserPrice": True,
    #   "templateCode": "مانتو",
    #   "productGroup": {
    #     "id": 3915,
    #     "sharedAttributeCodes": [
    #       "size"
    #     ]
    #   },
    #   "content": "تست محتوای مخفی برای یک محصول",
    #   "currency": {
    #     "name": "ریال",
    #     "code": "IRR"
    #   },
    #   "preferredTaxRate": 0.09
    # }

    attributes = [
        {
            "code": "size",
            "value": "L",
            "group": True,
        }
    ]
    
    sub_product = pod_product.add_sub_product(product["productGroup"]["id"], name="زیر محصول", price=1200,
                                              available_count=500, attributes=attributes, description="زیر محصول")
    print(sub_product)
    # OUTPUT
    # {
    #   "id": 94645,
    #   "version": 0,
    #   "timelineId": 55145,
    #   "entityId": 49159,
    #   "numOfLikes": 0,
    #   "numOfDisLikes": 0,
    #   "numOfFavorites": 0,
    #   "numOfComments": 0,
    #   "timestamp": 1581234195441,
    #   "enable": True,
    #   "hide": False,
    #   "business": {
    #     "id": 7867,
    #     "name": "شرکت رضا",
    #     "numOfProducts": 398,
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
    #     "postId": 94645,
    #     "liked": False,
    #     "favorite": False
    #   },
    #   "latitude": 43.787568,
    #   "longitude": 74.9890685,
    #   "uniqueId": "1234567890",
    #   "canComment": True,
    #   "canLike": True,
    #   "canRate": True,
    #   "tags": [
    #     "tag1",
    #     "tag2"
    #   ],
    #   "tagTrees": [],
    #   "name": "زیر محصول",
    #   "categoryList": [],
    #   "unlimited": False,
    #   "availableCount": 500,
    #   "price": 1200,
    #   "discount": 0,
    #   "attributeValues": [
    #     {
    #       "code": "gender",
    #       "name": "جنسیت",
    #       "value": "زن"
    #     },
    #     {
    #       "code": "size",
    #       "name": "اندازه",
    #       "value": "L"
    #     },
    #     {
    #       "code": "color",
    #       "name": "رنگ",
    #       "value": "سبز"
    #     }
    #   ],
    #   "allowUserInvoice": False,
    #   "allowUserPrice": False,
    #   "templateCode": "مانتو",
    #   "productGroup": {
    #     "id": 3915,
    #     "sharedAttributeCodes": [
    #       "size"
    #     ]
    #   },
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
