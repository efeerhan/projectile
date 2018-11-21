import prm
# startup
print('Welcome to P.E.E.P.E.E.! (ProjectilE Equation Project by Efe Erhan)')
print('This program solves 2-dimensional projectile kinematic problems.')
print('Which value are you solving for?')
prm.options()
solving_for = input()
while(solving_for != 'ia' and
      solving_for != 'fa' and
      solving_for != 'iv' and
      solving_for != 'fv' and
      solving_for != 'vcd' and
      solving_for != 'hcd' and
      solving_for != 'adg' and
      solving_for != 'ti'):
    print('invalid entry, what are you solving for?')
    prm.options()
    solving_for = input()
if solving_for == 'vcd':
    prm.sf_vcd()
elif solving_for == 'hcd':
    prm.sf_hcd()
elif solving_for == 'adg':
    prm.sf_adg()
elif solving_for == 'ti':
    prm.sf_ti()
elif solving_for == 'fv':
    prm.sf_fv()
elif solving_for == 'iv':
    prm.sf_iv()
elif solving_for == 'fa':
    prm.sf_fa()
elif solving_for == 'ia':
    prm.sf_ia()
