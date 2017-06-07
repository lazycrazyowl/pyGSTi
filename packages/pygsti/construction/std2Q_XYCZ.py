from __future__ import division, print_function, absolute_import, unicode_literals
"""
Variables for working with the 2-qubit gate set containing the gates
I*X(pi/2), I*Y(pi/2), X(pi/2)*I, Y(pi/2)*I, and CZ.
"""

from pygsti.construction import gatestringconstruction as _strc
from pygsti.construction import gatesetconstruction as _setc
from pygsti.construction import spamspecconstruction as _spamc

description = "I*X(pi/2), I*Y(pi/2), X(pi/2)*I, Y(pi/2)*I, and CZ gates"

gates = ['Gix', 'Giy', 'Gxi', 'Gyi', 'Gcz']

fiducials16 = _strc.gatestring_list(
    [(), ('Gix',), ('Giy',), ('Gix', 'Gix'),
     ('Gxi',), ('Gxi', 'Gix'), ('Gxi', 'Giy'), ('Gxi', 'Gix', 'Gix'),
     ('Gyi',), ('Gyi', 'Gix'), ('Gyi', 'Giy'), ('Gyi', 'Gix', 'Gix'),
     ('Gxi', 'Gxi'), ('Gxi', 'Gxi', 'Gix'), ('Gxi', 'Gxi', 'Giy'), ('Gxi', 'Gxi', 'Gix', 'Gix')])

fiducials36 = _strc.gatestring_list(
    [(), ('Gix',), ('Giy',), ('Gix', 'Gix'), ('Gix', 'Gix', 'Gix'), ('Giy', 'Giy', 'Giy'),
     ('Gxi',), ('Gxi', 'Gix'), ('Gxi', 'Giy'), ('Gxi', 'Gix', 'Gix'), ('Gxi', 'Gix', 'Gix', 'Gix'),
     ('Gxi', 'Giy', 'Giy', 'Giy'), ('Gyi',), ('Gyi', 'Gix'), ('Gyi', 'Giy'), ('Gyi', 'Gix', 'Gix'),
     ('Gyi', 'Gix', 'Gix', 'Gix'), ('Gyi', 'Giy', 'Giy', 'Giy'), ('Gxi', 'Gxi'),
     ('Gxi', 'Gxi', 'Gix'), ('Gxi', 'Gxi', 'Giy'), ('Gxi', 'Gxi', 'Gix', 'Gix'),
     ('Gxi', 'Gxi', 'Gix', 'Gix', 'Gix'), ('Gxi', 'Gxi', 'Giy', 'Giy', 'Giy'),
     ('Gxi', 'Gxi', 'Gxi'), ('Gxi', 'Gxi', 'Gxi', 'Gix'), ('Gxi', 'Gxi', 'Gxi', 'Giy'),
     ('Gxi', 'Gxi', 'Gxi', 'Gix', 'Gix'), ('Gxi', 'Gxi', 'Gxi', 'Gix', 'Gix', 'Gix'),
     ('Gxi', 'Gxi', 'Gxi', 'Giy', 'Giy', 'Giy'), ('Gyi', 'Gyi', 'Gyi'),
     ('Gyi', 'Gyi', 'Gyi', 'Gix'), ('Gyi', 'Gyi', 'Gyi', 'Giy'),
     ('Gyi', 'Gyi', 'Gyi', 'Gix', 'Gix'), ('Gyi', 'Gyi', 'Gyi', 'Gix', 'Gix', 'Gix'),
     ('Gyi', 'Gyi', 'Gyi', 'Giy', 'Giy', 'Giy')])

fiducials = fiducials16
prepStrs = fiducials16

effectStrs = _strc.gatestring_list(
    [(), ('Gix',), ('Giy',), 
     ('Gix', 'Gix'), ('Gxi',),
     ('Gyi',), ('Gxi', 'Gxi'),
     ('Gxi', 'Gix'), ('Gxi', 'Giy'),
     ('Gyi', 'Gix'), ('Gyi', 'Giy')])

legacy_effectStrs = _strc.gatestring_list(
    [(), ('Gix',), ('Giy',), ('Gxi',), ('Gyi',),
     ('Gix', 'Gxi'), ('Gxi', 'Giy'), ('Gyi', 'Gix'),
     ('Gyi', 'Giy'), ('Gxi', 'Gxi')])

germs = _strc.gatestring_list(
    [('Gxi',), ('Gyi',), ('Gix',), ('Giy',), ('Gcz',),
     ('Gxi', 'Gyi'), ('Gix', 'Giy'), ('Giy', 'Gyi'), ('Gix', 'Gyi'),
     ('Gyi', 'Gcz'), ('Giy', 'Gcz'),
     ('Gxi', 'Gcz', 'Gcz'),
     ('Giy', 'Gxi', 'Gcz'),
     ('Giy', 'Gcz', 'Gyi'),
     ('Giy', 'Gyi', 'Gcz'),
     ('Gix', 'Gxi', 'Gcz'),
     ('Giy', 'Giy', 'Gcz'),
     ('Giy', 'Gcz', 'Gxi'),
     ('Gix', 'Giy', 'Gcz'),
     ('Giy', 'Gxi', 'Gyi'),
     ('Gix', 'Giy', 'Gyi'),
     ('Gyi', 'Gyi', 'Gyi', 'Gxi'),
     ('Giy', 'Giy', 'Giy', 'Gix'),
     ('Gxi', 'Gyi', 'Gix', 'Giy'),
     ('Gcz', 'Gix', 'Gyi', 'Gyi'),
     ('Gcz', 'Gix', 'Gix', 'Gcz'),
     ('Gxi', 'Gcz', 'Gyi', 'Gyi'),
     ('Gyi', 'Gyi', 'Gyi', 'Gix'),
     ('Gix', 'Gix', 'Giy', 'Gcz', 'Gcz'),
     ('Gcz', 'Giy', 'Giy', 'Gix', 'Giy'),
     ('Gyi', 'Gcz', 'Gix', 'Giy', 'Gyi'),
     ('Giy', 'Gxi', 'Gcz', 'Gxi', 'Gcz'),
     ('Gyi', 'Gcz', 'Gxi', 'Gcz', 'Gxi'),
     ('Gyi', 'Gxi', 'Gyi', 'Gxi', 'Gxi', 'Gxi'),
     ('Gyi', 'Gxi', 'Gyi', 'Gyi', 'Gxi', 'Gxi'),
     ('Gyi', 'Gyi', 'Gyi', 'Gxi', 'Gyi', 'Gxi'),
     ('Gxi', 'Gxi', 'Gyi', 'Gxi', 'Gyi', 'Gyi'),
     ('Giy', 'Gix', 'Giy', 'Gix', 'Gix', 'Gix'),
     ('Giy', 'Gix', 'Giy', 'Giy', 'Gix', 'Gix'),
     ('Giy', 'Giy', 'Giy', 'Gix', 'Giy', 'Gix'),
     ('Gix', 'Gix', 'Giy', 'Gix', 'Giy', 'Giy'),
     ('Gcz', 'Gyi', 'Giy', 'Gxi', 'Gix', 'Gcz'),
     ('Gxi', 'Giy', 'Gxi', 'Gcz', 'Gyi', 'Gix'),
     ('Gxi', 'Giy', 'Giy', 'Giy', 'Gcz', 'Gxi'),
     ('Gcz', 'Gxi', 'Gcz', 'Gxi', 'Giy', 'Gix'),
     ('Gyi', 'Gix', 'Gyi', 'Gix', 'Gxi', 'Gxi'),
     ('Gix', 'Gcz', 'Gxi', 'Gix', 'Gxi', 'Gcz'),
     ('Gxi', 'Giy', 'Gyi', 'Gxi', 'Gcz', 'Gcz'),
     ('Gix', 'Gix', 'Giy', 'Gcz', 'Giy', 'Gcz', 'Gxi'),
     ('Giy', 'Gxi', 'Gcz', 'Gix', 'Gix', 'Giy', 'Giy'),
     ('Gxi', 'Gcz', 'Giy', 'Gyi', 'Gxi', 'Gix', 'Giy'),
     ('Gcz', 'Gcz', 'Gix', 'Gxi', 'Giy', 'Gxi', 'Gxi'),
     ('Gxi', 'Gix', 'Giy', 'Gyi', 'Gix', 'Gix', 'Gix'),
     ('Gxi', 'Gix', 'Gyi', 'Gix', 'Gyi', 'Giy', 'Gyi'),
     ('Gix', 'Gix', 'Gix', 'Gix', 'Gxi', 'Gxi', 'Gyi'),
     ('Giy', 'Gcz', 'Gxi', 'Gyi', 'Gyi', 'Gcz', 'Gix', 'Gcz'),
     ('Gxi', 'Gyi', 'Gxi', 'Giy', 'Gxi', 'Giy', 'Gix', 'Giy'),
     ('Giy', 'Giy', 'Gyi', 'Gix', 'Gcz', 'Gxi', 'Gyi', 'Gyi'),
     ('Gxi', 'Gix', 'Gcz', 'Gyi', 'Gix', 'Gcz', 'Gix', 'Giy'),
     ('Gix', 'Gxi', 'Gxi', 'Giy', 'Gxi', 'Gyi', 'Gix', 'Gcz'),
     ('Gix', 'Gix', 'Gyi', 'Gxi', 'Giy', 'Gix', 'Gcz', 'Gyi'),
     ('Gix', 'Giy', 'Gix', 'Gxi', 'Gix', 'Giy', 'Gxi', 'Gxi'),
     ('Giy', 'Gix', 'Gcz', 'Gxi', 'Gcz', 'Gxi', 'Gcz', 'Gyi'),
     ('Gxi', 'Giy', 'Gix', 'Gix', 'Gxi', 'Giy', 'Gxi', 'Gcz'),
     ('Gyi', 'Gyi', 'Gyi', 'Gyi', 'Gix', 'Giy', 'Gix', 'Gyi')
     ])

legacy_germs = _strc.gatestring_list(
    [('Giy',),
     ('Gxi',),
     ('Gyi',),
     ('Gcz',),
     ('Gix', 'Gyi'),
     ('Giy', 'Gyi'),
     ('Giy', 'Gcz'),
     ('Gyi', 'Gcz'),
     ('Gix', 'Gix', 'Giy'),
     ('Gix', 'Gix', 'Gyi'),
     ('Gix', 'Giy', 'Giy'),
     ('Gix', 'Giy', 'Gyi'),
     ('Gix', 'Giy', 'Gcz'),
     ('Gix', 'Gxi', 'Gcz'),
     ('Gix', 'Gcz', 'Giy'),
     ('Gix', 'Gcz', 'Gyi'),
     ('Giy', 'Giy', 'Gxi'),
     ('Giy', 'Giy', 'Gcz'),
     ('Giy', 'Gxi', 'Gyi'),
     ('Giy', 'Gxi', 'Gcz'),
     ('Giy', 'Gyi', 'Gxi'),
     ('Giy', 'Gyi', 'Gcz'),
     ('Giy', 'Gcz', 'Gxi'),
     ('Giy', 'Gcz', 'Gyi'),
     ('Gxi', 'Gxi', 'Gyi'),
     ('Gxi', 'Gxi', 'Gcz'),
     ('Gxi', 'Gyi', 'Gyi'),
     ('Gxi', 'Gcz', 'Gcz'),
     ('Gcz', 'Gix', 'Gyi', 'Gyi'),
     ('Gcz', 'Gix', 'Gix', 'Gcz'),
     ('Gxi', 'Giy', 'Gix', 'Giy'),
     ('Gxi', 'Gyi', 'Gix', 'Giy'),
     ('Gyi', 'Gyi', 'Gyi', 'Gix'),
     ('Gxi', 'Gcz', 'Gyi', 'Gyi'),
     ('Gyi', 'Gcz', 'Gix', 'Giy', 'Gyi'),
     ('Gix', 'Gix', 'Giy', 'Gcz', 'Gcz'),
     ('Giy', 'Gxi', 'Gcz', 'Gxi', 'Gcz'),
     ('Gyi', 'Gcz', 'Gxi', 'Gcz', 'Gxi'),
     ('Gcz', 'Giy', 'Giy', 'Gix', 'Giy'),
     ('Giy', 'Gix', 'Gix', 'Gyi', 'Gxi'),
     ('Giy', 'Gix', 'Gyi', 'Giy', 'Giy'),
     ('Gcz', 'Gxi', 'Gcz', 'Gix', 'Gyi'),
     ('Gix', 'Gix', 'Gyi', 'Gxi', 'Gyi', 'Gix'),
     ('Gxi', 'Giy', 'Gyi', 'Gxi', 'Gcz', 'Gcz'),
     ('Gcz', 'Gyi', 'Gcz', 'Gxi', 'Gyi', 'Gyi'),
     ('Gxi', 'Giy', 'Gxi', 'Gcz', 'Gyi', 'Gix'),
     ('Gcz', 'Gyi', 'Giy', 'Gxi', 'Gix', 'Gcz'),
     ('Gcz', 'Gxi', 'Gcz', 'Gxi', 'Giy', 'Gix'),
     ('Gxi', 'Gxi', 'Giy', 'Gix', 'Giy', 'Gix'),
     ('Gxi', 'Giy', 'Giy', 'Giy', 'Gcz', 'Gxi'),
     ('Gyi', 'Gix', 'Gyi', 'Gix', 'Gxi', 'Gxi'),
     ('Gix', 'Gcz', 'Gxi', 'Gix', 'Gxi', 'Gcz'),
     ('Gxi', 'Gix', 'Giy', 'Gyi', 'Gix', 'Gix', 'Gix'),
     ('Gyi', 'Gxi', 'Gyi', 'Giy', 'Giy', 'Gxi', 'Gix'),
     ('Gcz', 'Gcz', 'Gix', 'Gxi', 'Giy', 'Gxi', 'Gxi'),
     ('Gxi', 'Gcz', 'Giy', 'Gyi', 'Gxi', 'Gix', 'Giy'),
     ('Gxi', 'Gix', 'Gyi', 'Gix', 'Gyi', 'Giy', 'Gyi'),
     ('Gix', 'Gcz', 'Giy', 'Gcz', 'Gcz', 'Gix', 'Gix'),
     ('Giy', 'Gxi', 'Gcz', 'Gix', 'Gix', 'Giy', 'Giy'),
     ('Gix', 'Gix', 'Gix', 'Gix', 'Gxi', 'Gxi', 'Gyi'),
     ('Gix', 'Gix', 'Giy', 'Gcz', 'Giy', 'Gcz', 'Gxi'),
     ('Gxi', 'Giy', 'Gix', 'Gix', 'Gxi', 'Giy', 'Gxi', 'Gcz'),
     ('Giy', 'Gix', 'Gcz', 'Gxi', 'Gcz', 'Gxi', 'Gcz', 'Gyi'),
     ('Gix', 'Giy', 'Gix', 'Gxi', 'Gix', 'Giy', 'Gxi', 'Gxi'),
     ('Gix', 'Gix', 'Gyi', 'Gxi', 'Giy', 'Gix', 'Gcz', 'Gyi'),
     ('Gxi', 'Gyi', 'Gxi', 'Giy', 'Gxi', 'Giy', 'Gix', 'Giy'),
     ('Giy', 'Giy', 'Gyi', 'Gix', 'Gcz', 'Gxi', 'Gyi', 'Gyi'),
     ('Gix', 'Gxi', 'Gxi', 'Giy', 'Gxi', 'Gyi', 'Gix', 'Gcz'),
     ('Gyi', 'Gyi', 'Gyi', 'Gyi', 'Gix', 'Giy', 'Gix', 'Gyi'),
     ('Gxi', 'Gix', 'Gcz', 'Gyi', 'Gix', 'Gcz', 'Gix', 'Giy'),
     ('Giy', 'Gcz', 'Gxi', 'Gyi', 'Gyi', 'Gcz', 'Gix', 'Gcz')])

#Construct the target gateset
gs_target = _setc.build_gateset(
    [4], [('Q0', 'Q1')], ['Gix', 'Giy', 'Gxi', 'Gyi', 'Gcz'],
    ["X(pi/2,Q1)", "Y(pi/2,Q1)", "X(pi/2,Q0)", "Y(pi/2,Q0)", "CZ(pi,Q0,Q1)"],
    prepLabels=['rho0'], prepExpressions=["0"],
    effectLabels=['E0', 'E1', 'E2'], effectExpressions=["0", "1", "2"],
    spamdefs={'upup': ('rho0', 'E0'), 'updn': ('rho0', 'E1'),
              'dnup': ('rho0', 'E2'), 'dndn': ('rho0', 'remainder')}, basis="pp")


specs16x10 = _spamc.build_spam_specs(
    prepStrs=prepStrs,
    effectStrs=effectStrs,
    prep_labels=gs_target.get_prep_labels(),
    effect_labels=gs_target.get_effect_labels())

specs16 = _spamc.build_spam_specs(
    fiducials16,
    prep_labels=gs_target.get_prep_labels(),
    effect_labels=gs_target.get_effect_labels())

specs36 = _spamc.build_spam_specs(
    fiducials36,
    prep_labels=gs_target.get_prep_labels(),
    effect_labels=gs_target.get_effect_labels())

specs = specs16x10 #use smallest specs set as "default"
