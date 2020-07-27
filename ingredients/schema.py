import graphene
from graphene_django.types import DjangoObjectType

from ingredients.models import Personaje, Pelicula


class PersonajeType(DjangoObjectType):
    class Meta:
        model = Personaje
        filter_fields = ['name']


class PeliculaType(DjangoObjectType):
    class Meta:
        model = Pelicula


class Query(graphene.ObjectType):
    all_personaje = graphene.List(PersonajeType)
    all_pelicula = graphene.List(PeliculaType)

    def resolve_all_personaje(selfself, info, search=None, **kwargs):
        #return Personaje.objects.all()
        if search:
            filter = (
                    Personaje(name__icontains=search)
            )
            return Personaje.objects.filter(filter)

        return Personaje.objects.all()

    def resolve_all_pelicula(self, info, **kwargs):
        return Pelicula.objects.select_related('personaje').all()
