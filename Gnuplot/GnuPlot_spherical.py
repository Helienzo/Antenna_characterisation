from numpy import *
import Gnuplot, Gnuplot.funcutils

def test():

    g = Gnuplot.Gnuplot(debug = 1)
    g('set parametric')
    #g('set data style lines')
    #g('set hidden')
    #g('set contour base')
    g.xlabel('x')
    g.ylabel('y')
    g.title = "This is a 3D test plot"

    #g.splot( x= [1:100], y = [1:100], z =[1:100])
    #g.splot 'data.txt' u ($1==6 ? $2:1/0):3:4 title 'At-no 6' w points pt 7,
    g("set xrange [-5.0:5.0]")
    g("set yrange [-5:5]")
    g("set zrange [-5:5]")
    g("set mxtics 5")
    g("set mytics 5")
    g("set ticslevel 0")
    #g("set dgrid3d")
    g("set grid ztics")
    g("set grid xtics")
    g("set grid ytics")
    g("set label 'label in front' at 1,1,1 tc rgb 'white' font ',30' front")

    #g.set yrange(5)
    #g.set zrange(5)
    g("set hidden3d")
    #g("set parametrics")
    g("set title 'this is my plot'")
    g("set key off")
    g("set angles degrees")
    g("set mapping spherical")
    #g("set dgrid3d 16, 16")
    #g("splot 'sph_dat.txt' using 1:2:3  pt 7 ps 1")
    g("set style data linespoint")
    #g("set style fill transparent solid 0.65")
    #g("set pm3d") 
    g("splot 'sph_dat.txt' using 1:2:3:4 with linespoint")
    #g("splot 'data.txt' using 1:2:(0) with points")
    
    
	
    raw_input("Press any button to continue")

if __name__ == '__main__':
    test()
