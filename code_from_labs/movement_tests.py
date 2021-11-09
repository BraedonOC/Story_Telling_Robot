
# Choregraphe simplified export in Python.
from naoqi import ALProxy


names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1.68, 5.56])
keys.append([-0.414222, -0.131966])

names.append("HeadYaw")
times.append([1.68, 5.56])
keys.append([-0.016916, -0.0061779])

names.append("LAnklePitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.0890141, 0.0873961, 0.0997519, 0.0997519, 0.099668])

names.append("LAnkleRoll")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.11049, -0.108872, -0.11049, -0.11049, -0.108872])

names.append("LElbowRoll")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.50933, -0.493906, -0.52467, -0.01845, -0.00302601])

names.append("LElbowYaw")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-1.06916, -1.08918, -1.44959, -1.43885, -1.44047])

names.append("LHand")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.314, 0.3068, 0.3008, 0.3008, 0.3036])

names.append("LHipPitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.130348, 0.128898, 0.130348, 0.130348, 0.128898])

names.append("LHipRoll")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.118076, 0.122762, 0.118076, 0.118076, 0.112024])

names.append("LHipYawPitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.170232, -0.167164, -0.170232, -0.170232, -0.170232])

names.append("LKneePitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.0843279, -0.0844119, -0.0843279, -0.0843279, -0.0828779])

names.append("LShoulderPitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.79457, -0.75477, -0.834454, 0.398882, 1.30386])

names.append("LShoulderRoll")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.12728, -0.115092, 0.856014, 1.22571, 0.231592])

names.append("LWristYaw")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.128814, -0.14884, -0.148756, -1.13358, -0.7471])

names.append("RAnklePitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.0890141, 0.0873961, 0.0997519, 0.0997519, 0.0997519])

names.append("RAnkleRoll")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.11049, 0.108872, 0.11049, 0.11049, 0.11049])

names.append("RElbowRoll")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.50933, 0.493906, 0.52467, 0.01845, 0.303774])

names.append("RElbowYaw")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([1.06916, 1.08918, 1.44959, 1.43885, 1.44192])

names.append("RHand")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.314, 0.3068, 0.3008, 0.3008, 0.3008])

names.append("RHipPitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.130348, 0.128898, 0.130348, 0.130348, 0.130348])

names.append("RHipRoll")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.118076, -0.122762, -0.118076, -0.118076, -0.118076])

names.append("RHipYawPitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.170232, -0.167164, -0.170232, -0.170232, -0.170232])

names.append("RKneePitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.0843279, -0.0844119, -0.0843279, -0.0843279, -0.0843279])

names.append("RShoulderPitch")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([-0.79457, -0.75477, -0.834454, 0.398882, 1.44967])

names.append("RShoulderRoll")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.12728, 0.115092, -0.856014, -1.22571, -0.142704])

names.append("RWristYaw")
times.append([1.52, 1.68, 2.92, 4.2, 5.56])
keys.append([0.128814, 0.14884, 0.148756, 1.13358, 0.348176])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", "138.67.194.114", 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err

