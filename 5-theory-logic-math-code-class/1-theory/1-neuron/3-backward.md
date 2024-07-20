## Backward Pass

For going backwar and fixing weights and bias,
![Backward](media/backward.png)

we need to follow some steps

## Steps

1. Error: find how bad result is
2. Loss: determine how wrongly did model punished. 
3. Gradient: for every weight, it determines how much 'fix' it needs for this loss
4. Updating Wegiths: how much should we change these weights for current loss

seems difficult ?

let us simplify it.

## 1. Error

We first need to find "error".
It is how wrong did model predicted.

take a look at following example

![Eggs Game](media/eggs.png)

in first case, error = 1 eggs.

in second case, error = 6 eggs.

## 2. Loss

Loss means 'how much should we shout' based on error.

There are many [methods and techniques](../2-errors/README.md) used to calculate loss. But we shall use a simple method [Mean Sequared Error](../2-errors/1-mse/README.md)

This methods just chills for shorter errors.
Like for 1 egg, it still gives a win to Ezi. and gives a small number like 0.025

and punch weights to improve

![Punch](media/single-punch.png)

But for bigger errors, e.g., 6 eggs, it shouts and gives a big number. 23.42

and punch weights a lot more to improve much more for this error

![Multiple Punch](media/multi-punch.png)

## 3. Gradient

with loss, we know that how much punches
we need to fix model

but it is time to distribute punches for individual weights.

![Divide Punches](media/weights-punches.png)

inputs that were bigger, caused more bad results,
hance their weights will be punched more

and inputs that were smaller, deserve little fixing.

## 4. Update Weights

we know about all the punches.
but it is time for some math to see how these weights are actually fixed.

We determine Error and Loss.

![Responsibility](media/responsibility.png)

And then distribute loss against every input.

and change weights according to loss. here is how result will look afterwards

![Loss](media/loss-applied.png)

but there is a problem, with this method, our model will never learn.

Its weights will keep jumping from very high positive values to vary low negative values and vice versa.

To make it "actually learn". we slow down this fixing process by "learning rate".
that means if learning rate is 0.1, it will only apply 10% of loss and slightly change weights.

![Learning Rate](media/learning-rate.png)

this operation repeats for many samples until our Neuron is trained.