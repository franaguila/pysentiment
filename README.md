
[![](https://codecov.io/gh/nickderobertis/pysentiment/branch/master/graph/badge.svg)](https://codecov.io/gh/nickderobertis/pysentiment)

# pysentiment

## Overview

This is a library for sentiment analysis in dictionary framework.
Two dictionaries are provided in the library, namely, Harvard IV-4 and
Loughran and McDonald Financial Sentiment Dictionaries, which are sentiment
dictionaries for general and financial sentiment analysis.

See also http://www.wjh.harvard.edu/~inquirer/ and https://www3.nd.edu/~mcdonald/Word_Lists.html .

### Introduction

`Positive` and `Negative` are word counts for the words in positive and negative sets.


`Polarity` and `Subjectivity` are calculated in the same way of Lydia system.
See also http://www.cs.sunysb.edu/~skiena/lydia/


## Getting Started

```
pip install pysent3
```

```python
import pysent3
```

## Usage

To use the Harvard IV-4 dictionary, create an instance of the `HIV4` class

```python
import pysent3 as ps
hiv4 = ps.HIV4()
tokens = hiv4.tokenize(text)  # text can be tokenized by other ways
                                  # however, dict in HIV4 is preprocessed
                                  # by the default tokenizer in the library
score = hiv4.get_score(tokens)
```

`HIV4` is a subclass for `pysentiment3.base.BaseDict`. `BaseDict` can be inherited by 
implmenting `init_dict` to initialize `_posset` and `_negset` for the dictionary
to calculate 'positive' or 'negative' scores for terms.

Similarly, to use the Loughran and McDonald dictionary:
```python
import pysent3 as ps
lm = ps.LM()
tokens = lm.tokenize(text)
score = lm.get_score(tokens)
```


Largely based on `pysentiment2` created by Nick DeRobertis and based on `pysentiment` by Zhichao Han. GNU GPL License.