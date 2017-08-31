import factory
from django.contrib.auth import get_user_model

from accounts.factories.email_address_factory import EmailAddressFactory


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: "username{}".format(n))
    email = factory.Faker(provider='email')
    password = 'password123'
    first_name = factory.Faker(provider='first_name')
    last_name = factory.Faker(provider='last_name')

    is_superuser = True
    is_staff = True
    is_active = True

    raw_password = password

    class Meta:
        model = get_user_model()
        exclude = ('raw_password',)

    @classmethod
    def _create(cls, model_class, verified=True, *args, **kwargs):
        user = super(UserFactory, cls)._create(model_class, *args, **kwargs)

        user.raw_password = user.password
        user.set_password(user.raw_password)
        user.save()

        EmailAddressFactory(user=user, email=user.email, verified=verified)

        return user
