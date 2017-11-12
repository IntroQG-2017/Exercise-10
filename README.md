# Exercise 10: Hillslope diffusion

## Sources
This tutorial is based on [a MATLAB exercise from Prof. Todd Ehlers (Uni Tübingen)](http://www.mnf.uni-tuebingen.de/fachbereiche/geowissenschaften/arbeitsgruppen/mineralogie-geodynamik/forschungsbereich/geologie-geodynamik/workgroup.html).

## Overview
The objective of this set of problems is to compute hillslope profiles assuming hillslope evolution is a diffusive process.
As discussed in lecture, the hillslope diffusion model is based on the principal of conservation of mass, which states that the changes in surface elevation are proportional to the soil/sediment flux along the hillslope.

## Problem 1 - Steady-state diffusive hillslope profiles
In this exercise, you will be plotting a diffusive hillslope profile and exploring the effect of various parameters on the hillslope geometry.
Like last time, you are given [a broken Python script](hillslope_profile_ex1.py) that must be modified to complete this problem.
Your tasks are to:

1. Modify the file to add the equation for calculating the elevation of the hillslope *h* as a function of horizontal distance *x*.
The equation to insert is the last one in the section on [solving the diffusion equation in steady state](https://introqg.github.io/2017/lessons/L10/solving-diffusion.html#finding-integration-constant-2) in the notes on solving the diffusion equation in this week's lesson.
The `for` loop in the script goes over each index value in *x*, and you want to calculate the surface elevation of the hillslope (variable `h`) at each one of those values.
The *x*-values are in one-meter increments.
2. Two channels are located **100 m apart** and incise into a landscape being uplifted at a rate of 0.5 mm/a producing an interfluve with two symmetrical hillslopes.
Calculate the profile of the hillslope system, assuming erosion is a diffusive process with a diffusion coefficient of 50 × 10<sup>-3</sup> m<sup>2</sup>/a.
You should do this calculation using the solution for the diffusion equation you just added to the Python script, which is parabolic in form.
Note that you still want to have one-meter increments for the values of *x*.
3. Add some calculated values for this hillslope geometry to the plot.
    - **At what value of *x* (distance from the divide) is the maximum slope?**
    Add lines of code to the bottom of the Python program to calculate the maximum slope and add it to the plot with the `plt.text()` function.
    You can find the equation for the slope (*dh*/*dx*) in the [notes on solving the diffusion equation](https://introqg.github.io/2017/lessons/L10/solving-diffusion.html).
    **Where is the maximum slope in relation to the crest of the interfluve and the river channel?**
    - What is the maximum slope angle in degrees?
    Add this to your plot using the `plt.text()` function below the maximum slope.
    - What is the maximum relief of the hillslope?
    The maximum relief is the difference in elevation between the hillcrest and the adjacent valley bottom.
    Add lines of code to the bottom of the Python script to calculate the maximum relief and display it on the plot with the `plt.text()` function.
    - Diffusive problems have a characteristic timescale τ.
    **What does a characteristic timescale mean?**
    You may want to use [Google](https://www.google.fi) to look up the characteristic timescale of diffusion.
    Mathematically, the characteristic time scale for diffusion is simply the length scale of the problem squared, divided by the diffusivity.
    Convert the previous sentence into an equation in Python, and add lines of code to the bottom of the Python script to calculate the characteristic timescale and display this information on your plot using the `plt.text()` function.
    **What is the value for the characteristic timescale?
    Does it seem reasonable?
    Why or why not?**

    :heavy_exclamation_mark: Stop and save a copy of your plot with the requested values displayed as text on the plot.

4. Explore the effect of different parameters on the hillslope geometry.
Starting with the initial plot you made for point 2 above, make an additional plot for each of the four variations to the following parameters.
In each case be sure you only vary a single parameter from the original values in question 2.
    - Change `L` to 100 m
    - Double the uplift rate
    - Double the diffusivity
    - Reduce the diffusivity by half

**For points 2-4 of this exercise, you should modify the end of this document to include**

1. One plot with the values from point 3 of this question displayed as text on the plot.
2. One plot for **each** of the four modifications in point 4 of this question.
3. A figure caption beneath **each** plot explaining what it shows as if it was in a scientific publication.
4. Answers to the questions in bold for point 3 of this questions beneath the plots and captions.

**You should also save a copy of your modified code in your GitHub repository**.

## Problem 2 - Mountain hillslope profiles
Active mountain ranges typically have poorly developed soils and abundant exposed bedrock.

### Part 1 - Mountain hillslope profiles
For this question, you can use your modified Python script from Problem 1.
Assuming an interfluve width of 20 km, an uplift rate of 0.5 mm/a, and an appropriate diffusivity for rock of 10 m<sup>2</sup>/a, calculate a hillslope profile.
Again calculate the maximum slope and its value in degrees, the maximum relief, and the characteristic timescale just as you did for Problem 1.

### Part 2 - Incision history of the western Sierra Nevada mountains, California, USA 
For this section we will apply our model equation to a real landscape, the western Sierra Nevada mountains in California, USA.
We will use a [topographic profile](sierras_profile.txt) extracted across an interfluve between two streams draining into the Yuba River and change the landscape uplift rate in the equation until we get a reasonable match to the observed profile from our equation.

1. Before we load anything, it is important that you know the location of the topographic profile.

    ![Topographic profile location](Images/Sierras_profile_map.png)
    *Figure 1. Shaded relief digital elevation model of the western Sierra Nevada Mountains in California, USA. The line A-A´ is the location of a topographic profile used in Part 2 of Problem 2.*

2. Now that you know where the profile is located, you should download [a copy of the data file](sierras_profile.txt) for this week's exercise.
The data file contains distances from the drainage divide and elevations for the topographic profile A-A´.
For this part of the exercise you will also be using [another broken Python script](hillslope_profile_ex2.2.py) for loading and plotting the profile data and your calculated hillslope profile geometry.
The profile data should be loaded into arrays `data_x[]` and `data_h[]`, noting that the first column in the data file should be `data_x` and the second should be `data_h`.
There is no header on this file.
As in Problem 1, part of this script is not currently working and you will need to add the equation for calculating the hillslope elevations exactly like you did in Problem 1.
3. Once you have modified the program to add the missing equation, you will want to change some of the variables that go into the equation for hillslope diffusion.
You will be exploring a range of landscape uplift rates (`U`), but the values for the other variables will not change when you try different values of `U`.
Set the diffusion coefficient `kappa` to 1.8 m<sup>2</sup>/a and the half-width of the hillslope `L` should be half of the distance between the channels, which can be measured off the topographic profile in Figure 2 below.
Your *x*-values should range across the entire interfluve with distance increments of 100 m.

    ![Topographic profile](Images/sierras_profile.png)<br/>
    *Figure 2. Topographic profile across an interfluve between 2 streams draining into the Yuba River, Sierra Nevada mountains, California, USA.*

4. Lastly, you will want to plot the observed topographic profile along with the model prediction to try and fit the observation by varying the uplift rate until you get a similar profile.
Add a line in the script to plot the observed data using the `plt.plot()` function.
Be sure to use a different line color or pattern so that it is clear which line is the model and which is the data profile.
You can add the `label` parameter in the `plt.plot()` functions and a line legend if you like.
Also, you will want to shift the model profile up about 750 m since the channels in the observed profile are at ~750 m elevation.
Once you've determined your best-fit uplift rate, add text to the plot to display that rate using the `plt.text()` function.

**For Problem 2 you should add the following to the end of this document**

1. A copy of the plot for Part 1 of Problem 2 with the 4 calculated values displayed on it.
2. A figure caption as if the figure was in a scientific publication.
3. 2-3 sentences discussing the implications the results in Part 1 have for mountain hillslopes. What do the various values you have calculated imply for natural systems? How long might they take to respond to changes in river erosion rates, for example?
4. A plot comparing the observed and predicted topographic profiles for Part 2 with the landscape uplift rate displayed as text on the plot.
5. A figure caption explaining what is plotted as if it were in a scientific publication.

**As in Problem 1, you should also save a copy of your modified codes in your GitHub repository**.

# Answers
## Problem 1
This is some text. You can use *italics* or **bold** text easily. You may want to read a bit more about [formatting text in Github-flavored Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/). You can see an example of how to display an image with a caption below.

![Text shown if image does not load](Images/sine.png)<br/>
*Figure 3: Sine wave calculated from 0 to 2π*
