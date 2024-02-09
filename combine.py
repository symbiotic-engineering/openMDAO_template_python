import openmdao.api as om
from firstComponent import firstComponent
from secondComponent import secondComponent
class combine(om.Group):

    def setup(self):
        self.add_subsystem('first', firstComponent())
        self.add_subsystem('second', secondComponent())


    def configure(self):
        #ivc to geometryComponent
        self.connect('first.y', 'second.a')

if __name__ == "__main__":

    top = om.Problem(model=combine())
    top.setup()
    # run the compute
    top.run_model()
    print(top.get_val('second.b')) #50
    #main()
