from configparser import ConfigParser

# Initaialize the library
config = ConfigParser()

# Create Section
config['COMPANIES1'] = {   
    # Name
    'Name' : 'International Business Machines Corporation',
    # Code name
    'Code': 'IBM'
}
config['COMPANIES2'] = {
    'Name' : 'Cisco Systems, Inc.',
    'Code': 'CSCO'
}
config['COMPANIES3'] = {
    'Name' : 'Intel Corporation',
    'Code': 'INTC'
}
config['COMPANIES4'] = {
    'Name' : 'Oracle Corporation',
    'Code': 'ORCL'
}
config['COMPANIES5'] = {
    'Name' : 'Walmart Inc.',
    'Code': 'WMT'
}
config['COMPANIES6'] = {
    'Name' : 'Johnson & Johnson',
    'Code': 'JNJ'
}
config['COMPANIES7'] = {
    'Name' : 'Accenture plc',
    'Code': 'ACN'
}

#open a config file and write in it
with open("config.ini", "w") as configfile:
    config.write(configfile)