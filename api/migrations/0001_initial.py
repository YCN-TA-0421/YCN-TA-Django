# Generated by Django 3.0.10 on 2021-06-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Productgroepcode', models.IntegerField()),
                ('Productgroep_oms', models.CharField(choices=[('Aardappelen en knolgewassen', 'Aardappelen en knolgewassen'), ('Alcoholische dranken', 'Alcoholische dranken'), ('Brood', 'Brood'), ('Diversen', 'Diversen'), ('Eieren', 'Eieren'), ('Flesvoeding en preparaten', 'Flesvoeding en preparaten'), ('Fruit', 'Fruit'), ('Gebak en koek', 'Gebak en koek'), ('Graanproducten en bindmiddelen', 'Graanproducten en bindmiddelen'), ('Groente', 'Groente'), ('Hartig broodbeleg', 'Hartig broodbeleg'), ('Hartige sauzen', 'Hartige sauzen'), ('Hartige snacks en zoutjes', 'Hartige snacks en zoutjes'), ('Kaas', 'Kaas'), ('Kruiden en specerijen', 'Kruiden en specerijen'), ('Melk en melkproducten', 'Melk en melkproducten'), ('Niet-alcoholische dranken', 'Niet-alcoholische dranken'), ('Noten en zaden', 'Noten en zaden'), ('Peulvruchten', 'Peulvruchten'), ('Samengestelde gerechten', 'Samengestelde gerechten'), ('Soepen', 'Soepen'), ('Suiker, snoep, zoet beleg en zoete sauzen', 'Suiker, snoep, zoet beleg en zoete sauzen'), ('Vetten en oliën', 'Vetten en oliën'), ('Vis', 'Vis'), ('Vlees en gevogelte', 'Vlees en gevogelte'), ('Vleesvervangers en zuivelvervangers', 'Vleesvervangers en zuivelvervangers'), ('Vleeswaren', 'Vleeswaren')], default='Diversen', help_text="Choose one of the following: [('Aardappelen en knolgewassen', 'Aardappelen en knolgewassen'), ('Alcoholische dranken', 'Alcoholische dranken'), ('Brood', 'Brood'), ('Diversen', 'Diversen'), ('Eieren', 'Eieren'), ('Flesvoeding en preparaten', 'Flesvoeding en preparaten'), ('Fruit', 'Fruit'), ('Gebak en koek', 'Gebak en koek'), ('Graanproducten en bindmiddelen', 'Graanproducten en bindmiddelen'), ('Groente', 'Groente'), ('Hartig broodbeleg', 'Hartig broodbeleg'), ('Hartige sauzen', 'Hartige sauzen'), ('Hartige snacks en zoutjes', 'Hartige snacks en zoutjes'), ('Kaas', 'Kaas'), ('Kruiden en specerijen', 'Kruiden en specerijen'), ('Melk en melkproducten', 'Melk en melkproducten'), ('Niet-alcoholische dranken', 'Niet-alcoholische dranken'), ('Noten en zaden', 'Noten en zaden'), ('Peulvruchten', 'Peulvruchten'), ('Samengestelde gerechten', 'Samengestelde gerechten'), ('Soepen', 'Soepen'), ('Suiker, snoep, zoet beleg en zoete sauzen', 'Suiker, snoep, zoet beleg en zoete sauzen'), ('Vetten en oliën', 'Vetten en oliën'), ('Vis', 'Vis'), ('Vlees en gevogelte', 'Vlees en gevogelte'), ('Vleesvervangers en zuivelvervangers', 'Vleesvervangers en zuivelvervangers'), ('Vleeswaren', 'Vleeswaren')]", max_length=100)),
                ('Productcode', models.IntegerField(default=-1, null=True)),
                ('Product_omschrijving', models.CharField(max_length=100)),
                ('Product_description', models.CharField(max_length=100, null=True)),
                ('Product_synoniemen', models.CharField(max_length=100, null=True)),
                ('Meeteenheid', models.CharField(default='g', max_length=10)),
                ('Hoeveelheid', models.IntegerField(default='100')),
                ('Commentaarregel', models.CharField(max_length=500, null=True)),
                ('Verrijkt_met', models.CharField(max_length=150, null=True)),
                ('Bevat_een_spoor_van', models.CharField(max_length=200, null=True)),
                ('ENERCJ_kJ', models.FloatField(null=True)),
                ('ENERCC_kcal', models.FloatField(null=True)),
                ('PROT_g', models.FloatField(null=True)),
                ('PROTPL_g', models.FloatField(null=True)),
                ('PROTAN_g', models.FloatField(null=True)),
                ('NT_g', models.FloatField(null=True)),
                ('CHO_g', models.FloatField(null=True)),
                ('SUGAR_g', models.FloatField(null=True)),
                ('STARCH_g', models.FloatField(null=True)),
                ('POLYL_g', models.FloatField(null=True)),
                ('FIBT_g', models.FloatField(null=True)),
                ('ALC_g', models.FloatField(null=True)),
                ('WATER_g', models.FloatField(null=True)),
                ('OA_g', models.FloatField(null=True)),
                ('FAT_g', models.FloatField(null=True)),
                ('FACID_g', models.FloatField(null=True)),
                ('FASAT_g', models.FloatField(null=True)),
                ('FAMSCIS_g', models.FloatField(null=True)),
                ('FAPU_g', models.FloatField(null=True)),
                ('FAPUN3_g', models.FloatField(null=True)),
                ('FAPUN6_g', models.FloatField(null=True)),
                ('FATRS_g', models.FloatField(null=True)),
                ('F4_0_g', models.FloatField(null=True)),
                ('F6_0_g', models.FloatField(null=True)),
                ('F8_0_g', models.FloatField(null=True)),
                ('F10_0_g', models.FloatField(null=True)),
                ('F11_0_g', models.FloatField(null=True)),
                ('F12_0_g', models.FloatField(null=True)),
                ('F13_0_g', models.FloatField(null=True)),
                ('F14_0_g', models.FloatField(null=True)),
                ('F15_0_g', models.FloatField(null=True)),
                ('F16_0_g', models.FloatField(null=True)),
                ('F17_0_g', models.FloatField(null=True)),
                ('F18_0_g', models.FloatField(null=True)),
                ('F19_0_g', models.FloatField(null=True)),
                ('F20_0_g', models.FloatField(null=True)),
                ('F21_0_g', models.FloatField(null=True)),
                ('F22_0_g', models.FloatField(null=True)),
                ('F23_0_g', models.FloatField(null=True)),
                ('F24_0_g', models.FloatField(null=True)),
                ('F25_0_g', models.FloatField(null=True)),
                ('F26_0_g', models.FloatField(null=True)),
                ('FASATXR_g', models.FloatField(null=True)),
                ('F10_1CIS_g', models.FloatField(null=True)),
                ('F12_1CIS_g', models.FloatField(null=True)),
                ('F14_1CIS_g', models.FloatField(null=True)),
                ('F16_1CIS_g', models.FloatField(null=True)),
                ('F18_1CIS_g', models.FloatField(null=True)),
                ('F20_1CIS_g', models.FloatField(null=True)),
                ('F22_1CIS_g', models.FloatField(null=True)),
                ('F24_1CIS_g', models.FloatField(null=True)),
                ('FAMSCXR_g', models.FloatField(null=True)),
                ('F18_2CN6_g', models.FloatField(null=True)),
                ('F18_2CN9_g', models.FloatField(null=True)),
                ('F18_2CT_g', models.FloatField(null=True)),
                ('F18_2TC_g', models.FloatField(null=True)),
                ('F18_2R_g', models.FloatField(null=True)),
                ('F18_3CN3_g', models.FloatField(null=True)),
                ('F18_3CN6_g', models.FloatField(null=True)),
                ('F18_4CN3_g', models.FloatField(null=True)),
                ('F20_2CN6_g', models.FloatField(null=True)),
                ('F20_3CN9_g', models.FloatField(null=True)),
                ('F20_3CN6_g', models.FloatField(null=True)),
                ('F20_3CN3_g', models.FloatField(null=True)),
                ('F20_4CN6_g', models.FloatField(null=True)),
                ('F20_4CN3_g', models.FloatField(null=True)),
                ('F20_5CN3_g', models.FloatField(null=True)),
                ('F21_5CN3_g', models.FloatField(null=True)),
                ('F22_2CN6_g', models.FloatField(null=True)),
                ('F22_2CN3_g', models.FloatField(null=True)),
                ('F22_3CN3_g', models.FloatField(null=True)),
                ('F22_4CN6_g', models.FloatField(null=True)),
                ('F22_5CN6_g', models.FloatField(null=True)),
                ('F22_5CN3_g', models.FloatField(null=True)),
                ('F22_6CN3_g', models.FloatField(null=True)),
                ('F24_2CN6_g', models.FloatField(null=True)),
                ('FAPUXR_g', models.FloatField(null=True)),
                ('F10_1TRS_g', models.FloatField(null=True)),
                ('F12_1TRS_g', models.FloatField(null=True)),
                ('F14_1TRS_g', models.FloatField(null=True)),
                ('F16_1TRS_g', models.FloatField(null=True)),
                ('F18_1TRS_g', models.FloatField(null=True)),
                ('F18_2TTN6_g', models.FloatField(null=True)),
                ('F18_3TTTN3_g', models.FloatField(null=True)),
                ('F20_1TRS_g', models.FloatField(null=True)),
                ('F20_2TT_g', models.FloatField(null=True)),
                ('F22_1TRS_g', models.FloatField(null=True)),
                ('F24_1TRS_g', models.FloatField(null=True)),
                ('FAMSTXR_g', models.FloatField(null=True)),
                ('FAUN_g', models.FloatField(null=True)),
                ('CHORL_mg', models.FloatField(null=True)),
                ('NA_mg', models.FloatField(null=True)),
                ('K_mg', models.FloatField(null=True)),
                ('CA_mg', models.FloatField(null=True)),
                ('P_mg', models.FloatField(null=True)),
                ('MG_mg', models.FloatField(null=True)),
                ('FE_mg', models.FloatField(null=True)),
                ('HAEM_mg', models.FloatField(null=True)),
                ('NHAEM_mg', models.FloatField(null=True)),
                ('CU_mg', models.FloatField(null=True)),
                ('SE_mug', models.FloatField(null=True)),
                ('ZN_mg', models.FloatField(null=True)),
                ('ID_mug', models.FloatField(null=True)),
                ('ASH_g', models.FloatField(null=True)),
                ('VITA_RAE_mug', models.FloatField(null=True)),
                ('VITA_RE_mug', models.FloatField(null=True)),
                ('RETOL_mug', models.FloatField(null=True)),
                ('CARTBTOT_mug', models.FloatField(null=True)),
                ('CARTA_mug', models.FloatField(null=True)),
                ('LUTN_mug', models.FloatField(null=True)),
                ('ZEA_mug', models.FloatField(null=True)),
                ('CRYPXB_mug', models.FloatField(null=True)),
                ('LYCPN_mug', models.FloatField(null=True)),
                ('VITD_mug', models.FloatField(null=True)),
                ('CHOCALOH_mug', models.FloatField(null=True)),
                ('CHOCAL_mug', models.FloatField(null=True)),
                ('VITE_mg', models.FloatField(null=True)),
                ('TOCPHA_mg', models.FloatField(null=True)),
                ('TOCPHB_mg', models.FloatField(null=True)),
                ('TOCPHG_mg', models.FloatField(null=True)),
                ('TOCPHD_mg', models.FloatField(null=True)),
                ('VITK_mug', models.FloatField(null=True)),
                ('VITK1_mug', models.FloatField(null=True)),
                ('VITK2_mug', models.FloatField(null=True)),
                ('THIA_mg', models.FloatField(null=True)),
                ('RIBF_mg', models.FloatField(null=True)),
                ('VITB6_mg', models.FloatField(null=True)),
                ('VITB12_mug', models.FloatField(null=True)),
                ('NIA_mg', models.FloatField(null=True)),
                ('FOL_mug', models.FloatField(null=True)),
                ('FOLFD_mug', models.FloatField(null=True)),
                ('FOLAC_mug', models.FloatField(null=True)),
                ('VITC_mg', models.FloatField(null=True)),
            ],
        ),
    ]
