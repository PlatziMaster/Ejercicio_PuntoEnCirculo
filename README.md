# Exercise_DotInCircle

## Overview

In this exercise you have to make a function, which given circle radius with
center at (0,0) and dot (x,y) it determines if dot is in circle printing answer.

## Descripción

This exercise is of understanding, but its goal is you are able to search and
understand what are the properties of a circle, I recommend to begin for
understand which is the circle's formula and I remember you that you can find
if a dot is within a circle based on a inequality.

## Hint

You can see if your formula is working from visual way if you plot the result.

## Bonus

Resolve this exercise but without assume that circle's center is encounter at
(0,0).

---

## Walk-through

Let's begin with circumference formula:

<img src="https://render.githubusercontent.com/render/math?math=C%20=%202\pi%20r" style="background: #aaa; padding: 7.5px; border-radius: 2.5px;">

Just kidding, it's olny for information purposes because for this exercise we
don't need calculate the circumference.

Better, we imagine how to draw a circle on the beach; we can use two branches
and a little rope (but, How we can find two branches on a beach filled with palm
trees?). Ok let's do it!

First we must tie up both branches with the rope. At this point we need plant
the first branch into the sand and maybe grab strongly with a hand meanwhile
with another one we tense the rope and touch the sand with branch ending.

Now we move around the fixed branch to end where we began. Wonderful! We get a
beautiful circle over the sand.

With this action we can discover a fact: Any dot on circumference is at the
same distance from center. Such distance is radius.

Let's play bullseye and throw a stone... Good! But how we know if stone is
inside or outside of circle. Ok ok, just we need watch, but the exercise sense
is another one. Anyway the answer is simple: we compare the distance between the
stone and the circle's center with used rope length. If the rope lenght is too
short it means that the stone is outside the circumference. We got it!

However in geometry nothing is as simple as you imagine (ignore euclidean, it's
in another league). At this point we can't escape from maths also I guess will
be difficult imagine us using rules on sand, so let's take a photo. Now leave it
on our desk.

In terms of difficulty, to calculate the distance by vectorial way is not the
same as do it like scalar, then we gonna ruin the photo drawing a grid over it,
I mean it's a cartesian plane with origin from circle's center and we will
assume that all dots are given as (x,y) coordinates.

Now to size the distance between the stone and origin we need to know the lenght
from the first one to the vertical and horizontal axis and it will be `x` and
`y` coodinates respectively.

Yeah, I know this didn't intend to be a complicated explanation, but just trust
me, best  is coming! Every coordinate in a cartesian plane can be abstracted as
a right triangle, here comes Pythagoras and his theoreme. He was a very smart
guy and he establish that the square of hypotenuse is equals to the sum of the
squares of the oposite sides (it's not as complicated as it sounds).

We know the lenght of both triangle' small sides expressed as `x` and `y` of the
stone, so we can calculate the hypotenuse:

<img src="https://render.githubusercontent.com/render/math?math=h%20=%20\sqrt{x^{2}%20%2b+%20y^{2}}" style="background: #aaa; padding: 7.5px; border-radius: 2.5px;">

So hypotenuse will be the distance between the stone and the circle's center.
Finally we can compare the hypotenuse with the rope length and if it's greater
than last one it means that the stone is outside the circle.

Eureka!

## Algorithm

 1. begin.
 2. read: `radius`, `dot_x`, `dot_y`, `center_x` = `0`, `center_y` = `0`.
 3. verify: `radius`, `dot_x`, `dot_y`, `center_x`, `center_y` are _numbers_.
 4. if `true` then continue else goto: step 14.
 5. verify: `radius` is greater than `0`.
 6. if `true` then continue else goto: step 15.
 7. set: `side_a`, `side_b`, `hypotenuse` as _number_.
 8. calculate: `side_a` = `dot_x` - `center_x`.
 9. calculate: `side_b` = `dot_y` - `center_y`.
10. calculate: `hypotenuse` = (`side_a` ^ 2 + `side_b` ^ 2) ^ (1 / 2)
11. compare: `hypotenuse` is greater than `radius`.
12. if `true` then return: 'outside' else return: 'inside'.
13. goto: step 16.
14. return: 'at least a given data is not a numeric value'.
15. return: 'radius can't be less than 0'.
16. end.
