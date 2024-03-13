import logging

          




def log_function(func_name, result):
    # Configure the logging settings
    log_filename = 'game.log'
    logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    success = False
    if result:
        success = True
    logging.info(func_name + ' ' + str(success))
   

