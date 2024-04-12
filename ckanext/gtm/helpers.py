import ckantoolkit as toolkit

config = toolkit.config

def gtm_id():
    return config.get('ckanext.gtm.gtm_id')
