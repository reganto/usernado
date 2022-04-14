__all__ = [
    "Pluralize",
    "humanize",
    "api_route",
]

import functools

import pendulum
import tornado.web


class Pluralize(tornado.web.UIModule):
    """Pluralize a string based on a value.

    You Must set `Pluralize` as a valid UIModule
    In `ui_modules` setting like so.

    ui_modules=dict(
        'pluralize': Pluralize,
    )
    """

    def render(self, word: str, count: int) -> str:
        if count > 1:
            if word.endswith(("s", "x", "z", "ch", "sh")):
                return f"{word}es"
            elif word.endswith("y"):
                return f"{word[:len(word)-1]}ies"
            else:
                # TODO: implement other forms of word pluralization
                return f"{word}s"
        return word


def humanize(func):
    """Humanize datetime in templates.

    Take a look at example directory.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
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
        return " ".join([w for w in result])

    return wrapper


class Route(object):
    """Usernado API router class."""

    urls = []

    def __call__(self, url: str, name: str = None):
        def wrapper(cls):
            self.urls.append(
                tornado.web.URLSpec(
                    url, cls, name=name if name else cls.__name__.lower()
                )
            )
            return cls

        return wrapper


api_route = Route()
