import openmdao.api as om
class secondComponent(om.ExplicitComponent):

    def setup(self):
        #input
        self.add_input('a', val=0.0, desc="variable a")

        #output
        self.add_output('b')

    def setup_partials(self):
        self.declare_partials('*', '*')

    def compute(self, inputs, outputs):
        #retrieve the inputs
        a = inputs['a']
        outputs['b'] = a * 2
