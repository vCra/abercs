AberCompSoc
===========

Welcome to Code for The website of AberCompSoc

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: GPLv3



How to get started
^^^^^^

For development, you can use docker - simply clone this repo, and run docker-compose -f local.yml up
If you are using IDEA/pycharm, you can use the dockerfile as an environment, and all of the requirements will be built automatically

We use Gulp for front end resource management (minification etc...) - you will need to have NPM installed on your local machine to get this running

Custom Bootstrap Compilation
^^^^^^

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v4.1.3 is installed using npm and customised by tweaking your variables in ``static/sass/custom_bootstrap_vars``.

You can find a list of available variables `in the bootstrap source`_, or get explanations on them in the `Bootstrap docs`_.


Bootstrap's javascript as well as its dependencies is concatenated into a single file: ``static/js/vendors.js``.


.. _in the bootstrap source: https://github.com/twbs/bootstrap/blob/v4-dev/scss/_variables.scss
.. _Bootstrap docs: https://getbootstrap.com/docs/4.1/getting-started/theming/

It is recommended

