from rest_framework import serializers
from django.contrib.auth.models import User
from diap.models.person import Person, PersonImage, PersonText, PersonPlaceWhereHeWas, PersonSocialNetwork
from diap.models.choices import PersonTypeSocialNetworkChoices


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTypeSocialNetworkChoices
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PersonImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonImage
        fields = '__all__'


class PersonTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonText
        fields = '__all__'


class PersonPlaceWhereHeWasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonPlaceWhereHeWas
        fields = '__all__'


class PersonSocialNetworkSerializer(serializers.ModelSerializer):
    # type = SocialNetworkSerializer(many=True, read_only=True)
    class Meta:
        model = PersonSocialNetwork
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    images = PersonImageSerializer(many=True, read_only=True)
    texts = PersonTextSerializer(many=True, read_only=True)
    place_where_he_waa = PersonPlaceWhereHeWasSerializer(many=True, read_only=True)
    social_network = PersonSocialNetworkSerializer(many=True, read_only=True)

    user = UserSerializer(read_only=True)

    class Meta:
        model = Person
        fields = '__all__'
