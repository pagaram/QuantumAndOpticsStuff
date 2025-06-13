import numpy as np
import matplotlib.pyplot as plt

def lineEquation(x1,x2,y1,y2):
    slope = (y2-y1)/(x2-x1)
    intercept = y1 - slope*x1

    return slope, intercept


lens = np.array([[0.5, -5], [0.5, 5]])
focci = np.array([[-6.5, 0], [7.5, 0]])

steps = np.linspace(-11, 30, 30)
waist = np.zeros((len(steps), 1))
divergence = np.zeros((len(steps), 1))
beamRadius = np.zeros((len(steps), 1))

slopeDiv, interceptDiv = lineEquation(-11, 0.5, 0, 2.5)
thetaDivergence = np.arctan(slopeDiv)

slopeWaist, interceptWaist = lineEquation(0.5, 7.5, 1, 0)
thetaWaist = np.arctan(slopeWaist)

thetaDiv2 = -1*np.sqrt(thetaDivergence**2 - thetaWaist**2)
slopeDiv2 = np.tan(thetaDiv2)
interceptDiv2 = 2.5-.5 * slopeDiv2

for i in range(len(steps)):

    if steps[i] < 0.5:
        waist[i, 0] = 1
        divergence[i, 0] = slopeDiv * steps[i] + interceptDiv

    else:
        waist[i, 0] = slopeWaist * steps[i] + interceptWaist
        divergence[i, 0] = slopeDiv2 * steps[i] + interceptDiv2

    beamRadius[i, 0] = np.sqrt(waist[i, 0] ** 2 + divergence[i, 0] ** 2)

#finding beamWaist
radMinimum = beamRadius[0, 0]
waistLocation = 0

for i in range(len(steps)):
    if beamRadius[i, 0] < radMinimum:
        radMinimum = beamRadius[i, 0]
        waistLocation = steps[i] - 0.5

print(radMinimum)
print(waistLocation)

w0 = 7 * -1 * thetaWaist
print(w0)

plt.figure()
plt.plot(steps, waist[:, 0], '-r')
plt.plot(steps, divergence[:, 0], '-b')
plt.plot(steps, beamRadius[:, 0], '-k')
plt.plot(focci[:, 0], focci[:, 1], 'ok')
plt.plot(lens[:, 0], lens[:, 1], '-k')
plt.grid()
plt.legend(['Waist Ray','Divergence Ray','W(z)'])
plt.title('Gaussian Beam')
plt.show()
