from django.utils.text import slugify
import random
import string

def unique_slug_generator(instance, new_slug = None):
    """..."""
    def random_string_generator_for_slug (size = 10, chars = string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug = slug).exists()
    if qs_exists:
        new_slug = "{slug}.{randstr}".format(
            slug=slug,
            randstr = random_string_generator_for_slug(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug