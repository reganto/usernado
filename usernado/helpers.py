__all__ = [
    "Pluralize",
    "humanize",
    "api_route",
]

from typing import Optional, Dict, Any, Callable, List
import functools

import pendulum
import tornado.web
import usernado


class Pluralize(tornado.web.UIModule):
    """Pluralize a string based on a value.

    You Must set ``Pluralize`` as a valid UIModule
    In ``ui_modules`` setting like so

    .. code-block:: python

       ui_modules=dict('pluralize': Pluralize)

    and then use this uimoduele in templates like so

    .. code-block:: html

       {% module pluralize(post, post_counts) %}
    """

    IRREGULAR_NOUNS: Dict[str, str] = {
        "woman": "women",
        "man": "men",
        "child": "children",
        "tooth": "teeth",
        "foot": "feet",
        "person": "people",
        "leaf": "leaves",
        "mouse": "mice",
        "goose": "geese",
        "half": "halves",
        "knife": "knives",
        "wife": "wives",
        "life": "lives",
        "elf": "elves",
        "loaf": "loaves",
        "potato": "potatoes",
        "tomato": "tomatoes",
        "cactus": "cacti",
        "focus": "foci",
        "fungus": "fungi",
        "nucleus": "nuclei",
        "syllabus": "syllabuses",
        "analysis": "analyses",
        "diagnosis": "diagnoses",
        "oasis": "oases",
        "thesis": "theses",
        "crisis": "crises",
        "phenomenon": "phenomena",
        "criterion": "criteria",
        "datum": "data",
    }

    SAME_FORMS: Dict[str, str] = {
        "sheep": "sheep",
        "fish": "fish",
        "deer": "deer",
        "species": "species",
        "aircraft": "aircraft",
    }

    def render(self, word: str, count: int) -> Optional[str]:
        if count > 1:
            if word in self.IRREGULAR_NOUNS:
                return self.IRREGULAR_NOUNS.get(word)
            elif word in self.SAME_FORMS:
                return self.SAME_FORMS.get(word)
            elif word.endswith(("s", "x", "z", "ch", "sh")):
                return f"{word}es"
            elif word[-2] not in ["o", "u", "e", "i", "a"] and word.endswith("y"):  # noqa E501
                return f"{word[:len(word)-1]}ies"
            else:
                return f"{word}s"
        return word


def humanize(func: Callable[..., Any]) -> Callable[..., Any]:
    """Humanize datetime in templates.

    To use ``humanize`` you have to create a DateTimeField
    in your model then create a method in your model decorated with
    ``humanize`` like so

    .. code-block:: python

       @humanize
       def diff_for_humans(self):
           return self.created_at

    then use ``humanize`` in your templates like so::


       {{ obj.diff_for_humans() }}
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        field = func(*args, **kwargs)
        # replace naive datetime tzinfo with pendulum tzinfo
        # naive datetime(is not comparable)
        # timezone aware datetime(is comparable)
        local_timezone = pendulum.tz.get_local_timezone()
        field = field.replace(tzinfo=local_timezone)
        result = pendulum.now().diff_for_humans(field)
        result = result.split(" ")
        for word in result:
            if word == "after":
                result.remove(word)
        # TODO: Needs attention
        return " ".join([w for w in result])

    return wrapper


class _Route(object):
    """Usernado API router class.

    You can decorate :ref:`apihandler` inherited classes with ``api_route`` decorator.

    .. seealso:: For further information take a look at `examples <https://github.com/reganto/usernado/tree/master/example>`_
    """

    urls: List[tornado.web.URLSpec] = []

    def __call__(self, url: str, name: Optional[str] = None) -> Callable[..., Any]:  # noqa: E501
        def wrapper(cls: usernado.APIHandler) -> usernado.APIHandler:
            self.urls.append(
                tornado.web.URLSpec(
                    url,
                    cls,
                    name=name if name else cls.__name__.lower(),
                )
            )
            return cls

        return wrapper


api_route = _Route()
