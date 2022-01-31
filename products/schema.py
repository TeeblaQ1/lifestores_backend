from itertools import product
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, product_id=graphene.Int())

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()
    
    def resolve_product(self, info, product_id):
        return Product.objects.get(pk=product_id)


class ProductInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    sku = graphene.String()
    price = graphene.Int()
    image = graphene.String()


class CreateProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)
    
    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, product_data=None):
        product_instance = Product(
            name=product_data.name,
            description=product_data.description,
            sku=product_data.sku,
            price=product_data.price,
            image=product_data.image
        )
        product_instance.save()
        return CreateProduct(product=product_instance)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, product_data=None):
        product_instance = Product.objects.get(pk=product_data.id)

        if product_instance:
            product_instance.name = product_data.name
            product_instance.description = product_data.description
            product_instance.sku = product_data.sku
            product_instance.price = product_data.price
            product_instance.image = product_data.image
            product_instance.save()

            return UpdateProduct(product=product_instance)
        return UpdateProduct(product=None)


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, id):
        product_instance = Product.objects.get(pk=id)
        product_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)