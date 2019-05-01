print 'lets practcise everything '
print 'you \'d need to know \'bout escapes with \\ that do \n newlines and \t tabs \v vertical tabs and \b for backspace'
poem = """
\t the lovely world
with logic so firmly planed
cannot discern \n the needs of love
nor comprehend passion from intitution
and requires an explanation
\n\t where there is none.
"""
print "-" * 10
print poem
print '-' * 10
five = 10 - 2 + 3 - 6
print 'this should be five %s' % five
def secret_formula(started):
 jelly = started * 500
 jars = jelly / 1000
 crates = jars / 100
 return jelly , jars , crates

start_point = 10000
beans , jars, crates = secret_formula(start_point)

print 'with a starting point of: %d' % start_point
print 'we would have %d beans , %d jars and %d crates' %(beans,jars,crates)
start_point = start_point / 10
print 'we can also do that this way '
print 'we\'d have %d beans , %d jars and %d crates ' % secret_formula(start_point)

