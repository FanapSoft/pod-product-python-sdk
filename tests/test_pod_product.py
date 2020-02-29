# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_base import InvalidDataException

from pod_product import PodProduct
from tests.config import *
from datetime import datetime


class TestPodSubscription(unittest.TestCase):
    __slots__ = "__product"

    def setUp(self):
        self.__product = PodProduct(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_01_add_product(self):
        name = "محصول تستی {}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        price = 125.001
        result = self.__product.add_product(name=name, price=price, description="توضیحات محصول", available_count=20)
        self.assertIsInstance(result, dict, msg="add product : check instance")
        self.assertEqual(result["name"], name, msg="add product : check name")
        self.assertEqual(result["price"], price, msg="add product : check price")
        self.assertEqual(result["availableCount"], 20, msg="add product : check available count")
        self.assertEqual(result["enable"], True, msg="add product : check enable")
        self.assertEqual(result["canComment"], True, msg="add product : check canComment")

    def test_01_add_product_all_params(self):
        name = "محصول تستی {}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        unique_id = datetime.now().__format__("%s")
        tags = ["tag1", "tag2"]
        preview = "https://miro.medium.com/max/2600/0*WkY7VuAwNf0K5YRz.png"
        other_params = {
            "description": "Python Test",
            "unlimited": False,  # default : True
            "canComment": True,
            "canLike": True,
            "enable": True,
            "discount": 0,
            "guildCode": GUILD_CODE,
            "uniqueId": unique_id,
            "metaData": {"platform": "python", "unittest": True},
            "allowUserInvoice": True,  # default : False
            "allowUserPrice": True,  # default : False
            "currencyCode": "IRR",
            "attTemplateCode": "مانتو",
            "attributes":
                [
                    {
                        "code": "gender",
                        "value": "زنانه",
                        "group": False,
                    },
                    {
                        "code": "color",
                        "value": "قرمز",
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
            "tags": tags,
            "content": "تست محتوای مخفی برای یک محصول",
            "previewImage": preview,
            # "tagTrees": ["Tag tree level 01"],
            # "tagTreeCategoryName": "TestTagCategory5dd13cef16902",
            "preferredTaxRate": 0.09,
            "quantityPrecision": 2
        }

        result = self.__product.add_product(name=name, price=150.08, available_count=1000, **other_params)
        self.assertIsInstance(result, dict, msg="add product (all params): check instance")
        self.assertEqual(result["tags"], tags, msg="add product (all params): check tags")
        self.assertEqual(result["preview"], preview, msg="add product (all params): check preview")

    def test_01_add_product_validation_error(self):
        name = "محصول تستی {}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        unique_id = datetime.now().__format__("%s")
        tags = ["tag1", "tag2"]
        preview = "https://miro.medium.com/max/2600/0*WkY7VuAwNf0K5YRz.png"
        other_params = {
            "description": "Python Test",
            "unlimited": False,  # default : True
            "canComment": True,
            "canLike": True,
            "enable": True,
            "discount": 0,
            "guildCode": GUILD_CODE,
            "uniqueId": unique_id,
            "metaData": '{"platform": "python", "unittest": True}',  # should dict
            "allowUserInvoice": "True",  # should bool
            "allowUserPrice": "True",  # should bool
            "currencyCode": "IRR",
            "attTemplateCode": "مانتو",
            "attributes":
                [
                    {
                        "code": "gender",
                        "value": "زنانه",
                        "group": "False",  # should bool
                    },
                    {
                        "code": "color",
                        "value": "قرمز",
                        "group": "False",  # should bool
                    },
                    {
                        "code": "size",
                        "value": "M",
                        "group": "True",  # should bool
                    }
                ],
            "lat": "43.787568",  # should float
            "lng": "74.9890685",  # should float
            "tags": tags,
            "content": "تست محتوای مخفی برای یک محصول",
            "previewImage": preview,
            # "tagTrees": ["Tag tree level 01"],
            # "tagTreeCategoryName": "TestTagCategory5dd13cef16902",
            "preferredTaxRate": 5,  # should between 0 - 1
            "quantityPrecision": 2
        }

        with self.assertRaises(InvalidDataException, msg="add product : validation error"):
            self.__product.add_product(name=name, price="45500", **other_params)

    def test_01_add_product_required_params(self):
        with self.assertRaises(TypeError, msg="add product : required params"):
            self.__product.add_product()

    def __add_product(self, **kwargs):
        name = "محصول تستی {}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        return self.__product.add_product(product_id=PRODUCT_ID,
                                          name=name,
                                          price=10,
                                          description="محصول تستی برای تست در پایتون",
                                          **kwargs)

    def test_02_add_sub_product_all_params(self):
        product_info = {
            "attTemplateCode": "مانتو",
            "attributes":
                [
                    {
                        "code": "gender",
                        "value": "زنانه",
                        "group": False,
                    },
                    {
                        "code": "color",
                        "value": "قرمز",
                        "group": False,
                    },
                    {
                        "code": "size",
                        "value": "M",
                        "group": True,
                    }
                ],
        }

        product = self.__add_product(**product_info)

        name = "زیر محصول {}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        other_params = {
            "description": "این یک زیر محصول است که سایز آن S است",
            "discount": 0,
            "attributes":
                [
                    {
                        "code": "size",
                        "value": "S",
                        "group": True,
                    }
                ]
        }

        result = self.__product.add_sub_product(group_id=product["productGroup"]["id"], name=name, price=150.08,
                                                available_count=1000,
                                                **other_params)
        self.assertIsInstance(result, dict, msg="add sub product (all params): check instance")
        self.assertEqual(result["name"], name, msg="add sub product (all params): check name")

    def test_02_add_sub_product_validation_error(self):
        name = "محصول تستی {}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        other_params = {
            "description": "Python Test",
            "attributes":
                [
                    {
                        "code": "gender",
                        "value": "زنانه",
                        "group": "False",  # should bool
                    },
                    {
                        "code": "color",
                        "value": "قرمز",
                        "group": "False",  # should bool
                    },
                    {
                        "code": "size",
                        "value": "M",
                        "group": "True",  # should bool
                    }
                ]
        }

        with self.assertRaises(InvalidDataException, msg="add sub product : validation error"):
            self.__product.add_sub_product(group_id="1000", name=name, price="45500", **other_params)

    def test_02_add_sub_product_required_params(self):
        with self.assertRaises(TypeError, msg="add sub product : required params"):
            self.__product.add_sub_product()

    def test_03_add_products(self):
        products = [
            {
                "name": "محصول تستی ۱ {}".format(datetime.now().__format__("%Y%m%d%H%M%S")),
                "price": 1200,
                "description": "افزودن گروهی محصول ۱"
            },
            {
                "name": "محصول تستی ۲ {}".format(datetime.now().__format__("%Y%m%d%H%M%S")),
                "price": 1000,
                "description": "افزودن گروهی محصول ۲"
            }
        ]

        result = self.__product.add_products(products=products)
        self.assertIsInstance(result, list, msg="add products : check instance")
        self.assertEqual(len(result), 2, msg="add products : check length")

    def test_03_add_products_all_params(self):
        tags = ["tag1", "tag2"]
        products = [{
            "name": "محصول گروهی ۱ {}".format(datetime.now().__format__("%Y%m%d%H%M%S")),
            "description": "توضیحات محصول شماره ۱",
            "price": 12500,
            "available_count": 100
        }, {
            "name": "محصول گروهی ۲ {}".format(datetime.now().__format__("%Y%m%d%H%M%S")),
            "description": "توضیحات محصول شماره ۲",
            "price": 10000,
            "unlimited": True,
            "canComment": False,
            "canLike": False,
            "tags": tags,
            "uniqueId": datetime.now().__format__("%s"),
            "metaData": {"unittest": "python"},
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

        result = self.__product.add_products(products=products)
        self.assertIsInstance(result, list, msg="add products (all params): check instance")
        self.assertEqual(len(result), 2, msg="add products (all params): check length")

    def test_03_add_products_validation_error(self):
        name = "محصول تستی {}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        unique_id = datetime.now().__format__("%s")
        tags = ["tag1", "tag2"]
        preview = "https://miro.medium.com/max/2600/0*WkY7VuAwNf0K5YRz.png"
        products = [{
            "name": name,
            "price": 12300,
            "description": "Python Test",
            "unlimited": False,  # default : True
            "canComment": True,
            "canLike": True,
            "enable": True,
            "discount": 0,
            "guildCode": GUILD_CODE,
            "uniqueId": unique_id,
            "metaData": '{"platform": "python", "unittest": True}',  # should dict
            "allowUserInvoice": "True",  # should bool
            "allowUserPrice": "True",  # should bool
            "currencyCode": "IRR",
            "attTemplateCode": "مانتو",
            "attributes":
                [
                    {
                        "code": "gender",
                        "value": "زنانه",
                        "group": "False",  # should bool
                    },
                    {
                        "code": "color",
                        "value": "قرمز",
                        "group": "False",  # should bool
                    },
                    {
                        "code": "size",
                        "value": "M",
                        "group": "True",  # should bool
                    }
                ],
            "lat": "43.787568",  # should float
            "lng": "74.9890685",  # should float
            "tags": tags,
            "content": "تست محتوای مخفی برای یک محصول",
            "previewImage": preview,
            # "tagTrees": ["Tag tree level 01"],
            # "tagTreeCategoryName": "TestTagCategory5dd13cef16902",
            "preferredTaxRate": 5,  # should between 0 - 1
            "quantityPrecision": 2
        }]

        with self.assertRaises(InvalidDataException, msg="add products : validation error"):
            self.__product.add_products(products=products)

    def test_03_add_products_required_params(self):
        with self.assertRaises(TypeError, msg="add products : required params"):
            self.__product.add_products()

    def test_04_update_product(self):
        product = self.__add_product()
        name = "محصول ویرایش شده"
        price = 16.07

        result = self.__product.update_product(entity_id=product["entityId"], name=name, price=price,
                                               description="توضیحات محصول ویرایش شده", available_count=20)

        self.assertIsInstance(result, dict, msg="update product : check instance")
        self.assertEqual(result["name"], name, msg="update product : check name")
        self.assertEqual(result["price"], price, msg="update product : check price")
        self.assertEqual(result["availableCount"], 20, msg="update product : check available count")
        self.assertEqual(result["enable"], True, msg="update product : check enable")
        self.assertEqual(result["canComment"], True, msg="update product : check canComment")

    def test_04_update_product_all_params(self):
        product = self.__add_product()

        name = "محصول ویرایشی"
        unique_id = "edited_" + datetime.now().__format__("%s")
        tags = ["tag1", "tag2", "tag3"]
        preview = "https://miro.medium.com/max/2600/0*WkY7VuAwNf0K5YRz.png"
        other_params = {
            "description": "Python Test",
            "unlimited": False,  # default : True
            "canComment": True,
            "canLike": True,
            "enable": True,
            "discount": 0,
            "guildCode": GUILD_CODE,
            "uniqueId": unique_id,
            "metaData": {"platform": "python", "unittest": True},
            "allowUserInvoice": True,  # default : False
            "allowUserPrice": True,  # default : False
            "currencyCode": "IRR",
            "attTemplateCode": "مانتو",
            "attributes":
                [
                    {
                        "code": "gender",
                        "value": "زنانه",
                        "group": False,
                    },
                    {
                        "code": "color",
                        "value": "قرمز",
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
            "tags": tags,
            "content": "تست محتوای مخفی برای یک محصول",
            "previewImage": preview,
            # "tagTrees": ["Tag tree level 01"],
            # "tagTreeCategoryName": "TestTagCategory5dd13cef16902",
            "preferredTaxRate": 0.09,
            "quantityPrecision": 2
        }

        result = self.__product.update_product(entity_id=product["entityId"], name=name, price=150.08,
                                               available_count=1000, **other_params)

        self.assertIsInstance(result, dict, msg="update product (all params): check instance")
        self.assertEqual(result["tags"], tags, msg="update product (all params): check tags")

    def test_04_update_product_validation_error(self):
        name = "محصول تستی {}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        other_params = {
            "description": "Python Test",
            "unlimited": False,  # default : True
            "canComment": True,
            "canLike": True,
            "enable": True,
            "discount": 0
        }

        with self.assertRaises(InvalidDataException, msg="update product : validation error"):
            self.__product.update_product(entity_id=12346, name=name, price="45500", **other_params)

    def test_04_update_product_required_params(self):
        with self.assertRaises(TypeError, msg="update product : required params"):
            self.__product.update_product()

    def test_05_update_products(self):
        products = [
            self.__add_product(),
            self.__add_product()
        ]

        edited_products = [
            {
                "entityId": products[0]["entityId"],
                "name": "{} ویرایش شد".format(products[0]["name"]),
                "price": 10000,
                "description": "توضیحات محصول اول رو ویرایش می کنیم",
                "unlimited": True
            },
            {
                "entityId": products[1]["entityId"],
                "name": "محصول تستی ۲ - ویرایشی {}".format(datetime.now().__format__("%Y%m%d%H%M%S")),
                "price": 800,
                "description": "اسم و قیمت و متادیتا رو ویرایش کردم",
                "metaData": {"edited": True},
                "availableCount": 1000
            }
        ]

        result = self.__product.update_products(products=edited_products)
        self.assertIsInstance(result, list, msg="update products : check instance")
        self.assertEqual(len(result), 2, msg="update products : check length")

    def test_05_update_products_all_params(self):
        products = [
            self.__add_product(),
            self.__add_product()
        ]

        products = [{
            "entityId": products[0]["entityId"],
            "name": "محصول تستی ویرایش شده - گروهی",
            "price": 1607,
            "description": "این محصول رو به صورت گروهی هم ویرایش کردیم",
            "availableCount": 10000
        }, {
            "entityId": products[1]["entityId"],
            "name": "اینم ویرایش شد",
            "price": 16007,
            "description": "این را نیز ویرایش کردیم",
            "unlimited": False,
            "canComment": True,
            "canLike": True
        }]

        result = self.__product.update_products(products=products)
        self.assertIsInstance(result, list, msg="update products (all params): check instance")
        self.assertEqual(len(result), 2, msg="update products (all params): check length")

    def test_05_update_products_validation_error(self):
        products = [{
            "entityId": "45000",
            "name": "محصول تستی ویرایش شده - گروهی",
            "price": "1607.005",
            "description": "این محصول رو به صورت گروهی هم ویرایش کردیم",
            "availableCount": "10000"
        }, {
            "entityId": "1203",
            "name": "اینم ویرایش شد",
            "price": "16007",
            "description": "این را نیز ویرایش کردیم",
            "unlimited": "False",
            "canComment": "True",
            "canLike": "True"
        }]

        with self.assertRaises(InvalidDataException, msg="update products : validation error"):
            self.__product.update_products(products=products)

    def test_05_update_products_required_params(self):
        with self.assertRaises(TypeError, msg="update products : required params"):
            self.__product.update_products()

    def test_06_get_product_list(self):
        result = self.__product.get_product_list()
        self.assertIsInstance(result, list, msg="get product list : check instance")

    def test_06_get_product_list_all_params(self):
        params = {
            "id": [49179, 49032],
            "attributes": [{
                "code": "size",
                "value": "M"
            }],
            "businessId": 7867,
            "guildCode": [GUILD_CODE],
            "currencyCode": "USD",
            # "uniqueId": ["123"],
            # "relatedProductsId": [123, 456],
            "size": 5,
            "tags": ["tag1"],
            # "tagTrees": ["tag1"],
            # "tagTreeCategoryName": ["tag1"],
            # "orderByPrice": "asc",  #  asc or desc
            # "orderBySale": "asc",  #  asc or desc
            # "orderByLike": "asc",  #  asc or desc
        }
        result = self.__product.get_product_list(**params)
        self.assertIsInstance(result, list, msg="get product list (all params): check instance")

    def test_06_get_product_list_validation_error(self):
        params = {
            "id": "abcd",
            "attributes": "asdasdasd",
            "businessId": "7867",
            "guildCode": GUILD_CODE,
            "currencyCode": "USD",
            # "uniqueId": ["123"],
            # "relatedProductsId": [123, 456],
            "size": 5,
            "tags": ["tag1"],
            # "tagTrees": ["tag1"],
            # "tagTreeCategoryName": ["tag1"],
            # "orderByPrice": "asc",  #  asc or desc
            # "orderBySale": "asc",  #  asc or desc
            # "orderByLike": "asc",  #  asc or desc
        }

        with self.assertRaises(InvalidDataException, msg="get product list : validation error"):
            self.__product.get_product_list(**params)

    def test_07_get_business_product_list(self):
        result = self.__product.get_business_product_list()
        self.assertIsInstance(result, list, msg="get business product list : check instance")

    def test_07_get_business_product_list_all_params(self):
        params = {
            "id": [49179, 49032],
            "attributes": [{
                "code": "size",
                "value": "M"
            }],
            "attributeTemplateCode": "مانتو",
            "businessId": 7867,
            "guildCode": [GUILD_CODE],
            "currencyCode": "USD",
            "uniqueId": ["123"],
            "relatedProductsId": [123, 456],
            "size": 5,
            "scope": PodProduct.SCOPE_DEALER_PRODUCT_PERMISSION,  # PodProduct.SCOPE_BUSINESS_PRODUCT (default) or
            #                                                        # PodProduct.SCOPE_PARENT_PRODUCT or
            #                                                        # PodProduct.SCOPE_DEALER_PRODUCT_PERMISSION
            #
            # "attributeSearchQuery": [{
            #     "field": "name",
            #     "is": "reza"
            # }],
            "tags": ["tag1"],
            "tagTrees": ["tag1"],
            "tagTreeCategoryName": ["tag1"],
            "orderByPrice": "asc",  # asc or desc
            "orderBySale": "asc",  # asc or desc
            "orderByLike": "asc",  # asc or desc
        }
        result = self.__product.get_business_product_list(**params)
        self.assertIsInstance(result, list, msg="get business product list : check instance")

    def test_07_get_business_product_list_validation_error(self):
        params = {
            "id": "123456",
            "attributes": [{
                "code": "size",
                "value": "M"
            }],
            "attributeTemplateCode": "مانتو",
            "businessId": "7867",
            "guildCode": [GUILD_CODE],
            "currencyCode": "USD",
            "uniqueId": ["123"],
            "relatedProductsId": ["123", "456"],
            "size": 5,
            "scope": PodProduct.SCOPE_DEALER_PRODUCT_PERMISSION,  # PodProduct.SCOPE_BUSINESS_PRODUCT (default) or
            #                                                        # PodProduct.SCOPE_PARENT_PRODUCT or
            #                                                        # PodProduct.SCOPE_DEALER_PRODUCT_PERMISSION
            #
            # "attributeSearchQuery": [{
            #     "field": "name",
            #     "is": "reza"
            # }],
            "tags": ["tag1"],
            "tagTrees": ["tag1"],
            "tagTreeCategoryName": ["tag1"],
            "orderByPrice": "asc",  # asc or desc
            "orderBySale": "asc",  # asc or desc
            "orderByLike": "asc",  # asc or desc
        }
        with self.assertRaises(InvalidDataException, msg="get business product list : validation error"):
            self.__product.get_business_product_list(**params)

    def test_08_get_attribute_template_list(self):
        result = self.__product.get_attribute_template_list()
        self.assertIsInstance(result, list, msg="get attribute template list : check instance")

    def test_08_get_attribute_template_list_all_params(self):
        params = {
            "guildCode": ["CLOTHING_GUILD"],
            "attributeTemplateCode": ["مانتو", "پیراهن مردانه"],
            "firstId": 0,
            # "lastId": 0,
            # "page": 1,
            "size": 50
        }
        result = self.__product.get_attribute_template_list(**params)
        self.assertIsInstance(result, list, msg="get attribute template list (all params) : check instance")

    def test_08_get_attribute_template_list_validation_error(self):
        params = {
            "guildCode": "asdasd",
            # "attributeTemplateCode": ["مانتو", "پیراهن مردانه"],
            "firstId": "0",
            # "lastId": 0,
            # "page": 1,
            "size": 50
        }
        with self.assertRaises(InvalidDataException, msg="get attribute template list : validation error"):
            self.__product.get_attribute_template_list(**params)

    def test_09_search_product(self):
        result = self.__product.search_product()
        self.assertIsInstance(result, dict, msg="search product : check instance")
        self.assertIsInstance(result["products"], list, msg="search product : check products instance")

    def test_09_search_product_all_params(self):
        params = {
            "q": "محصول",
            "id": [49342],
            "uniqueId": ["abc"],
            "relatedProductsId": [],
            "businessId": 7867,
            "guildCode": ["CLOTHING_GUILD"],
            "currencyCode": "IRR",
            "attributes": [
                {
                    "code": "size",
                    "value": "M"
                },
                {
                    "code": "size",
                    "value": "L"
                }
            ],
            "attributeTemplateCode": "مانتو",
            "tags": ["tag1"],
            "tagTreeCategoryName": ["tagname1"],
            "tagTrees": ["tagname"],
            "orderByLike": "desc",  # asc or desc
            "orderBySale": "asc",  # asc or desc
            "orderByPrice": "asc",  # asc or desc
            # "firstId": 0,
            # "lastId": 0,
            "page": 1,
            "size": 2
        }
        result = self.__product.search_product(**params)
        self.assertIsInstance(result, dict, msg="search product (all params): check instance")
        self.assertIsInstance(result["products"], list,
                              msg="search product (all params): check products instance")

    def test_09_search_product_validation_error(self):
        params = {
            "id": ["49342"],
            "uniqueId": ["abc"],
            "businessId": "7867",
            "orderByLike": "asdas",  # asc or desc
            "orderBySale": "adasdasdsc",  # asc or desc
            "orderByPrice": "dsafd",  # asc or desc
        }
        with self.assertRaises(InvalidDataException, msg="search product : validation error"):
            self.__product.search_product(**params)

    def test_10_search_sub_product(self):
        product_info = {
            "attTemplateCode": "مانتو",
            "attributes":
                [
                    {
                        "code": "gender",
                        "value": "دخترانه",
                        "group": False,
                    },
                    {
                        "code": "color",
                        "value": "قرمز",
                        "group": False,
                    },
                    {
                        "code": "size",
                        "value": "M",
                        "group": True,
                    }
                ],
        }

        product = self.__add_product(**product_info)

        params = {
            "q": "اطلاعات",
            # "tags": ["tag1"],
            # "tagTrees": ["tagname"],
            # "orderByAttributeCode": "size",  # asc or desc
            # "orderByDirection": "desc",  # asc or desc
            "page": 1,
            "size": 2
        }
        result = self.__product.search_sub_product(product_group_id=[product["productGroup"]["id"]], **params)
        self.assertIsInstance(result, list, msg="search sub product : check instance")

    def test_10_search_sub_product_validation_error(self):
        params = {
            # "q": "اطلاعات",
            # "tags": ["tag1"],
            # "tagTrees": ["tagname"],
            "orderByAttributeCode": "size",  # asc or desc
            "orderByDirection": "asdasd",  # asc or desc
        }
        with self.assertRaises(InvalidDataException, msg="search sub product : validation error"):
            self.__product.search_sub_product(product_group_id="123", **params)

    def test_10_search_sub_product_required_params(self):
        with self.assertRaises(TypeError, msg="search sub product : required param"):
            self.__product.search_sub_product()
