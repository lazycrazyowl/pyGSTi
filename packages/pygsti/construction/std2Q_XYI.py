from pygsti.construction import gatestringconstruction as _strc
from pygsti.construction import gatesetconstruction as _setc
import itertools

def add_1Q_expts(expt1, expt2):
    all_expt = itertools.product(expt1, expt2)
    ret_expts = []

    for expt in all_expt:
        ret_expt = []
        for f in expt[0]:
            for g in expt[1]:
                ret_expt.append(f + g[-1])
        ret_expts.append(tuple(ret_expt))

    return ret_expts

fid_1Q = [('Gi',), ('Gx',), ('Gy',), ('Gx','Gx'), ('Gx','Gx','Gx'), ('Gy','Gy','Gy')]

germs_1Q = [('Gx',), ('Gy',), ('Gi',), ('Gx', 'Gy'), ('Gx', 'Gy', 'Gi'), ('Gx', 'Gi', 'Gy'),
            ('Gx', 'Gi', 'Gi'), ('Gy', 'Gi', 'Gi'), ('Gx', 'Gx', 'Gi', 'Gy'),
            ('Gx', 'Gy', 'Gy', 'Gi'), ('Gx', 'Gx', 'Gy', 'Gx', 'Gy', 'Gy')]

prepStrs = effectStrs = _strc.gatestring_list(add_1Q_expts(fid_1Q, fid_1Q))

germs = _strc.gatestring_list(add_1Q_expts(germs_1Q, germs_1Q))

gs_target = _setc.build_gateset([4], [('Q0', 'Q1')],['Gix', 'Giy', 'Gxi', 'Gyi'],
    ["I(Q0):X(pi/2,Q1)", "I(Q0):Y(pi/2,Q1)", "X(pi/2,Q0):I(Q1)", "Y(pi/2,Q0):I(Q1)"],
    prepLabels=['rho0'], prepExpressions=["0"],
    effectLabels=['E0', 'E1', 'E2'], effectExpressions=["0", "1", "2"],
    spamdefs={'upup': ('rho0', 'E0'), 'updn': ('rho0', 'E1'),
              'dnup': ('rho0', 'E2'), 'dndn': ('rho0', 'remainder')}, basis="pp")
