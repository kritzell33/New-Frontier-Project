

from dataclasses import dataclass
import mesa

@dataclass
class CrewAgent(mesa.Agent):
    unique_id: int
    model: mesa.Model

    name: str
    age: str
    gender: str
    role: str

    ##PersonalityTraits(Core)##
    hex_h: float
    hex_e: float
    hex_x: float
    hex_a: float
    hex_c: float
    hex_o: float
    neo_n: float
    neo_e: float
    neo_o: float
    neo_a: float
    neo_c: float
    bfas_vol: float
    bfas_with: float
    bfas_enth: float
    bfas_asst: float
    bfas_intl: float
    bfas_open: float
    bfas_comp: float
    bfas_pol: float
    bfas_indu: float
    bfas_ord: float
    bis: float
    bis_d: float
    bis_f: float
    bis_r: float
    mach: float
    npi: float
    lsrp_p: float
    lsrp_s: float
    soi_beh: float
    soi_att: float  
    soi_des: float
    soi: float
    buss_avg: float
    buss_kind: float
    buss_values: float
    buss_physat: float
    buss_health: float
    buss_family: float
    buss_intel: float
    buss_educ: float
    buss_earn: float
    buss_stab: float
    loc_i: float
    loc_p: float
    loc_c: float
    sm: float
    lot_r: float
    cfq_sum: float
    orvis_lead: float
    orvis_org: float
    orvis_alt: float
    orvis_cre: float
    orvis_ana: float
    orvis_pro: float
    orvis_adv: float
    orvis_eru: float
    catpd_rig: float
    catpd_ed: float
    catpd_ri: float
    catpd_man: float
    catpd_cal: float
    catpd_np: float
    catpd_wkh: float
    catpd_al: float
    catpd_ha: float
    catpd_sw: float
    catpd_npl: float
    via_crea: float
    via_curi: float
    via_judg: float
    via_lrnl: float
    via_persp: float
    via_brav: float
    via_persv: float
    via_hon: float
    via_zest: float
    via_love: float
    via_kind: float
    via_si: float
    via_team: float
    via_fair: float
    via_lead: float
    via_forg: float
    via_humb: float
    via_prud: float
    via_sr: float
    via_beau: float
    via_grat: float
    via_hope: float
    via_humo: float
    via_spir: float
    self_control: float

    ##PersonalityTraits(Mate)##
    #WIP Mainly comes into play at Level 3, but nees to be able to account for level 1-2 anomolies.  

    ##PersonalityTraits(Sleep)##
    meq: int
    psqi: int
    circadian_chronotype: int

    ##PsychologicalCompounds(Core)##
    acute_stress: float #(Source: 01,...)
    chronic_stress: float
    sleep_debt_h: float
    sleep_pressure_S: float
    circadian_C: float
    wakeup_penalty: float
    mental_fatigue: float
    vigilance: float #Complacientcy grows with time. Find study giving estimated time

    ##PsychologicalEmotionalCompounds(Core)##
    valence: float
    arousal: float
    #X and Y axis built around a polar chart of current emotional state  

    ##BodyStateCompounds(Core)##
    physical_fatigue: float
    #Will need to be expanded to precise pody parts/areas
    #Excercise_Science????

    ##PsychologicalOutputs(Core)##
    alertness: float #`f(C − S − debt_penalty − inertia)`#
    general_cognitive_effectiveness: float
    long_term_cognition: float
    short_term_cognition: float


    def __post_init__(self):
       #Mesa Additions
        super().__init__(self.unique_id, self.model)