import openmdao.api as om

class firstComponent(om.ExplicitComponent):

    def setup(self):
        # input
        self.add_input('x', val=5.0, desc="variable x")

        # output
        self.add_output('y')

    def setup_partials(self):
        self.declare_partials('*', '*')

    def compute(self, inputs, outputs):
        # retrieve the inputs
        x = inputs['x']
        outputs['y'] = x ** 2
