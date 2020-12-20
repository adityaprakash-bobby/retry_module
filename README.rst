============
Retry Module
============


.. image:: https://img.shields.io/pypi/v/retry_module.svg
        :target: https://pypi.python.org/pypi/retry_module

.. image:: https://img.shields.io/travis/adityaprakash-bobby/retry_module.svg
        :target: https://travis-ci.com/adityaprakash-bobby/retry_module

.. image:: https://readthedocs.org/projects/retry-module/badge/?version=latest
        :target: https://retry-module.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/adityaprakash-bobby/retry_module/shield.svg
     :target: https://pyup.io/repos/github/adityaprakash-bobby/retry_module/
     :alt: Updates



A simple decorator for implementing retry mechanishm


* Free software: MIT license
* Documentation: https://retry-module.readthedocs.io.


Installation and Usage
----------------------

* Install it using `pip`

```bash
pip install retry_module
```

* Use the `retry` decorator to retry functions on exception.

```python
from retry_module.decorators import retry
from random import random

@retry(SomeError, max_retries=10)
def func():
    random_num = random()
    if random_num < 0.6:
        return "Yaay!"
    else:
        raise SomeError("There you go!")
```

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
