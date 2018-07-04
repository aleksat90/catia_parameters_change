# Catia automatisation testing script

This script in simplified way updates Catia 3D model to the desired value automaticly.

I used it for creating Monte Carlo analysis. My use case was that I need to do the statistical influence of tolerances to resulting dimension
if the variable dimensions are changing according the Gaussian and Uniform distribution. Basically, by the script, there were 10000
cad models created and ofcourse 10k times output value of resulting dimension.

Second use case was using this script to test parametric 3D models for application engineers. All possible combinations
of parameters were created statistically, and script was looping through them and every time update the CAD model. In this case
I was just counting how many times Catia coudn't update itself.

So for details of above use cases, don't hesitate to contact me :)
Thank you.
