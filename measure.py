### measure libraby version 1.8.12
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sigval import sigval

# Settings
linreg_change = 0.00001 # min relative change per step to end linear regression
minfloat = 1e-80 # replaces zeros in linreg
linspace_res = 2000 # resolution for nplinspace

# Variables for export
sqrt = np.sqrt
exp = np.exp
ln = np.log
log10 = np.log10
sin = np.sin
cos = np.cos
tan = np.tan
arcsin = np.arcsin
arccos = np.arccos
arctan = np.arctan
pi = np.pi
euler_e = np.e
c = 2.99792458e8 # Speed of light
h = 6.62607015e-34 # Planck's constant
e = 1.602176634e-19 # Elementary charge
kB = 1.380649e-23 # Boltzmann constant
NA = 6.02214076e23 # Avogadro constant
T0 = 273.15 # Zero Celsius in Kelvin
p0 = 101325 # NIST standard pressure
g = 9.80984 # Gravitanional acceleration in Heidelberg 
dg = 2e-5 # Uncertainty of the gravitational acceleration

unitPrefixes = "kMGTPEZYyzafpnμm"

def npfarray(x):
  return np.array(x, dtype='float')

def nplinspace(start,stop):
  return np.linspace(start,stop,num=linspace_res,endpoint=True)

def mv(x):
  s = 0.0
  for i in range(len(x)):
    s += x[i]
  return s / len(x)

def dsto(x):
  s = 0.0
  for i in range(len(x)):
    s += (x[i] - mv(x))**2
  return sqrt(s / (len(x) - 1))

def dsto_mv(x):
  return dsto(x) / sqrt(len(x))

def dsys_mv(x):
  return sqrt(np.sum(x**2)) / len(x)

def dtot(dsys, dsto):
  return sqrt(dsys**2 + dsto**2)

def signval(val, err=0.0):
  if (err == 0.0):
    return ['{:g}'.format(val), '']
  errstr = '{:.1g}'.format(err)
  err = float(errstr)
  expdiff = int(np.floor(np.log10(abs(val))) - np.floor(np.log10(err)))
  sdigits = expdiff + 1
  if (expdiff < -2):
    val = 0.0
    sdigits = 0
  elif (expdiff == -2):
    if (int('{:e}'.format(abs(val))[0]) >= 5):
      sig = val / abs(val)
      val = sig * 10**int(1+np.floor(np.log10(abs(val))))
    else:
      val = 0.0
    sdigits = 0
  elif (expdiff == -1):
    if (int(np.floor(np.log10(abs(float('{:.0e}'.format(val))))) - np.floor(np.log10(err))) == -1):
      val = val
      sdigits = 0
    else:
      val = float('{:.0e}'.format(val))
      sdigits = 1
  else:
    if (int(np.floor(np.log10(abs(float('{:.{digits}e}'.format(val, digits=sdigits))))) - np.floor(np.log10(err))) != expdiff):
      val = float('{:.{digits}e}'.format(val, digits=sdigits))
      sdigits += 1
  valstr = '{:.{digits}e}'.format(val, digits=sdigits)
  return [valstr, errstr]

def val(name, val, err=0.0, unit='', prefix=True):
  """
  Parameters

  val: float
  err: float, uncertainty of val
  name: string, name of val
  ----------
  Returns

  string, format: "name = val ± err" with two significant digits
  """

  out = ''
  if name != '':
    out += name + ' = '
  
  valstr, errstr, expstr = sigval(val, err, unit != '' and prefix)

  if err != 0.0 and (expstr[0] != '0' or unit != ''):
    out += '('
  out += valstr
  if err != 0.0:
    out += ' ± ' + errstr
  if err != 0.0 and (expstr[0] != '0' or unit != ''):
    out += ')'
  if expstr[0] != '0':
    exp = int(expstr)
    if unit != '' and prefix and abs(exp) <= 3 * len(unitPrefixes) / 2:
      p = exp // 3
      if p > 0:
        p -= 1
      out += ' ' + unitPrefixes[p] + unit
    else:
      out += 'e' + expstr
      if unit != '':
        out += ' ' + unit
  else:
    out += ' ' + unit

  return out

def lst(val, err=[], name='', unit='', prefix=True, expToFix=None):
  """
  Parameters

  val: array of floats with length N
  err: array of floats with length N, uncertainties of val
  name: string, name of the list
  ----------
  Returns

  array of strings, format "val[i] ± err[i]" with significant digits
  """
  # Use zeros in case of empty err
  if (err == []):
    err = [0.0 for i in range(len(val))]

  # Use most frequent exponent (multiple of 3)
  N = len(val)
  lstExp = expToFix
  if expToFix == None or prefix:
    exps = np.zeros(N)
    for i in range(N):
      _, _, exps[i] = sigval(val[i], err[i], True)
    exps, counts = np.unique(exps, return_counts=True)
    lstExp = int(exps[np.argmax(counts)])

  # Determine maximal val and err lengths
  valmaxlen = 0
  errmaxlen = 0
  for i in range(N):
    tmp = sigval(val[i], err[i], True, lstExp)
    if (len(tmp[0]) > valmaxlen):
      valmaxlen = len(tmp[0])
    if (len(tmp[1]) > errmaxlen):
      errmaxlen = len(tmp[1])
  
  # Create and center title
  out = []
  title = ''
  if (name != ''):
    title += name
  if unit != '' or lstExp != 0:
    title += ' / '
    if prefix and unit != '':
      p = lstExp // 3
      if p == 0:
        title += unit
      else:
        if p > 0:
          p -= 1
        title += unitPrefixes[p] + unit
    else:
      if unit != '':
        title += '(' + 'e' + str(lstExp) + ' ' + unit + ')'
      else:
        title += 'e' + str(lstExp) + ' ' + unit
  pos = int(np.floor((valmaxlen + errmaxlen + 3 + len(title))/2))
  out.append(title.rjust(pos))

  # Write and adjust value error strings to out
  for i in range(len(val)):
    tmp = sigval(val[i], err[i], True, lstExp)
    tmp2 = tmp[0].ljust(valmaxlen)
    if (tmp[1] != ''):
      tmp2 += ' ± ' + tmp[1].ljust(errmaxlen)
    elif (errmaxlen != 0):
      tmp2 += ''.ljust(errmaxlen + 3)
    out.append(tmp2)
  
  return out

def tbl(lists, name=''):
  """
  Parameters

  lists: array of rowarrays with length N, which should be arrays with length M of the column strings
  name: string, which is added before the table
  ----------
  Returns

  string of the MxN array
  """
  M = len(lists[0])
  N = len(lists)
  out = ''
  if (name != ''):
    out += name + ':\n'
  lens = [int(npfarray([len(lists[i][j]) for j in range(M)]).max()) for i in range(N)]
  for j in range(M):
    for i in range(N):
      suffix = ' | '
      if (i == N-1):
        suffix = '\n' 
      out += lists[i][j].ljust(lens[i]) + suffix
  return out

def sig(name, val1, err1, val2, err2=0.0, perc=False):
  ### deprecated, use dev instead
  return dev(val1,err1,val2,err2,name=name,perc=perc)

def dev(val1, err1, val2, err2=0.0, name='', perc=False):
  def get_sig(nominator, denominator):
    if (nominator == 0.0):
      sigstr = '0'
    elif (denominator == 0.0):
      sigstr = '∞ '
    else:
      sigma = nominator / denominator
      if (sigma < 0.95):
        digits = int(abs(np.floor(np.log10(sigma))))
      elif (sigma < 3.95):
        digits = 1
      else:
        digits = 0
      sigstr = '{:.{digits}f}'.format(sigma,digits=digits)
    sigstr += 'σ'
    return sigstr

  def get_perc(val1,val2,pformat='{:.2f}'):
    percval = abs(val1 - val2) / val2 * 100
    percstr = pformat.format(percval) + '%'
    return percstr

  out = None
  nominator = abs(val1 - val2)
  denominator = np.sqrt(err1**2 + err2**2)
  if type(val1) is np.ndarray:
    out = []
    N = len(val1)
    if type(denominator) is not np.ndarray:
      denominator = npfarray([denominator for i in range(N)])
    if perc:
      if type(val2) is not np.ndarray:
        val2 = npfarray([val2 for i in range(N)])
      tmp = []
      tmp2 = []
      sigmaxlen = 0
      percmaxlen = 0
      for i in range(N):
        tmp.append(get_sig(nominator[i],denominator[i]))
        siglen = len(tmp[i])
        if (siglen > sigmaxlen):
          sigmaxlen = siglen
        tmp2.append(get_perc(val1[i],val2[i]))
        perclen = len(tmp2[i])
        if (perclen > percmaxlen):
          percmaxlen = perclen
      if (name != ''):
        adjust = int(np.floor((sigmaxlen/2 + 2 + len(name))))
        out.append(name.rjust(adjust))
      for i in range(N):
        out.append(tmp[i].rjust(sigmaxlen) + ' | ' + tmp2[i].rjust(percmaxlen))
    else:
      if (name != ''):
        out.append(name)
      for i in range(N):
        out.append(get_sig(nominator[i],denominator[i]))
  else:
    out = ''
    prefix = ''
    if (name != ''):
      prefix = name + ': '
    out += prefix + get_sig(nominator,denominator)
    if perc:
      out += ' ; ' + get_perc(val1,val2,pformat='{:.2g}')
  return out

def chi2(yo, dyo, ye, dye=[]):
  if (dye == []):
    dye = [0.0 for i in range(len(ye))]
  chi2 = 0.0
  for i in range(len(yo)):
    chi2 += (yo[i] - ye[i])**2 / (dyo[i]**2 + dye[i]**2)
  return chi2

def chi2_red(yo, dyo, ye, dye=[], dof=0):
  if (dof == 0):
    dof = len(ye)
  return chi2(yo, dyo, ye, dye) / dof

class pltext:
  @staticmethod
  def initplot(num=0, nrows=1, ncols=1, title='', xlabel='', ylabel='', scale='linlin', fignum=False):
    fig, axs = plt.subplots(nrows=nrows, ncols=ncols)
    if fignum:
      if nrows != 1 or ncols != 1:
        st = fig.suptitle('Diagramm ' + str(num) + ': ' + title, fontsize='14')
      else:
        plt.title('Diagramm ' + str(num) + ': ' + title, fontsize='14')
    else:
      if nrows != 1 or ncols != 1:
        st = fig.suptitle(title, fontsize='14')
      else:
        plt.title(title, fontsize='14')
    for ax in np.array([axs]).reshape(-1):
      ax.set_xlabel(xlabel)
      ax.set_ylabel(ylabel)
      ax.grid(True, which='both')
      if (scale == 'linlin'):
        ax.ticklabel_format(style='sci', axis='both', scilimits=(-2,3))
      elif (scale == 'linlog'):
        ax.set_yscale('log')
        ax.ticklabel_format(style='sci', axis='x', scilimits=(-2,3))
      elif (scale == 'loglin'):
        ax.set_xscale('log')
        ax.ticklabel_format(style='sci', axis='y', scilimits=(-2,3))
      elif (scale == 'loglog'):
        ax.set_yscale('log')
        ax.set_xscale('log')
    fig.set_size_inches(11.69,8.27)
    fig.tight_layout()
    if nrows != 1 or ncols != 1:
      st.set_y(0.97)
      fig.subplots_adjust(top=0.92)

  @staticmethod
  def set_axis(num):
    plt.sca(plt.gcf().axes[num])

  @staticmethod
  def plotdata(x, y, dy=[], dx=[], label='', color=None, connect=False):
    # Do not plot uncertainties if they are zero
    if all(err == 0.0 for err in dx):
      dx = []
    if all(err == 0.0 for err in dy):
      dy = []
    
    # Plot data with errorbars, excluding empty uncertainties
    if (dx == [] and dy == []):
      plot = plt.errorbar(x=x, y=y, label=label, color=color, fmt='o', markersize=3, capsize=5)
    elif (dx == [] and dy != []):
      plot = plt.errorbar(x=x, y=y, yerr=dy, label=label, color=color, fmt='o', markersize=3, capsize=5)
    elif (dx != [] and dy == []):
      plot = plt.errorbar(x=x, y=y, xerr=dx, label=label, color=color, fmt='o', markersize=3, capsize=5)
    else:
      plot = plt.errorbar(x=x, y=y, yerr=dy, xerr=dx, label=label, color=color, fmt='o', markersize=3, capsize=5)
    
    # Other plot options
    for cap in plot[1]:
      cap.set_markeredgewidth(1)
    if (connect == True):
      if (color == None):
        color = plot[0].get_color()
      plt.plot(x, y, color=color)
    if (label != ''):
      plt.legend()
    return plot
  
  @staticmethod
  def savefigs(path):
    # Save figures in 'path' as figN.pdf, where N is the figures number
    for i in plt.get_fignums():
      plt.figure(i).savefig(path + '/fig' + str(i) +'.pdf', papertype='a4', orientation='landscape', bbox_inches='tight', pad_inches=0.3, format='pdf')

def linreg(x, y, dy, dx=[], fit_range=None, plot=False, graphname='', legend=False):
  if (fit_range == None):
    fit_range = range(len(x))
  def linreg_iter(x, y, dy):
    [s0, s1, s2, s3, s4] = [0.0, 0.0, 0.0, 0.0, 0.0]
    for i in fit_range:
      if (dy[i] == 0.0):
        dy[i] = minfloat
      s0 += dy[i]**-2
      s1 += x[i] * dy[i]**-2
      s2 += y[i] * dy[i]**-2
      s3 += x[i]**2 * dy[i]**-2
      s4 += x[i] * y[i] * dy[i]**-2
    eta = s0 * s3 - s1**2
    g = (s0 * s4 - s1 * s2) / eta
    dg = np.sqrt(s0 / eta)
    b = (s3 * s2 - s1 * s4) / eta
    db = np.sqrt(s3 / eta)
    return [g, dg, b, db]

  iter0 = linreg_iter(x, y, dy)
  result = []
  if (dx == []):
    dx = [0.0 for i in range(len(x))]
    result = iter0
  else:
    g = iter0[0]
    g_old = g * (1 - 2 * linreg_change)
    dy_ = dy
    while (abs(1 - g_old / g) >= linreg_change):
      g_old = g
      dy_ = np.sqrt((g * dx)**2 + dy_**2)
      g = linreg_iter(x, y, dy_)[0]
    result = linreg_iter(x, y, dy_)
  if (plot):
    [g, dg, b, db] = result
    min_x = np.argmin(x)
    max_x = np.argmax(x)
    xint = nplinspace(x[min_x] - dx[min_x], x[max_x] + dx[max_x])
    yfit = g * xint + b
    yerr = (g + dg) * xint + (b - db)
    data_plot = pltext.plotdata(x=x, y=y, dy=dy, dx=dx, label=graphname)
    color = data_plot[0].get_color()
    left, right = plt.xlim()
    top, bottom = plt.ylim()
    plt.plot(xint, yfit, marker='', color=color)
    plt.plot(xint, yerr, marker='', linestyle='dashed', color=color)
    plt.xlim(left, right)
    plt.ylim(top, bottom)
    if (legend):
      plt.legend(['Fit', 'Fit uncertainty'])
    elif (graphname != ''):
      plt.legend()
  return result

def expreg(x, y, dy, dx=[], fit_range=None, plot=True):
  if fit_range == None:
    fit_range = range(len(x))
  if dx == []:
    dx = np.zeros(len(x))
  expo, dexpo, _yitc, _dyitc = linreg(x, np.log(y), dy/y, dx, fit_range=fit_range)
  yitc = exp(_yitc)
  dyitc = yitc * _dyitc
  result = [expo,dexpo,yitc,dyitc]
  if (plot):
    min_x = np.argmin(x)
    max_x = np.argmax(x)
    xint = np.linspace(x[min_x] - dx[min_x], x[max_x] + dx[max_x], 1000)
    yfit = yitc * exp(expo * xint)
    yerr = (yitc - dyitc) * exp((expo + dexpo) * xint)
    data_plot = pltext.plotdata(x=x, y=y, dy=dy, dx=dx)
    color = data_plot[0].get_color()
    left, right = plt.xlim()
    top, bottom = plt.ylim()
    plt.plot(xint, yfit, marker='', color=color)
    plt.plot(xint, yerr, marker='', linestyle='dashed', color=color)
    plt.xlim(left, right)
    plt.ylim(top, bottom)
  return result

def fit(x, y, dy, f, p0=None, fit_range=None, plot=True):
  if fit_range == None:
    fit_range = range(len(x))
  x_fit = [x[i] for i in fit_range]
  y_fit = [y[i] for i in fit_range]
  dy_fit = [dy[i] for i in fit_range]
  p, d_p = curve_fit(f, x_fit, y_fit, sigma=dy_fit, p0=p0)
  if plot:
    xint = np.linspace(np.min(x), np.max(x), 1000)
    yfit = f(xint, *p)
    data_plot = pltext.plotdata(x, y, dy)
    color = data_plot[0].get_color()
    left, right = plt.xlim()
    top, bottom = plt.ylim()
    plt.plot(xint, yfit, marker='', color=color)
    plt.xlim(left, right)
    plt.ylim(top, bottom)
  return (p, sqrt(np.diag(d_p)))

def lin_yerr(x, dx, y, dy):
  g = linreg(x, y, dx, dy)
  new_dy = [np.sqrt(dy[i]**2 + (g * dx[i])**2) for i in range(len(dy))]
  return new_dy
