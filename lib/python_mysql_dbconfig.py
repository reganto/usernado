from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):
    """ read database config 
    :param filename: config file name
    :param section: config section
    return: db dictionary config
    """

    parser = ConfigParser()
    
    # read config file
    parser.read(filename)

    config_dictionary = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            config_dictionary[item[0]] = item[1]
    return config_dictionary

