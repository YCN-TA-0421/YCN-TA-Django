from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Food, Food_analysis, PRODUCTGROEP_OMS_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'index', 'created', 'Productgroep_oms', 'Product_omschrijving', 'ENERCC_kcal', 'PROT_g', 'CHO_g', 'FAT_g']


class FoodAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_analysis
        fields = ['id', 'index', 'Productgroepcode', 'Productgroep_oms', 'Productcode', 'Product_omschrijving', 'Product_description', 'Product_synoniemen', 'Meeteenheid', 'Hoeveelheid', 'Commentaarregel', 'Verrijkt_met', 'Bevat_een_spoor_van', 'ENERCJ_kJ', 'ENERCC_kcal', 'PROT_g', 'PROTPL_g', 'PROTAN_g', 'NT_g', 'CHO_g', 'SUGAR_g', 'STARCH_g', 'POLYL_g', 'FIBT_g', 'ALC_g', 'WATER_g', 'OA_g', 'FAT_g', 'FACID_g', 'FASAT_g', 'FAMSCIS_g', 'FAPU_g', 'FAPUN3_g', 'FAPUN6_g', 'FATRS_g', 'F4_0_g', 'F6_0_g', 'F8_0_g', 'F10_0_g', 'F11_0_g', 'F12_0_g', 'F13_0_g', 'F14_0_g', 'F15_0_g', 'F16_0_g', 'F17_0_g', 'F18_0_g', 'F19_0_g', 'F20_0_g', 'F21_0_g', 'F22_0_g', 'F23_0_g', 'F24_0_g', 'F25_0_g', 'F26_0_g', 'FASATXR_g', 'F10_1CIS_g', 'F12_1CIS_g', 'F14_1CIS_g', 'F16_1CIS_g', 'F18_1CIS_g', 'F20_1CIS_g', 'F22_1CIS_g', 'F24_1CIS_g', 'FAMSCXR_g', 'F18_2CN6_g', 'F18_2CN9_g', 'F18_2CT_g', 'F18_2TC_g', 'F18_2R_g', 'F18_3CN3_g', 'F18_3CN6_g', 'F18_4CN3_g', 'F20_2CN6_g', 'F20_3CN9_g', 'F20_3CN6_g', 'F20_3CN3_g', 'F20_4CN6_g', 'F20_4CN3_g', 'F20_5CN3_g', 'F21_5CN3_g', 'F22_2CN6_g', 'F22_2CN3_g', 'F22_3CN3_g', 'F22_4CN6_g', 'F22_5CN6_g', 'F22_5CN3_g', 'F22_6CN3_g', 'F24_2CN6_g', 'FAPUXR_g', 'F10_1TRS_g', 'F12_1TRS_g', 'F14_1TRS_g', 'F16_1TRS_g', 'F18_1TRS_g', 'F18_2TTN6_g', 'F18_3TTTN3_g', 'F20_1TRS_g', 'F20_2TT_g', 'F22_1TRS_g', 'F24_1TRS_g', 'FAMSTXR_g', 'FAUN_g', 'CHORL_mg', 'NA_mg', 'K_mg', 'CA_mg', 'P_mg', 'MG_mg', 'FE_mg', 'HAEM_mg', 'NHAEM_mg', 'CU_mg', 'SE_mug', 'ZN_mg', 'ID_mug', 'ASH_g', 'VITA_RAE_mug', 'VITA_RE_mug', 'RETOL_mug', 'CARTBTOT_mug', 'CARTA_mug', 'LUTN_mug', 'ZEA_mug', 'CRYPXB_mug', 'LYCPN_mug', 'VITD_mug', 'CHOCALOH_mug', 'CHOCAL_mug', 'VITE_mg', 'TOCPHA_mg', 'TOCPHB_mg', 'TOCPHG_mg', 'TOCPHD_mg', 'VITK_mug', 'VITK1_mug', 'VITK2_mug', 'THIA_mg', 'RIBF_mg', 'VITB6_mg', 'VITB12_mug', 'NIA_mg', 'FOL_mug', 'FOLFD_mug', 'FOLAC_mug', 'VITC_mg']
