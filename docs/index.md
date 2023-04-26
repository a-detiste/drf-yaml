<div class="badges">
    <img src="https://img.shields.io/github/checks-status/Qu4tro/django-rest-framework-yaml/main">
  <a href="https://pypi.python.org/pypi/drf-yaml">
    <img src="https://img.shields.io/pypi/v/drf-yaml.svg">
  </a>
</div>

---

# REST Framework YAML

YAML support for Django REST Framework

---

## Overview

YAML support for the Django REST Framework, forked from [https://github.com/jpadilla/django-rest-framework-yaml][original].

## Requirements

* Python (3.8, 3.9, 3.10, 3.11)
* Django (3.2, 4.*)

## Installation

Install using `pip`...

```bash
$ pip install drf-yaml
```

## Example

```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'drf_yaml.parsers.YAMLParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'drf_yaml.renderers.YAMLRenderer',
    ),
}
```

You can also set the renderer and parser used for an individual view, or viewset, using the APIView class based views.

```python
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yaml.parsers import YAMLParser
from drf_yaml.renderers import YAMLRenderer

class ExampleView(APIView):
    """
    A view that can accept POST requests with YAML content.
    """
    parser_classes = (YAMLParser,)
    renderer_classes = (YAMLRenderer,)

    def post(self, request, format=None):
        return Response({'received data': request.DATA})
```

### Sample output

```yaml
---
-
  email: jpadilla@example.com
  is_staff: true
  url: "http://127.0.0.1:8000/users/1/"
  username: jpadilla
```

## Testing

Install testing requirements.

```bash
$ poetry install
```

Run with pytest.

```bash
$ poetry run pytest
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ poetry install --only docs
```

To preview the documentation:

```bash
$ poetry run mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```
$ poetry run mkdocs build
```

[original]: https://github.com/jpadilla/django-rest-framework-yaml
