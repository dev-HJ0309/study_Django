import os
import django
from django.test import TestCase

from product.models import Product

# Create your tests here.

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()
#
#
class ProductTest(TestCase):

    def test_save(self):
        product = Product.objects.create(
            product_name='pizza',
            product_stock='120'
        )
        product.save()
#         # 저장을 먼저 하고 출력하자
#
#         # print(Product.objects.get(id=1))
#         print(product)
        # product = Product(product_name='pizza',
        #                   product_stock='120',

        # select id, member_email, member_password, member_name, member_age, member_status from tbl_member
        # print(Product.objects.get(id=1))

    # def test_bulk_create(self):
    #     Product.objects.bulk_create([
    #         Product(product_name='pizza', product_stock='1000'),
    #         Product(product_name='chicken', product_stock='250'),
    #         Product(product_name='hamburger', product_stock='500'),
    #         Product(product_name='french-fly', product_stock='2500'),
    #         Product(product_name='kimchi-jeon', product_stock='100'),
    #     ])
    #
    #     print(Product.objects.values('product_stock'))
    #     print(Product.objects.values_list('product_stock'))
    #     # print(list(Member.objects.all()))
    #     print(Member.objects.values('member_email').query)
    #     print(Member.objects.values('member_email'))
    #     print(Member.objects.values_list('member_email'))
    #
    #     for i in Member.objects.values_list('member_email'):
    #         print(i)
    #
    #
# ----------------------test_get_or_create----------------------------------------

    # def test_get_or_create(self):
    #     product = Product.objects.get_or_create(product_name='chicken', product_stock= 15000)
    #     print(product)


# filter------------------------------------------------------------------------
#     def test_filter(self):
#         Product.objects.bulk_create([
#             Product(product_name='pizza', product_stock=1000),
#             Product(product_name='chicken', product_stock=250),
#             Product(product_name='hamburger', product_stock=500),
#             Product(product_name='french-fly', product_stock=2500),
#             Product(product_name='kimchi-jeon', product_stock=100),
#         ])

        # print(Product.objects.filter(product_name='peach'))
        # 위에 내용에 없는 것은 빈 쿼리셋이 출력 된다.
        # print(Product.objects.filter(product_name__contains='e'))
        # print(Product.objects.filter(product_name__endswith='er'))
        # print(Product.objects.filter(product_name__in=['chicken', 'bear']))
        # print(Product.objects.filter(product_name__icontains='F').count())
        #         뒤에 .count 쓰면 해당 하는 것의 갯수 출력 된다.
        # print(Product.objects.filter(product_name__startswith='p'))
        #  __startswith = 해당 문자로 시작 하는 것을 가져온다.
        # print(Product.objects.filter(product_name__isnull='e'))
        #   __isnull = 해당 문자가 없는 것을 가져온다.

        # print(Product.objects.first())
        # print(Product.objects.last())

        # print(Product.objects.exclude(product_name='hamburger'))
        # print(Product.objects.exclude(product_name__in=['hamburger', 'pizza']))
        # print(Product.objects.filter(product_name__contains='er')
        #             & Product.objects.filter(product_name__contains='a'))
        # print(Product.objects.filter(product_name__contains='er')
        #       | Product.objects.filter(product_name__contains='f'))
        # print(Product.objects.all().order_by('product_name'))
        # # 가나다 순으로 정렬!
        # print(Product.objects.all().order_by('-id'))
        # # 내림 차순
        #
        # print(Product.objects.values('product_name').annotate(count=Count('id')))

# AND, OR
# ======================================
#       print(Product.objects.filter(product_name__contains='test')
#             & Product.objects.filter(product_stock__isnull=''))
#       print(Product.objects.filter(member_email__contains='test')
#             | Product.objects.filter(member_age__lte=30))
#       print(Product.objects.filter(member_email__contains='test', member_age__lte=30))
#
#       condition1 = Q(member_email__contains='test')
#       condition2 = Q(member_age__lte=30)
#
#       print(Product.objects.filter(condition1 | condition2))

# print(Member.objects.all().order_by('member_name'))
# print(Member.objects.all().order_by('-id'))


    # Meta 클래스에서 ordering = ['-id']로 설정
    # print(Member.objects.all())
    # ======================================
    # annotate()
    # ======================================
    # def test_annotate(self):
    #     Product.objects


    # values()를 사용하고 annotate()를 사용하면 추가 연산에 대한 결과 컬럼을 만들 수 있고
    # annotate()를 사용하고 values를 사용하면 기존 컬럼을 다른 이름으로 변경할 수 있다.
    # print(Member.objects.annotate(email=F('member_email')).values('email', 'member_name'))
    # print(Member.objects.annotate(age=F('member_age') - 1).values('member_name', 'age'))
    # print(Member.objects.values('member_age').annotate(count=Count('id')))
    # 회원의 이용 상태 별 명 수
    # for i in list(Member.objects.values('member_status').annotate(member_count=Count('id'))):
    #     print('이용가능' if i['member_status'] else '이용불가', f'{i["member_count"]}명')

    # ======================================
    # aggregate
    # ======================================
    # print(Member.objects.aggregate(total_count=Sum('id'))['total_count'] + 10)
    # for i in list(Member.objects.annotate(name=F('member_name'))):
    #     print(i.name)

    # annotate()는 QuerySet 객체로 리턴하기 때문에 뒤에 이어서 filter() 등을 사용할 수 있으며,
    # 개별 행 처리이므로 전체 집계가 불가능하다.
    # aggregate()는 전체를 대상으로 집계하며, 뒤에 이어서 다른 절을 사용할 수 없다.
    # print(Member.objects.aggregate(max_age=Max('member_age')))
    # print(Member.objects.aggregate(min_age=Min('member_age')))
    # print(Member.objects.aggregate(max_age=Max('member_age'), min_age=Min('member_age')))



from django.test import TestCase

from cart.models import Cart
from member.models import Member
from product.models import Product


# Create your tests here.
class ProductTest(TestCase):
    Product.objects.create(product_name='볼펜', product_price='800', product_stock='100')
    Product.objects.create(product_name='키보드', product_price='1500', product_stock='215')
    Product.objects.create(product_name='마우스', product_price='2000', product_stock='50')
    pass








