# Catia automation testing script

This script in simplified way updates Catia 3D model to the desired values e.g. updates height of the cube, diameter of cylinder, depth of the hole, changing names of the model etc.

I used it for creating Monte Carlo analysis. My use case was that I needed to do the statistical influence of tolerances to resulting dimension
by changing variable dimensions according the Gaussian and Uniform distribution. Basically, with this script, there were 10000
CAD models created and 10k times it read value of resulting dimension which was later used for further analysis.

Second use case was using this script to test parametric 3D models for application engineers. All possible combinations
of parameters (that somebody can input) were created statistically, and script was looping through them and every time update the CAD model. In this case
I was just counting how many times Catia coudn't update itself due to impossible geometry, this was considered as failed case.

So for details of above use cases, don't hesitate to contact me :)

Thank you,
Aleksa
