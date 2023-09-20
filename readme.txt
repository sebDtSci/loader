import sys
sys.path.append("../loader")
from loaderA import funLoader
goodLoader('dots', 'red')

or 
import loaderA as lo

lo.funLoader('dots', 'red')


