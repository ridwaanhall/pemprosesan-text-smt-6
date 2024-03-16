# %%
month = "month january"
month[1]
# %%
import re
kata ='sedangberpuasadibulanramadhan'
re.findall(r'[aeiou]',kata)
# %%
len(re.findall(r'[aeiou]',kata))

# %%
# word = 'supercalifragilisticexpialidocious'
re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')

# %%
re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'loving')

# %%
re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')

# %%
padang = "enak banget"
padang.find("banget")
# %%
