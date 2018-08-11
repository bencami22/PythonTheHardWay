print("Let's practice everything")
print('You\'d need to know \'bout escape characaters using the \\ that do:')
print ('\n newlines and \t tabs')

poem="""
\t The local world \n where people use \t technology
"""

print("----------------")
print("poem")
print("-----------------")

five=8-3
print(f"This should be five =  {five}")

def secret_formula(started):
    jelly_beans=started*100
    jars=jelly_beans/23
    crates=jars*4.5
    return jelly_beans, jars, crates

jelly_beans, jars, crates=secret_formula(12)

print("jelly_beans={}, jars={}, crates={}".format(jelly_beans, jars, crates))

print("We can also do it this way:")
formula=secret_formula(12)
print("jelly_beans={}, jars={}, crates={}".format(*formula))
