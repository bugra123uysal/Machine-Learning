
import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
""" ortalama """
c=numpy.mean(speed)

print(c)
""" orta noktayı bulmak """
r=numpy.median(speed)
print(r)

""" en çok tekrar eden  """

n=stats.mode(speed)
print(n)

""" standart sapma """

m= numpy.std(speed)
print(m)
""" varyans """
z=numpy.var(speed)
print(z)

""" yüzdelik ler """
""" yüzde hesaplama """
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

uıu=numpy.percentile(ages, 90)
print(uıu)

""" veri dağıtımı  """
""" 0 ile 5 arasında 300 rasgele kayan nokta """

vbg=numpy.random.uniform(0.0, 5.0, 300 )
print(vbg)

