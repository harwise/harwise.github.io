---
layout: default
title: Symbols
---

{% include katex.html %}

# Metrics Prefixes

$G$ (giga) $M$ (mega) $k$ (kilo) $1$ $m$ (milli) $\mu$ (micro) $n$ (nano) $p$ (pico)

# Energy

Voltage  - Potential energy. Pressure.\
Current  - Kinetic energy. Flow.

Joule ($J$) - How much energy is transferred.\
Watt ($W$)  - Electric Power. The rate at which energy is transferred or transformed.

$$
1W = 1J \space per \space second
$$

$$
P = I \times V
$$

|Situation|Approximate Power|
|:-:|:-:|
|Arduino Uno Micro-controller|0.25$W$|
|Cell Phone Transmitter|3$W$|
|Laptop Computer|65$W$|
|50-Inch LCD Television|150$W$|
|Microwave Oven|1000$W$|

# Battery

Nominal Voltage   - Output voltage after 50% discharge\
Capacity ($Ah$)   - Amp-hours. Amount of electrons. One amp of current for one hour at its rated voltage.

# Grounded vs. floating

GND (ground) - wall power outlets.\
COM (**own** common point) - batteries.







This is a demo of all styled elements in Jekyll Now. 

[View the markdown used to create this post](https://raw.githubusercontent.com/barryclark/www.jekyllnow.com/gh-pages/_posts/2014-6-19-Markdown-Style-Guide.md).

This is a paragraph, it's surrounded by whitespace. Next up are some headers, they're heavily influenced by GitHub's markdown style.

## Header 2 (H1 is reserved for post titles)##

### Header 3

#### Header 4
 
A link to [Jekyll Now](http://github.com/barryclark/jekyll-now/). A big ass literal link <http://github.com/barryclark/jekyll-now/>
  
An image, located within /images

![an image alt text]({{ site.baseurl }}/images/jekyll-logo.png "an image title")

* A bulletted list
- alternative syntax 1
+ alternative syntax 2
  - an indented list item

1. An
2. ordered
3. list

Inline markup styles: 

- _italics_
- **bold**
- `code()` 
 
> Blockquote
>> Nested Blockquote 
 
Syntax highlighting can be used by wrapping your code in a liquid tag like so:

{{ "{% highlight javascript " }}%}  
/* Some pointless Javascript */
var rawr = ["r", "a", "w", "r"];
{{ "{% endhighlight " }}%}  

creates...

{% highlight javascript %}
/* Some pointless Javascript */
var rawr = ["r", "a", "w", "r"];
{% endhighlight %}
 
Use two trailing spaces  
on the right  
to create linebreak tags  
 
Finally, horizontal lines
 
---
***