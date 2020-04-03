# html-to-shpaml

A simple script to convert `html` code to [`shpaml`](http://shpaml.com/).

I wrote this because:

1. https://github.com/timothycrosley/Html2Shpaml does not work because some dependencies are antiquated
2. I use `shpaml` in my projects, and I will like to keep my source code in [shpaml] only
3. I need to convert long html code to be used in my `shpaml` files

## Precautions
Its only Work on python 3.7
Remove Doctype HTML tag like this
```
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```
It doesnt work with stype/script tags & inline css, To make it work need a little adjustment

### Only work with html markup 

## To use
```
$ poetry install
$ ./manage convert <path_to_html> > output.shpaml
```