from numpy import *
import Gnuplot, Gnuplot.funcutils

def test():

	g = Gnuplot.Gnuplot(debug = 1)
	g.title = "This is a test plot"
	g('set data style linespoints')
	g.plot([[0,1.1], [1,5.8], [2,3.3], [3,4.2]])
	raw_imput("Press any button to continue")
