import re

txt = "RAM 2594/3483MB (lfb 2x2MB) SWAP 366/4096MB (cached 14MB) CPU [9%@306,9%@306,12%@306,8%@306] GR3D_FREQ 2% LCPU@36.5C CPU@33C Charger@115C Tdiode@40C PLL@32C GPU@32.5C thermal@39C AO@41.5C max170xx@38.9C PMIC@100C Tboard@39C"
x = re.search("CPU[ ].{0,50}[]][ ]", txt)
x = x.group()
print(x) 
