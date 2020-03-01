# html-to-shpaml

A simple script to convert `html` code to [`shpaml`](http://shpaml.com/).

I wrote this because:

1. https://github.com/timothycrosley/Html2Shpaml does not work because some dependencies are antiquated
2. I use `shpaml` in my projects, and I will like to keep my source code in [shpaml] only
3. I need to convert long html code to be used in my `shpaml` files

## To use

```
$ poetry install
$ ./manage convert <path_to_html> > output.shpaml
```