import numpy
z = numpy.e ** (1j * (2 * numpy.pi / 5)*2)

print(f"Real: {numpy.real(z)}\nImaginary: {numpy.imag(z)}\n")

#z = numpy.e**(3+1j*((-numpy.pi/2)+(2*numpy.pi*3)))
#print(f"e^z = {-1j*numpy.e**3}")
