# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_product import PodProduct

try:
    pod_product = PodProduct(api_token=API_TOKEN, server_type=SERVER_MODE)
    products = [{
        "name": "محصول ثبت گروهی ۱",
        "description": "توضیحات محصول شماره ۱",
        "price": 12500,
        "available_count": 100
    }, {
        "name": "محصول ثبت گروهی ۲",
        "description": "توضیحات محصول شماره ۲",
        "price": 10000,
        "unlimited": True,
        "canComment": False,
        "canLike": False,
        "tags": ["tag1", "tag2"],
        "attTemplateCode": "مانتو",
        "attributes": [{
            "code": "size",
            "value": "M",
            "group": False
        }, {
            "code": "color",
            "value": "قرمز",
            "group": False
        }, {
            "code": "gender",
            "value": "دخترانه",
            "group": False
        }]
    }]
    print(pod_product.add_products(products))
    # OUTPUT
    # [
    #   {
    #     "id": 95220,
    #     "version": 0,
    #     "timelineId": 55700,
    #     "entityId": 49514,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 1581492740843,
    #     "enable": True,
    #     "hide": False,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 406,
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
    #       "postId": 95220,
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
    #     "name": "محصول ثبت گروهی ۱",
    #     "description": "توضیحات محصول شماره ۱",
    #     "categoryList": [],
    #     "unlimited": False,
    #     "availableCount": 100,
    #     "price": 12500,
    #     "discount": 0,
    #     "attributeValues": [],
    #     "allowUserInvoice": False,
    #     "allowUserPrice": False,
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     }
    #   },
    #   {
    #     "id": 95221,
    #     "version": 0,
    #     "timelineId": 55701,
    #     "entityId": 49515,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 1581492740961,
    #     "enable": True,
    #     "hide": False,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 406,
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
    #       "postId": 95221,
    #       "liked": False,
    #       "favorite": False
    #     },
    #     "latitude": 0,
    #     "longitude": 0,
    #     "canComment": False,
    #     "canLike": False,
    #     "canRate": True,
    #     "tags": [
    #       "tag1",
    #       "tag2"
    #     ],
    #     "tagTrees": [],
    #     "name": "محصول ثبت گروهی ۲",
    #     "description": "توضیحات محصول شماره ۲",
    #     "categoryList": [],
    #     "unlimited": True,
    #     "availableCount": 0,
    #     "price": 10000,
    #     "discount": 0,
    #     "attributeValues": [
    #       {
    #         "code": "gender",
    #         "name": "جنسیت",
    #         "value": "دخترانه"
    #       },
    #       {
    #         "code": "size",
    #         "name": "اندازه",
    #         "value": "M"
    #       },
    #       {
    #         "code": "color",
    #         "name": "رنگ",
    #         "value": "قرمز"
    #       }
    #     ],
    #     "allowUserInvoice": False,
    #     "allowUserPrice": False,
    #     "templateCode": "مانتو",
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     }
    #   }
    # ]
except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
