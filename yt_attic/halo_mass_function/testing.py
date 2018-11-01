"""
Answer testing functions for halo_mass_function



"""

#-----------------------------------------------------------------------------
# Copyright (c) yt Development Team. All rights reserved.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


from yt.utilities.answer_testing.framework import \
    AnswerTestingTest

class SimulatedHaloMassFunctionTest(AnswerTestingTest):
    _type_name = "SimulatedHaloMassFunction"
    _attrs = ("finder",)

    def __init__(self, ds_fn, finder):
        super(SimulatedHaloMassFunctionTest, self).__init__(ds_fn)
        self.finder = finder

    def run(self):
        from yt.extensions.astro_analysis.halo_analysis.api import HaloCatalog
        from yt.extensions.attic.halo_mass_function.api import HaloMassFcn
        hc = HaloCatalog(data_ds=self.ds, finder_method=self.finder)
        hc.create()

        hmf = HaloMassFcn(halos_ds=hc.halos_ds)
        result = np.empty((2, hmf.masses_sim.size))
        result[0] = hmf.masses_sim.d
        result[1] = hmf.n_cumulative_sim.d
        return result

    def compare(self, new_result, old_result):
        err_msg = ("Simulated halo mass functions not equation for " +
                   "%s halo finder.") % self.finder
        assert_equal(new_result, old_result,
                     err_msg=err_msg, verbose=True)

class AnalyticHaloMassFunctionTest(AnswerTestingTest):
    _type_name = "AnalyticHaloMassFunction"
    _attrs = ("fitting_function",)

    def __init__(self, ds_fn, fitting_function):
        super(AnalyticHaloMassFunctionTest, self).__init__(ds_fn)
        self.fitting_function = fitting_function

    def run(self):
        from yt.extensions.attic.halo_mass_function.api import HaloMassFcn
        hmf = HaloMassFcn(simulation_ds=self.ds,
                          fitting_function=self.fitting_function)
        result = np.empty((2, hmf.masses_analytic.size))
        result[0] = hmf.masses_analytic.d
        result[1] = hmf.n_cumulative_analytic.d
        return result

    def compare(self, new_result, old_result):
        err_msg = ("Analytic halo mass functions not equal for " +
                   "fitting function %d.") % self.fitting_function
        assert_almost_equal(new_result, old_result,
                            err_msg=err_msg, verbose=True)
