import functools

import pendulum


def humanize(func):
    """Humanize datetime in templates

    example:

        class Post(Model):
            title = CharField(max_length=200)
            created_at = DateTimeField(default=datetime.now)

            @humanize
            def diff_for_humans(self):
                return self.created_at

    Then you can use it in templates like so:

        <p>This post was published {{ post.diff_for_humans() }} ago.</p>
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