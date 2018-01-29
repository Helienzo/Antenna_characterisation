from numpy import *
import Gnuplot, Gnuplot.funcutils

def test():

    g = Gnuplot.Gnuplot(debug = 1)
    g('set parametric')
    #g('set data style lines')
    g('set hidden')
    g('set contour base')
    g.xlabel('x')
    g.ylabel('y')
    g.title = "This is a 3D test plot"
    '''
	#g('set data style linespoints')
    #g.plot([[0,1.1,1], [1,5.8,1], [2,3.3,1], [3,4.2,1]])
    x = arange(35)/2.0
    y = arange(30)/10.0 - 1.5
    # Make a 2-d array containing a function of x and y.  First create
    # xm and ym which contain the x and y values in a matrix form that
    # can be `broadcast' into a matrix of the appropriate shape:
    xm = x[:,newaxis]
    ym = y[newaxis,:]
    m = (sin(xm) + 0.1*xm) - ym**2
    g('set parametric')
    #g('set data style lines')
    g('set hidden')
    g('set contour base')
   # g.title('An example of a surface plot")
    g.xlabel('x')
    g.ylabel('y')
    # The `binary=1' option would cause communication with gnuplot to
    # be in binary format, which is considerably faster and uses less
    # disk space.  (This only works with the splot command due to
    # limitations of gnuplot.)  `binary=1' is the default, but here we
    # disable binary because older versions of gnuplot don't allow
    # binary data.  Change this to `binary=1' (or omit the binary
    # option) to get the advantage of binary format.
    '''
    #g.splot(Gnuplot.GridData(m,x,y, binary=0)) #FROM EXAMPLE
    
    
    #g.splot( x= [1:100], y = [1:100], z =[1:100])
    #g.splot 'data.txt' u ($1==6 ? $2:1/0):3:4 title 'At-no 6' w points pt 7,
    g("set xtic 15")
    g("set ytic 5")
    g("set ztic 15")
    #g.set yrange(5)
    #g.set zrange(5)
    g("splot 'data.txt' 1:2:3")
	
    raw_input("Press any button to continue")

if __name__ == '__main__':
    test()
