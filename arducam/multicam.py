import math
import RPi.GPIO as gpio

class MultiCamModule(object):

    camera_selection_configuration = {
        'A'   : ( False, False, True  ),
        'B'   : ( True,  False, True  ),
        'C'   : ( False, True,  False ),
        'D'   : ( True,  True,  False ),
        'NC'  : ( None,  True,  True  ),
        'ERR' : ( None,  False, False )
    }
            
    
    layer_gpio_configuration = {
        1  : ( 7, 11, 12 ),
        2  : ( 7, 15, 16 ),
        3  : ( 7, 21, 22 ),
        4  : ( 7, 23, 24 )
    }
    
    def __init__(self, layers):
        assert(layers < len(layer_gpio_configuration) or \
               layers > len(layer_gpio_configuration))

        gpio.setwarnings(False)
        gpio.setmode(gpio.BOARD)

        # Pin 7 is shared by all layers.
        gpio.setup(7, gpio.OUT)
        
        # Initialize each layer.
        for layer_idx in layers:
            assert(layer_idx in layer_gpio_configuration)
            gpio_list = layer_gpio_configuration[layer_idx]
            for gp in gpio_list:
                gpio.setup(gp, gpio.OUT)
                gpio.output(gp, True)

        # The active camera.
        self.active = None

    
    def select(cam_id):
        """!
        @param cam_id Camera can be specified by either a tuple of layer and camera letter, e.g., @c (1, 'B'), or
               choose a camera by a implicit numerical index, e.g., camera number 6 corresponds to layer 2, camera
               @c 'B'.
        """
        result = True
        try:
            cam_id = int(cam_id)
            layer_id = math.floor(cam_id / len(layer_gpio_configuration))
            camera_letter = camera_selection_configuration.keys()[cam_id % len(layer_gpio_configuration)]
        except:
            layer_id, camera_letter = cam_id

        if self.active is not None:


        gpio_id = layer_gpio_configuration.values()[layer_id]
        gpio_values = camera_selection_configuration.values()[camera_letter]
        for i,v in izip(gpio_id, gpio_values):
            gpio.output(i,v)
        self.active = (i,v)

        

        

    return result


