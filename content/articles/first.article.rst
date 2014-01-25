The first article
#################

:tags: begining, first-post, test
:category: разметка

Моя первая статья. Тестовая. Тут ничего важного нету.

\* Italic text here \*

*Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam bibendum auctor blandit. Duis blandit tristique aliquam. Maecenas viverra dolor et nulla rutrum, in convallis diam feugiat. Ut eleifend elit ut est semper, sed posuere metus interdum. Nullam tellus urna, lobortis non arcu et, malesuada euismod sem. Maecenas cursus purus ut nulla hendrerit pharetra. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.*



*Donec suscipit dui eu gravida molestie. Praesent sit amet sagittis sem, eget pretium diam. Vivamus interdum et mi suscipit ornare. Quisque varius interdum elit, tincidunt gravida enim mollis vel. Donec faucibus tortor sed dapibus feugiat. Praesent tempus laoreet sapien, vel commodo elit molestie at. Vestibulum elit diam, placerat quis sollicitudin vitae, fermentum sed diam. Etiam dui orci, suscipit tincidunt lobortis ac, vehicula ac neque.*

\*\* Bold text here \*\*

**Bold text Nunc mollis rhoncus eros, in bibendum magna convallis quis. Phasellus sem tortor, ultricies quis velit eu, bibendum mattis tellus. Duis sit amet tincidunt leo, quis mollis urna. Ut bibendum justo in erat rutrum rutrum. Nulla mollis odio sit amet auctor rhoncus. Aliquam lorem nisl, cursus at nisl vitae, dapibus auctor mauris. Aliquam a venenatis diam. Suspendisse neque nisl, hendrerit eget erat non, semper interdum mauris. Donec ornare tellus et sodales commodo.**

Lists
*****

* Первый элемент списка.
* Второй элемент с дочерним списком.

  * Первый элемент дочернего списка.
  * Второй элемент дочернего списка.

    Another element

    Second another element

      * And yet
 
        i. Numeric text

        ii. Second numeric text
	
       	iii. Wut wut wut
* Третий элемент списка.

Links:
======
	`Гугль <http://www.google.com>`_

	`ReStructuredText  <http://docutils.sf.net/rst.html>`_
	
	`Cheat-sheet <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_

Other:
------

External hyperlinks, like Python_ or Triton_.

.. _Python: http://www.python.org/
.. _Triton: http://www.triton.org/


Footnote references, like [5]_. 
Note that footnotes may get 
rearranged, e.g., to the bottom of 
the "page".

.. [5] A numerical footnote. Note 
   there's no colon after the ``]``.

Hmmmmmmm another text

Autonumbered footnotes are 
possible, like using [#]_ and [#]_.

.. [#] This is the first one.
.. [#] This is the second one.

They may be assigned 'autonumber 
labels' - for instance, 
[#fourth]_ and [#third]_.


.. [#third] a.k.a. third_
.. [#fourth] a.k.a. fourth_

Таблицы рисуются так:
---------------------
Simple table:

=====  =====  ====== 
   Inputs     Output 
------------  ------ 
  A      B    A or B 
=====  =====  ====== 
False  False  False 
True   False  True 
False  True   True 
True   True   True 
=====  =====  ======

Что за ерунда со строками начинающимися с \|
--------------------------------------------

| \|Раз два три
| \|Четыре пять
| \|Ничего не понимаю ... `один` **два**
| \|Эти строки начинаются с символа "\|"

Раз два три
Четыре пять
Ничего не понимаю ... `один` **два**
Эти строки НЕ начинаются с символа "\|"

Raw text::

  Raw text::
  <empty line>
  *раз* **два**

