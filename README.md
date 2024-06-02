# Real Python Feed Reader

This project is the result of working through Real Python's [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/) tutorial. Since the original package was already published on PyPI under the `realpython-reader` name, 
I am using a slighly modified name for the project.

The Real Python Feed Reader is a basic [web feed](https://en.wikipedia.org/wiki/Web_feed) reader that can download the 
latest Real Python tutorials from the [Real Python feed](https://realpython.com/contact/#rss-atom-feed).


## Installation

You can install the Real Python feed Reader from [PyPI](https://pypi.org/project/rys-reader/):

```
python -m pip install rys-reader
```

The reader is supported on Python 3.7 and above. Older versions of Python, including Python 2.7, are supported by
version 1.0.0 of the reader

## How to use

The Real Python Feed Reader is a command line application, named `realpython`. To see a list of the 
[latest Real Python tutorials](https://realpython.com/), call the program without an arguments:

```
$ realpython
The latest tutorials from Real Python (https://realpython.com/)
  0 The Real Python Podcast – Episode #206: Building Python Unit Tests & Exploring a Data Visualization Gallery
  1 What Are CRUD Operations?
  2 Efficient Iterations With Python Iterators and Iterables
  3 How to Create Pivot Tables With pandas
  4 Quiz: How to Create Pivot Tables With pandas
  5 The Python calendar Module: Create Calendars With Python
  6 Building a Python GUI Application With Tkinter
  7 Basic Data Types in Python: A Quick Exploration
  8 The Real Python Podcast – Episode #205: Considering Accessibility & Assistive Tech as a Python Developer
  9 How to Get the Most Out of PyCon US
 10 Python's Built-in Exceptions: A Walkthrough With Examples
 11 Quiz: What Are CRUD Operations?
 12 HTML and CSS Foundations for Python Developers
 13 What Is the __pycache__ Folder in Python?
 14 The Real Python Podcast – Episode #204: Querying OpenStreetMaps via API & Lazy Evaluation in Python
 15 PyTorch vs TensorFlow for Your Python Deep Learning Project
 16 Flattening a List of Lists in Python
 17 Python News: What's New From April 2024
 18 The Real Python Podcast – Episode #203: Embarking on a Relaxed and Friendly Python Coding Journey
 19 Quiz: The Python calendar Module
 20 Python Sequences: A Comprehensive Guide
```

To read one particular tutorial, call the program with the numerical ID of the tutorial as a parameter:

```
$ realpython 0
# The Real Python Podcast – Episode #206: Building Python Unit Tests & Exploring a Data Visualization Gallery

How do you start adding unit tests to your Python code? Can the built-in
unittest framework cover most or all of your needs? Christopher Trudeau is
back on the show this week, bringing another batch of PyCoder's Weekly
articles and projects.

[... The full text of the article ...]
```

You can also call the Real Python Feed Reader in your own Python code, by importing from the `reader` package:

```python
>>> from reader import feed
>>> feed.get_titles()
['The Real Python Podcast – Episode #206: Building Python Unit Tests & Exploring a Data Visualization Gallery',...]
```
