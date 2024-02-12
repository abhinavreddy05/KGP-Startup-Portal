import graphene
from graphene import Field
from graphql_auth.schema import MeQuery
from graphql_auth import mutations

from graphene_django.types import DjangoObjectType
import users.models

from graphene_django.forms.mutation import DjangoModelFormMutation

from .models import StartupModel, MentorModel
from .forms import StartupForm, MentorForm

class Startup(DjangoObjectType):
    class Meta:
        model = StartupModel
        fields = "__all__"

class Mentor(DjangoObjectType):
    class Meta:
        model = MentorModel
        fields = "__all__"

class StartupMutation(DjangoModelFormMutation):
    startup = Field(Startup)

    class Meta:
        form_class = StartupForm

    @classmethod
    def perform_mutate(cls, form, info):
        if info.context.user.user_type == "startup":
            form.instance.user = info.context.user
            return super().perform_mutate(form, info)
        else:
            raise Exception("User is not a startup")
  
class MentorMutation(DjangoModelFormMutation):
    mentor = Field(Mentor)

    class Meta:
        form_class = MentorForm

    @classmethod
    def perform_mutate(cls, form, info):
        form.instance.user = info.context.user
        return super().perform_mutate(form, info)

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    verify_token = mutations.VerifyToken.Field()
    revoke_token = mutations.RevokeToken.Field()

class Query(MeQuery, graphene.ObjectType):
    startups = graphene.List(Startup)
    def resolve_startups(self,info, **kwargs):
        return StartupModel.objects.all()
    mentors = graphene.List(Mentor)
    def resolve_mentors(self,info, **kwargs):
        return MentorModel.objects.all()

class Mutation(AuthMutation, graphene.ObjectType):
    create_startup = StartupMutation.Field()
    create_mentor = MentorMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)