# Perceptron
This project was created as a response to Luis Serrano's [logistic regression and perceptron alrogithm video](https://www.youtube.com/watch?v=jbluHIgBmBo). I tried to use the same terminology that was used in the video (eg. red and blue points), so it would be easier to see how the ideas in the video can be represented as code.

To put it simply, the goal of the perceptron algorithm (as implemented here) is to use a line to separate the red and blue points. Luis goes over the algorithm in great detail in the video linked above, so I won't explaini it fully here. However, the general idea is to start with a random line of the form ax + by + c = 0, and then iterate randomly over the red and blue points. If the randomly chosen point is on the wrong side of the line, nudge the line so it's a little closer to the point.

## Example
This example shows the line before and after training. The initial line is -7 - 3y - 6 = 0

![image](https://user-images.githubusercontent.com/17073202/54399460-c6b23400-467b-11e9-8600-47cee90eb72a.png)

![image](https://user-images.githubusercontent.com/17073202/54399478-dc275e00-467b-11e9-8a1c-a5eeb7ea23f7.png)
