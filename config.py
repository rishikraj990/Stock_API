from configparser import ConfigParser

config = ConfigParser()

config['COMPANIES1'] = {
    'Name' : 'IBM',
    'Code': 'IBM'
}
config['COMPANIES2'] = {
    'Name' : 'CISCO',
    'Code': 'CSCO'
}
config['COMPANIES3'] = {
    'Name' : 'INTEL',
    'Code': 'INTC'
}
config['COMPANIES4'] = {
    'Name' : 'ORACLE',
    'Code': 'ORCL'
}
config['COMPANIES5'] = {
    'Name' : 'WALLMART',
    'Code': 'WMT'
}
config['COMPANIES6'] = {
    'Name' : 'JOHNSON & JOHNSON',
    'Code': 'JNJ'
}
config['COMPANIES7'] = {
    'Name' : 'ACCENTURE',
    'Code': 'ACN'
}

with open("config.ini", "w") as configfile:
    config.write(configfile)