# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_product import PodProduct

try:
    pod_product = PodProduct(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        "guildCode": ["CLOTHING_GUILD"],
        # "attributeTemplateCode": ["مانتو", "پیراهن مردانه"],
        "firstId": 0,
        # "lastId": 0,
        # "page": 1,
        "size": 50
    }

    print(pod_product.get_attribute_template_list(**params))
    print("Total :", pod_product.total_items())
    # OUTPUT
    # [
    #   {
    #     "name": "پیراهن مردانه",
    #     "code": "پیراهن مردانه",
    #     "attributes": [
    #       {
    #         "id": 2,
    #         "name": "جنسیت",
    #         "code": "gender"
    #       },
    #       {
    #         "id": 3,
    #         "name": "اندازه",
    #         "code": "size"
    #       },
    #       {
    #         "id": 4,
    #         "name": "رنگ",
    #         "code": "color"
    #       }
    #     ]
    #   },
    #   {
    #     "name": "پیراهن مجلسی",
    #     "code": "پیراهن مجلسی",
    #     "attributes": [
    #       {
    #         "id": 2,
    #         "name": "جنسیت",
    #         "code": "gender"
    #       },
    #       {
    #         "id": 3,
    #         "name": "اندازه",
    #         "code": "size"
    #       },
    #       {
    #         "id": 4,
    #         "name": "رنگ",
    #         "code": "color"
    #       }
    #     ]
    #   },
    #   ...
    # ]
    # Total : 23

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
