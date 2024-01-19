from rest_framework.response import Response
from rest_framework.views import APIView


class UserProductAPIView(APIView):
    def get(self, request):
        session_key = request.session._get_or_create_session_key()
        print(session_key)
        print('---------------')
        anonymous = request.user.is_anonymous
        user_id = request.user.id
        print(anonymous, user_id)
        return Response({'Attention': 'Tne product has already been added '})

    def post(self, request):
        anonymous = request.user.is_anonymous
        user_id=request.user.id
        print(anonymous, user_id)
        # if
        # data = request.data.copy()
        # user = request.user
        # if not len(user_product.objects.filter(name_product=data['name_product'])):
        #     original_product = product.safe_get(product, data['name_product'])
        #     if original_product is not None:
        #         new_user_product = user_product.objects.create(
        #             name_product=data['name_product'],
        #             total_count= data['total_count'],
        #             calories=data['calories'],
        #             user=user,
        #             product=original_product
        #         )
        #         serializer = UserProductSerializer(new_user_product)
        #         return Response({'post': serializer.data})
        #     new_user_product = user_product.objects.create(
        #         name_product=data['name_product'],
        #         total_count=data['total_count'],
        #         calories=data['calories'],
        #         user=user,
        #         product=None
        #     )
        #     serializer = UserProductSerializer(new_user_product)
        #     return Response({'post': serializer.data})
        # else:
        #     return Response({'Attention': 'Tne product has already been added '})
