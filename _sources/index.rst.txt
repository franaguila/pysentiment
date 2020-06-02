.. pysentiment2 documentation master file, created by
   cookiecutter-pypi-sphinx.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Python Sentiment Analysis documentation!
********************************************************************

Sentiment Analysis in Python using a Dictionary Approach

To get started, look here.

.. toctree::
   :caption: Tutorial

   tutorial
   auto_examples/index

An overview
===========

This is a library for sentiment analysis in dictionary framework.
Two dictionaries are provided in the library, namely, Harvard IV-4 and
Loughran and McDonald Financial Sentiment Dictionaries, which are sentiment
dictionaries for general and financial sentiment analysis.

See also http://www.wjh.harvard.edu/~inquirer/ and https://www3.nd.edu/~mcdonald/Word_Lists.html .

Introduction
-------------

``Positive`` and ``Negative`` are word counts for the words in positive and negative sets.


``Polarity`` and ``Subjectivity`` are calculated in the same way of Lydia system.
See also http://www.cs.sunysb.edu/~skiena/lydia/

The formula for ``Polarity`` is,

    Polarity= (Pos-Neg)/(Pos+Neg)

The formula for ``Subjectivity`` is,

    Subjectivity= (Pos+Neg)/count(*)


Install
^^^^^^^^^
::

    pip install pysentiment2

Usage
^^^^^^^^^
To use the Harvard IV-4 dictionary, create an instance of the `HIV4` class

::

    >>> import pysentiment2 as ps
    >>> hiv4 = ps.HIV4()
    >>> tokens = hiv4.tokenize(text)  # text can be tokenized by other ways
                                      # however, dict in HIV4 is preprocessed
                                      # by the default tokenizer in the library
    >>> score = hiv4.get_score(tokens)


``HIV4`` is a subclass for ``pysentiment2.base.BaseDict``. ``BaseDict`` can be inherited by implmenting ``init_dict`` to initialize ``_posset`` and ``_negset`` for the dictionary
to calculate 'positive' or 'negative' scores for terms.

Similarly, to use the Loughran and McDonald dictionary:
::

    >>> import pysentiment2 as ps
    >>> lm = ps.LM()
    >>> tokens = lm.tokenize(text)
    >>> score = lm.get_score(tokens)

Quick Links
------------

Find the source code `on Github <https://github.com/nickderobertis/pysentiment>`_.


.. toctree:: api/modules
   :caption: API Documentation
   :maxdepth: 3

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
