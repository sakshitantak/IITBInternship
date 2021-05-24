import re
from flask import Flask
from flask import render_template, request
import math

app = Flask(__name__)

app.config.from_object(__name__)

@app.route('/', methods = ['POST', 'GET'])
def laminates_bs6464():
    return render_template("laminates_bs6464.html",
                        K = 0,
                        K1 = 0,
                        K2 = 0,
                        K3 = 0,
                        K4 = 0,
                        K5 = 0,
                        F = 0,
                        extension_to_failure_for_resin = 0,
                        U_csm = 0,
                        U_wrm = 0,
                        U_filament = 0,
                        UL_csm = 0,
                        UL_wrm = 0,
                        UL_filament = 0,
                        X_csm = 0,
                        X_wrm = 0,
                        X_filament = 0,
                        load_limiting_strain_csm = 0,
                        load_limiting_strain_wrm = 0,
                        load_limiting_strain_filament = 0,
                        internal_laminal_shear_strength_csm = 0,
                        internal_laminal_shear_strength_wrm = 0,
                        internal_laminal_shear_strength_filament = 0,
                        maximum_allowable_lamina_design_strain_csm = 0,
                        maximum_allowable_lamina_design_strain_wrm = 0,
                        maximum_allowable_lamina_design_strain_filament = 0,
                        glass_fiber_mass_fraction_csm = 0,
                        glass_fiber_mass_fraction_wrm = 0,
                        glass_fiber_mass_fraction_filament = 0,
                        allowable_design_strain_csm = 0,
                        allowable_design_strain_wrm = 0,
                        allowable_design_strain_filament = 0,
                        R_csm = 0,
                        R_wrm = 0,
                        R_filament = 0,
                        final_allowable_design_strain_csm = 0,
                        final_allowable_design_strain_wrm = 0,
                        final_allowable_design_strain_filament = 0,
                        Us_csm = 0,
                        Us_wrm = 0,
                        relative_density = 0,
                        Uz_csm = 0,
                        Uz_wrm = 0,
                        ti_csm = 0,
                        ti_wrm = 0,
                        ti_filament = 0,
                        xphi_filament = 0,
                        ultimate_tensile_strength_csm = 0,
                        ultimate_tensile_strength_wrm = 0,
                        ultimate_tensile_strength_filament = 0,
                        xx_filament = 0,
                        allowable_resin_strain_csm = 0,
                        allowable_resin_strain_wrm = 0,
                        allowable_resin_strain_filament = 0,
                        uphi_filament = 0,
                        tg_csm = 0,
                        tg_wrm = 0,
                        tg_filament = 0,
                        ux_filament = 0,
                        tex_filament = 0,
                        fphi_filament = 0,
                        width_of_roving_filament = 0,
                        fx_filament = 0,
                        winding_angle_filament = 0,
                        flexural_modulus_filament = 0
                        )


if __name__ == '__main__':
    app.run(debug=True)