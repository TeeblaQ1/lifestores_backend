
# Create your tests here.
import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from graphene.test import Client
 
from products.models import Product
from products.schema import schema

products_list_query = """
    query {
        allProducts {
            name
            description
            sku
            price
            image
        }
    }
"""

single_product_query = """
    query($id:Int) {
        product(productId: $id) {
            id
            name
            description
            sku
            price
            image
        }
    }
"""

create_product_mutation = """
     mutation CreateMutation($input: ProductInput!) {
        createProduct(productData: $input) {
            product {
                name
                description
                sku
                price
                image
            }
        }
    }
"""

update_product_mutation = """
     mutation UpdateMutation($input: ProductInput!) {
        updateProduct(productData: $input) {
            product {
                name
                description
                sku
                price
                image
            }
        }
    }
"""
 
delete_product_mutation = """
    mutation deleteMutation($id:ID) {
        deleteProduct(id: $id) {
            product {
                id
            }
        }
    }
"""


@pytest.mark.django_db
class TestProductsSchema(TestCase):
 
    def setUp(self):
        self.client = Client(schema)
        self.product = mixer.blend(Product)
 
    def test_single_product_query(self):
        response = self.client.execute(single_product_query, variable_values={"id": self.product.id})
        response_product = response.get("data").get("product")
        assert response_product["id"] == str(self.product.id)

 
    def test_products_list_query(self):
        mixer.blend(Product)
 
        response = self.client.execute(products_list_query)
        products = response.get("data").get("allProducts")
        ok = response.get("data").get("ok")
         
        assert len(products)
 
    def test_create_blog(self):
        payload = {
            "name": "How to test GraphQL with pytest",
            "description": "Testing description",
            "sku": "This is the example of functional testing.",
            "price": 1000,
            "image": "sdfdklsaosidnf"
        }
 
        response = self.client.execute(create_product_mutation, variable_values={"input": payload})
        product = response.get("data").get("createProduct").get("product")
        name = product.get("name")
        assert name == payload["name"]
 
    def test_update_blog(self):
        payload = {
            "id": self.product.id,
            "name": "How to test GraphQL update mutation with pytest",
            "description": self.product.description,
            "sku": self.product.sku,
            "price": self.product.price,
            "image": self.product.image
        }
 
        response = self.client.execute(update_product_mutation, variable_values={"input": payload})
 
        response_product = response.get("data").get("updateProduct").get("product")
        name = response_product.get("name")
        assert name == payload["name"]
        assert name != self.product.name 
 
    def test_delete_product(self):
        response = self.client.execute(delete_product_mutation, variable_values={"id": self.product.id})
        assert response.get("data").get("deleteProduct") == None

