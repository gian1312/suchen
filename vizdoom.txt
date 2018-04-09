# encoding: utf-8
# module vizdoom.vizdoom
# from /home/bjoern/anaconda3/lib/python3.6/site-packages/vizdoom/vizdoom.so
# by generator 1.145
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


# Variables with simple values

BINARY_BUTTON_COUNT = 38

BUTTON_COUNT = 43

DEFAULT_TICRATE = 35

DELTA_BUTTON_COUNT = 5

MAX_PLAYERS = 16

MAX_PLAYER_NAME_LENGTH = 16

SLOT_COUNT = 10

USER_VARIABLE_COUNT = 60

__version__ = '1.1.4'

# functions

def doom_fixed_to_double(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    doom_fixed_to_double(*args, **kwargs)
    Overloaded function.
    
    1. doom_fixed_to_double(arg0: int) -> float
    
    2. doom_fixed_to_double(arg0: float) -> float
    """
    pass

def doom_fixed_to_float(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    doom_fixed_to_float(*args, **kwargs)
    Overloaded function.
    
    1. doom_fixed_to_float(arg0: int) -> float
    
    2. doom_fixed_to_float(arg0: float) -> float
    """
    pass

def doom_tics_to_ms(arg0, arg1): # real signature unknown; restored from __doc__
    """ doom_tics_to_ms(arg0: float, arg1: int) -> float """
    return 0.0

def doom_tics_to_sec(arg0, arg1): # real signature unknown; restored from __doc__
    """ doom_tics_to_sec(arg0: float, arg1: int) -> float """
    return 0.0

def is_binary_button(arg0): # real signature unknown; restored from __doc__
    """ is_binary_button(arg0: vizdoom.vizdoom.Button) -> bool """
    return False

def is_delta_button(arg0): # real signature unknown; restored from __doc__
    """ is_delta_button(arg0: vizdoom.vizdoom.Button) -> bool """
    return False

def ms_to_doom_tics(arg0, arg1): # real signature unknown; restored from __doc__
    """ ms_to_doom_tics(arg0: float, arg1: int) -> float """
    return 0.0

def sec_to_doom_tics(arg0, arg1): # real signature unknown; restored from __doc__
    """ sec_to_doom_tics(arg0: float, arg1: int) -> float """
    return 0.0

# classes

class AutomapMode(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: vizdoom.vizdoom.AutomapMode, arg0: vizdoom.vizdoom.AutomapMode) -> bool
        
        2. __eq__(self: vizdoom.vizdoom.AutomapMode, arg0: int) -> bool
        """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: vizdoom.vizdoom.AutomapMode) -> tuple """
        return ()

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: vizdoom.vizdoom.AutomapMode) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: vizdoom.vizdoom.AutomapMode, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: vizdoom.vizdoom.AutomapMode) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: vizdoom.vizdoom.AutomapMode, arg0: vizdoom.vizdoom.AutomapMode) -> bool
        
        2. __ne__(self: vizdoom.vizdoom.AutomapMode, arg0: int) -> bool
        """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: vizdoom.vizdoom.AutomapMode) -> str """
        return ""

    def __setstate__(self, arg0): # real signature unknown; restored from __doc__
        """ __setstate__(self: vizdoom.vizdoom.AutomapMode, arg0: tuple) -> None """
        pass

    NORMAL = None # (!) forward: NORMAL, real value is ''
    OBJECTS = None # (!) forward: OBJECTS, real value is ''
    OBJECTS_WITH_SIZE = None # (!) forward: OBJECTS_WITH_SIZE, real value is ''
    WHOLE = None # (!) forward: WHOLE, real value is ''
    __members__ = {
        'NORMAL': '<failed to retrieve the value>',
        'OBJECTS': '<failed to retrieve the value>',
        'OBJECTS_WITH_SIZE': '<failed to retrieve the value>',
        'WHOLE': '<failed to retrieve the value>',
    }


class Button(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: vizdoom.vizdoom.Button, arg0: vizdoom.vizdoom.Button) -> bool
        
        2. __eq__(self: vizdoom.vizdoom.Button, arg0: int) -> bool
        """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: vizdoom.vizdoom.Button) -> tuple """
        return ()

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: vizdoom.vizdoom.Button) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: vizdoom.vizdoom.Button, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: vizdoom.vizdoom.Button) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: vizdoom.vizdoom.Button, arg0: vizdoom.vizdoom.Button) -> bool
        
        2. __ne__(self: vizdoom.vizdoom.Button, arg0: int) -> bool
        """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: vizdoom.vizdoom.Button) -> str """
        return ""

    def __setstate__(self, arg0): # real signature unknown; restored from __doc__
        """ __setstate__(self: vizdoom.vizdoom.Button, arg0: tuple) -> None """
        pass

    ACTIVATE_SELECTED_ITEM = None # (!) forward: ACTIVATE_SELECTED_ITEM, real value is ''
    ALTATTACK = None # (!) forward: ALTATTACK, real value is ''
    ATTACK = None # (!) forward: ATTACK, real value is ''
    CROUCH = None # (!) forward: CROUCH, real value is ''
    DROP_SELECTED_ITEM = None # (!) forward: DROP_SELECTED_ITEM, real value is ''
    DROP_SELECTED_WEAPON = None # (!) forward: DROP_SELECTED_WEAPON, real value is ''
    JUMP = None # (!) forward: JUMP, real value is ''
    LAND = None # (!) forward: LAND, real value is ''
    LOOK_DOWN = None # (!) forward: LOOK_DOWN, real value is ''
    LOOK_UP = None # (!) forward: LOOK_UP, real value is ''
    LOOK_UP_DOWN_DELTA = None # (!) forward: LOOK_UP_DOWN_DELTA, real value is ''
    MOVE_BACKWARD = None # (!) forward: MOVE_BACKWARD, real value is ''
    MOVE_DOWN = None # (!) forward: MOVE_DOWN, real value is ''
    MOVE_FORWARD = None # (!) forward: MOVE_FORWARD, real value is ''
    MOVE_FORWARD_BACKWARD_DELTA = None # (!) forward: MOVE_FORWARD_BACKWARD_DELTA, real value is ''
    MOVE_LEFT = None # (!) forward: MOVE_LEFT, real value is ''
    MOVE_LEFT_RIGHT_DELTA = None # (!) forward: MOVE_LEFT_RIGHT_DELTA, real value is ''
    MOVE_RIGHT = None # (!) forward: MOVE_RIGHT, real value is ''
    MOVE_UP = None # (!) forward: MOVE_UP, real value is ''
    MOVE_UP_DOWN_DELTA = None # (!) forward: MOVE_UP_DOWN_DELTA, real value is ''
    RELOAD = None # (!) forward: RELOAD, real value is ''
    SELECT_NEXT_ITEM = None # (!) forward: SELECT_NEXT_ITEM, real value is ''
    SELECT_NEXT_WEAPON = None # (!) forward: SELECT_NEXT_WEAPON, real value is ''
    SELECT_PREV_ITEM = None # (!) forward: SELECT_PREV_ITEM, real value is ''
    SELECT_PREV_WEAPON = None # (!) forward: SELECT_PREV_WEAPON, real value is ''
    SELECT_WEAPON0 = None # (!) forward: SELECT_WEAPON0, real value is ''
    SELECT_WEAPON1 = None # (!) forward: SELECT_WEAPON1, real value is ''
    SELECT_WEAPON2 = None # (!) forward: SELECT_WEAPON2, real value is ''
    SELECT_WEAPON3 = None # (!) forward: SELECT_WEAPON3, real value is ''
    SELECT_WEAPON4 = None # (!) forward: SELECT_WEAPON4, real value is ''
    SELECT_WEAPON5 = None # (!) forward: SELECT_WEAPON5, real value is ''
    SELECT_WEAPON6 = None # (!) forward: SELECT_WEAPON6, real value is ''
    SELECT_WEAPON7 = None # (!) forward: SELECT_WEAPON7, real value is ''
    SELECT_WEAPON8 = None # (!) forward: SELECT_WEAPON8, real value is ''
    SELECT_WEAPON9 = None # (!) forward: SELECT_WEAPON9, real value is ''
    SPEED = None # (!) forward: SPEED, real value is ''
    STRAFE = None # (!) forward: STRAFE, real value is ''
    TURN180 = None # (!) forward: TURN180, real value is ''
    TURN_LEFT = None # (!) forward: TURN_LEFT, real value is ''
    TURN_LEFT_RIGHT_DELTA = None # (!) forward: TURN_LEFT_RIGHT_DELTA, real value is ''
    TURN_RIGHT = None # (!) forward: TURN_RIGHT, real value is ''
    USE = None # (!) forward: USE, real value is ''
    ZOOM = None # (!) forward: ZOOM, real value is ''
    __members__ = {
        'ACTIVATE_SELECTED_ITEM': '<failed to retrieve the value>',
        'ALTATTACK': '<failed to retrieve the value>',
        'ATTACK': '<failed to retrieve the value>',
        'CROUCH': '<failed to retrieve the value>',
        'DROP_SELECTED_ITEM': '<failed to retrieve the value>',
        'DROP_SELECTED_WEAPON': '<failed to retrieve the value>',
        'JUMP': '<failed to retrieve the value>',
        'LAND': '<failed to retrieve the value>',
        'LOOK_DOWN': '<failed to retrieve the value>',
        'LOOK_UP': '<failed to retrieve the value>',
        'LOOK_UP_DOWN_DELTA': '<failed to retrieve the value>',
        'MOVE_BACKWARD': '<failed to retrieve the value>',
        'MOVE_DOWN': '<failed to retrieve the value>',
        'MOVE_FORWARD': '<failed to retrieve the value>',
        'MOVE_FORWARD_BACKWARD_DELTA': '<failed to retrieve the value>',
        'MOVE_LEFT': '<failed to retrieve the value>',
        'MOVE_LEFT_RIGHT_DELTA': '<failed to retrieve the value>',
        'MOVE_RIGHT': '<failed to retrieve the value>',
        'MOVE_UP': '<failed to retrieve the value>',
        'MOVE_UP_DOWN_DELTA': '<failed to retrieve the value>',
        'RELOAD': '<failed to retrieve the value>',
        'SELECT_NEXT_ITEM': '<failed to retrieve the value>',
        'SELECT_NEXT_WEAPON': '<failed to retrieve the value>',
        'SELECT_PREV_ITEM': '<failed to retrieve the value>',
        'SELECT_PREV_WEAPON': '<failed to retrieve the value>',
        'SELECT_WEAPON0': '<failed to retrieve the value>',
        'SELECT_WEAPON1': '<failed to retrieve the value>',
        'SELECT_WEAPON2': '<failed to retrieve the value>',
        'SELECT_WEAPON3': '<failed to retrieve the value>',
        'SELECT_WEAPON4': '<failed to retrieve the value>',
        'SELECT_WEAPON5': '<failed to retrieve the value>',
        'SELECT_WEAPON6': '<failed to retrieve the value>',
        'SELECT_WEAPON7': '<failed to retrieve the value>',
        'SELECT_WEAPON8': '<failed to retrieve the value>',
        'SELECT_WEAPON9': '<failed to retrieve the value>',
        'SPEED': '<failed to retrieve the value>',
        'STRAFE': '<failed to retrieve the value>',
        'TURN180': '<failed to retrieve the value>',
        'TURN_LEFT': '<failed to retrieve the value>',
        'TURN_LEFT_RIGHT_DELTA': '<failed to retrieve the value>',
        'TURN_RIGHT': '<failed to retrieve the value>',
        'USE': '<failed to retrieve the value>',
        'ZOOM': '<failed to retrieve the value>',
    }


class DoomGame(__pybind11_builtins.pybind11_object):
    # no doc
    def add_available_button(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        add_available_button(*args, **kwargs)
        Overloaded function.
        
        1. add_available_button(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.Button) -> None
        
        2. add_available_button(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.Button, arg1: float) -> None
        """
        pass

    def add_available_game_variable(self, arg0): # real signature unknown; restored from __doc__
        """ add_available_game_variable(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.GameVariable) -> None """
        pass

    def add_game_args(self, arg0): # real signature unknown; restored from __doc__
        """ add_game_args(self: vizdoom.vizdoom.DoomGame, arg0: str) -> None """
        pass

    def advance_action(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        advance_action(*args, **kwargs)
        Overloaded function.
        
        1. advance_action(self: vizdoom.vizdoom.DoomGame) -> None
        
        2. advance_action(self: vizdoom.vizdoom.DoomGame, arg0: int) -> None
        
        3. advance_action(self: vizdoom.vizdoom.DoomGame, arg0: int, arg1: bool) -> None
        """
        pass

    def clear_available_buttons(self): # real signature unknown; restored from __doc__
        """ clear_available_buttons(self: vizdoom.vizdoom.DoomGame) -> None """
        pass

    def clear_available_game_variables(self): # real signature unknown; restored from __doc__
        """ clear_available_game_variables(self: vizdoom.vizdoom.DoomGame) -> None """
        pass

    def clear_game_args(self): # real signature unknown; restored from __doc__
        """ clear_game_args(self: vizdoom.vizdoom.DoomGame) -> None """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self: vizdoom.vizdoom.DoomGame) -> None """
        pass

    def get_available_buttons(self): # real signature unknown; restored from __doc__
        """ get_available_buttons(self: vizdoom.vizdoom.DoomGame) -> list """
        return []

    def get_available_buttons_size(self): # real signature unknown; restored from __doc__
        """ get_available_buttons_size(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_available_game_variables(self): # real signature unknown; restored from __doc__
        """ get_available_game_variables(self: vizdoom.vizdoom.DoomGame) -> list """
        return []

    def get_available_game_variables_size(self): # real signature unknown; restored from __doc__
        """ get_available_game_variables_size(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_button_max_value(self, arg0): # real signature unknown; restored from __doc__
        """ get_button_max_value(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.Button) -> float """
        return 0.0

    def get_death_penalty(self): # real signature unknown; restored from __doc__
        """ get_death_penalty(self: vizdoom.vizdoom.DoomGame) -> float """
        return 0.0

    def get_episode_start_time(self): # real signature unknown; restored from __doc__
        """ get_episode_start_time(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_episode_time(self): # real signature unknown; restored from __doc__
        """ get_episode_time(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_episode_timeout(self): # real signature unknown; restored from __doc__
        """ get_episode_timeout(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_game_variable(self, arg0): # real signature unknown; restored from __doc__
        """ get_game_variable(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.GameVariable) -> float """
        return 0.0

    def get_last_action(self): # real signature unknown; restored from __doc__
        """ get_last_action(self: vizdoom.vizdoom.DoomGame) -> list """
        return []

    def get_last_reward(self): # real signature unknown; restored from __doc__
        """ get_last_reward(self: vizdoom.vizdoom.DoomGame) -> float """
        return 0.0

    def get_living_reward(self): # real signature unknown; restored from __doc__
        """ get_living_reward(self: vizdoom.vizdoom.DoomGame) -> float """
        return 0.0

    def get_mode(self): # real signature unknown; restored from __doc__
        """ get_mode(self: vizdoom.vizdoom.DoomGame) -> vizdoom.vizdoom.Mode """
        pass

    def get_screen_channels(self): # real signature unknown; restored from __doc__
        """ get_screen_channels(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_screen_format(self): # real signature unknown; restored from __doc__
        """ get_screen_format(self: vizdoom.vizdoom.DoomGame) -> vizdoom.vizdoom.ScreenFormat """
        pass

    def get_screen_height(self): # real signature unknown; restored from __doc__
        """ get_screen_height(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_screen_pitch(self): # real signature unknown; restored from __doc__
        """ get_screen_pitch(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_screen_size(self): # real signature unknown; restored from __doc__
        """ get_screen_size(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_screen_width(self): # real signature unknown; restored from __doc__
        """ get_screen_width(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_seed(self): # real signature unknown; restored from __doc__
        """ get_seed(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self: vizdoom.vizdoom.DoomGame) -> vizdoom.vizdoom.GameState """
        pass

    def get_ticrate(self): # real signature unknown; restored from __doc__
        """ get_ticrate(self: vizdoom.vizdoom.DoomGame) -> int """
        return 0

    def get_total_reward(self): # real signature unknown; restored from __doc__
        """ get_total_reward(self: vizdoom.vizdoom.DoomGame) -> float """
        return 0.0

    def init(self): # real signature unknown; restored from __doc__
        """ init(self: vizdoom.vizdoom.DoomGame) -> None """
        pass

    def is_automap_buffer_enabled(self): # real signature unknown; restored from __doc__
        """ is_automap_buffer_enabled(self: vizdoom.vizdoom.DoomGame) -> bool """
        return False

    def is_depth_buffer_enabled(self): # real signature unknown; restored from __doc__
        """ is_depth_buffer_enabled(self: vizdoom.vizdoom.DoomGame) -> bool """
        return False

    def is_episode_finished(self): # real signature unknown; restored from __doc__
        """ is_episode_finished(self: vizdoom.vizdoom.DoomGame) -> bool """
        return False

    def is_labels_buffer_enabled(self): # real signature unknown; restored from __doc__
        """ is_labels_buffer_enabled(self: vizdoom.vizdoom.DoomGame) -> bool """
        return False

    def is_multiplayer_game(self): # real signature unknown; restored from __doc__
        """ is_multiplayer_game(self: vizdoom.vizdoom.DoomGame) -> bool """
        return False

    def is_new_episode(self): # real signature unknown; restored from __doc__
        """ is_new_episode(self: vizdoom.vizdoom.DoomGame) -> bool """
        return False

    def is_player_dead(self): # real signature unknown; restored from __doc__
        """ is_player_dead(self: vizdoom.vizdoom.DoomGame) -> bool """
        return False

    def is_running(self): # real signature unknown; restored from __doc__
        """ is_running(self: vizdoom.vizdoom.DoomGame) -> bool """
        return False

    def load_config(self, arg0): # real signature unknown; restored from __doc__
        """ load_config(self: vizdoom.vizdoom.DoomGame, arg0: str) -> bool """
        return False

    def make_action(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        make_action(*args, **kwargs)
        Overloaded function.
        
        1. make_action(self: vizdoom.vizdoom.DoomGame, arg0: list) -> float
        
        2. make_action(self: vizdoom.vizdoom.DoomGame, arg0: list, arg1: int) -> float
        """
        pass

    def new_episode(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        new_episode(*args, **kwargs)
        Overloaded function.
        
        1. new_episode(self: vizdoom.vizdoom.DoomGame) -> None
        
        2. new_episode(self: vizdoom.vizdoom.DoomGame, arg0: str) -> None
        """
        pass

    def replay_episode(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        replay_episode(*args, **kwargs)
        Overloaded function.
        
        1. replay_episode(self: vizdoom.vizdoom.DoomGame, arg0: str) -> None
        
        2. replay_episode(self: vizdoom.vizdoom.DoomGame, arg0: str, arg1: int) -> None
        """
        pass

    def respawn_player(self): # real signature unknown; restored from __doc__
        """ respawn_player(self: vizdoom.vizdoom.DoomGame) -> None """
        pass

    def send_game_command(self, arg0): # real signature unknown; restored from __doc__
        """ send_game_command(self: vizdoom.vizdoom.DoomGame, arg0: str) -> None """
        pass

    def set_action(self, arg0): # real signature unknown; restored from __doc__
        """ set_action(self: vizdoom.vizdoom.DoomGame, arg0: list) -> None """
        pass

    def set_automap_buffer_enabled(self, arg0): # real signature unknown; restored from __doc__
        """ set_automap_buffer_enabled(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_automap_mode(self, arg0): # real signature unknown; restored from __doc__
        """ set_automap_mode(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.AutomapMode) -> None """
        pass

    def set_automap_render_textures(self, arg0): # real signature unknown; restored from __doc__
        """ set_automap_render_textures(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_automap_rotate(self, arg0): # real signature unknown; restored from __doc__
        """ set_automap_rotate(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_available_buttons(self, arg0): # real signature unknown; restored from __doc__
        """ set_available_buttons(self: vizdoom.vizdoom.DoomGame, arg0: list) -> None """
        pass

    def set_available_game_variables(self, arg0): # real signature unknown; restored from __doc__
        """ set_available_game_variables(self: vizdoom.vizdoom.DoomGame, arg0: list) -> None """
        pass

    def set_button_max_value(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ set_button_max_value(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.Button, arg1: float) -> None """
        pass

    def set_console_enabled(self, arg0): # real signature unknown; restored from __doc__
        """ set_console_enabled(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_death_penalty(self, arg0): # real signature unknown; restored from __doc__
        """ set_death_penalty(self: vizdoom.vizdoom.DoomGame, arg0: float) -> None """
        pass

    def set_depth_buffer_enabled(self, arg0): # real signature unknown; restored from __doc__
        """ set_depth_buffer_enabled(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_doom_config_path(self, arg0): # real signature unknown; restored from __doc__
        """ set_doom_config_path(self: vizdoom.vizdoom.DoomGame, arg0: str) -> None """
        pass

    def set_doom_game_path(self, arg0): # real signature unknown; restored from __doc__
        """ set_doom_game_path(self: vizdoom.vizdoom.DoomGame, arg0: str) -> None """
        pass

    def set_doom_map(self, arg0): # real signature unknown; restored from __doc__
        """ set_doom_map(self: vizdoom.vizdoom.DoomGame, arg0: str) -> None """
        pass

    def set_doom_scenario_path(self, arg0): # real signature unknown; restored from __doc__
        """ set_doom_scenario_path(self: vizdoom.vizdoom.DoomGame, arg0: str) -> None """
        pass

    def set_doom_skill(self, arg0): # real signature unknown; restored from __doc__
        """ set_doom_skill(self: vizdoom.vizdoom.DoomGame, arg0: int) -> None """
        pass

    def set_episode_start_time(self, arg0): # real signature unknown; restored from __doc__
        """ set_episode_start_time(self: vizdoom.vizdoom.DoomGame, arg0: int) -> None """
        pass

    def set_episode_timeout(self, arg0): # real signature unknown; restored from __doc__
        """ set_episode_timeout(self: vizdoom.vizdoom.DoomGame, arg0: int) -> None """
        pass

    def set_labels_buffer_enabled(self, arg0): # real signature unknown; restored from __doc__
        """ set_labels_buffer_enabled(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_living_reward(self, arg0): # real signature unknown; restored from __doc__
        """ set_living_reward(self: vizdoom.vizdoom.DoomGame, arg0: float) -> None """
        pass

    def set_mode(self, arg0): # real signature unknown; restored from __doc__
        """ set_mode(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.Mode) -> None """
        pass

    def set_render_all_frames(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_all_frames(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_corpses(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_corpses(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_crosshair(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_crosshair(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_decals(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_decals(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_effects_sprites(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_effects_sprites(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_hud(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_hud(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_messages(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_messages(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_minimal_hud(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_minimal_hud(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_particles(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_particles(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_screen_flashes(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_screen_flashes(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_render_weapon(self, arg0): # real signature unknown; restored from __doc__
        """ set_render_weapon(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_screen_format(self, arg0): # real signature unknown; restored from __doc__
        """ set_screen_format(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.ScreenFormat) -> None """
        pass

    def set_screen_resolution(self, arg0): # real signature unknown; restored from __doc__
        """ set_screen_resolution(self: vizdoom.vizdoom.DoomGame, arg0: vizdoom.vizdoom.ScreenResolution) -> None """
        pass

    def set_seed(self, arg0): # real signature unknown; restored from __doc__
        """ set_seed(self: vizdoom.vizdoom.DoomGame, arg0: int) -> None """
        pass

    def set_sound_enabled(self, arg0): # real signature unknown; restored from __doc__
        """ set_sound_enabled(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def set_ticrate(self, arg0): # real signature unknown; restored from __doc__
        """ set_ticrate(self: vizdoom.vizdoom.DoomGame, arg0: int) -> None """
        pass

    def set_vizdoom_path(self, arg0): # real signature unknown; restored from __doc__
        """ set_vizdoom_path(self: vizdoom.vizdoom.DoomGame, arg0: str) -> None """
        pass

    def set_window_visible(self, arg0): # real signature unknown; restored from __doc__
        """ set_window_visible(self: vizdoom.vizdoom.DoomGame, arg0: bool) -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: vizdoom.vizdoom.DoomGame) -> None """
        pass


class FileDoesNotExistException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class GameState(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    automap_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    depth_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    game_variables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    labels_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    screen_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class GameVariable(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: vizdoom.vizdoom.GameVariable, arg0: vizdoom.vizdoom.GameVariable) -> bool
        
        2. __eq__(self: vizdoom.vizdoom.GameVariable, arg0: int) -> bool
        """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: vizdoom.vizdoom.GameVariable) -> tuple """
        return ()

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: vizdoom.vizdoom.GameVariable) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: vizdoom.vizdoom.GameVariable, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: vizdoom.vizdoom.GameVariable) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: vizdoom.vizdoom.GameVariable, arg0: vizdoom.vizdoom.GameVariable) -> bool
        
        2. __ne__(self: vizdoom.vizdoom.GameVariable, arg0: int) -> bool
        """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: vizdoom.vizdoom.GameVariable) -> str """
        return ""

    def __setstate__(self, arg0): # real signature unknown; restored from __doc__
        """ __setstate__(self: vizdoom.vizdoom.GameVariable, arg0: tuple) -> None """
        pass

    ALTATTACK_READY = None # (!) forward: ALTATTACK_READY, real value is ''
    AMMO0 = None # (!) forward: AMMO0, real value is ''
    AMMO1 = None # (!) forward: AMMO1, real value is ''
    AMMO2 = None # (!) forward: AMMO2, real value is ''
    AMMO3 = None # (!) forward: AMMO3, real value is ''
    AMMO4 = None # (!) forward: AMMO4, real value is ''
    AMMO5 = None # (!) forward: AMMO5, real value is ''
    AMMO6 = None # (!) forward: AMMO6, real value is ''
    AMMO7 = None # (!) forward: AMMO7, real value is ''
    AMMO8 = None # (!) forward: AMMO8, real value is ''
    AMMO9 = None # (!) forward: AMMO9, real value is ''
    ANGLE = None # (!) forward: ANGLE, real value is ''
    ARMOR = None # (!) forward: ARMOR, real value is ''
    ATTACK_READY = None # (!) forward: ATTACK_READY, real value is ''
    DEAD = None # (!) forward: DEAD, real value is ''
    DEATHCOUNT = None # (!) forward: DEATHCOUNT, real value is ''
    FRAGCOUNT = None # (!) forward: FRAGCOUNT, real value is ''
    HEALTH = None # (!) forward: HEALTH, real value is ''
    ITEMCOUNT = None # (!) forward: ITEMCOUNT, real value is ''
    KILLCOUNT = None # (!) forward: KILLCOUNT, real value is ''
    ON_GROUND = None # (!) forward: ON_GROUND, real value is ''
    PITCH = None # (!) forward: PITCH, real value is ''
    PLAYER10_FRAGCOUNT = None # (!) forward: PLAYER10_FRAGCOUNT, real value is ''
    PLAYER11_FRAGCOUNT = None # (!) forward: PLAYER11_FRAGCOUNT, real value is ''
    PLAYER12_FRAGCOUNT = None # (!) forward: PLAYER12_FRAGCOUNT, real value is ''
    PLAYER13_FRAGCOUNT = None # (!) forward: PLAYER13_FRAGCOUNT, real value is ''
    PLAYER14_FRAGCOUNT = None # (!) forward: PLAYER14_FRAGCOUNT, real value is ''
    PLAYER15_FRAGCOUNT = None # (!) forward: PLAYER15_FRAGCOUNT, real value is ''
    PLAYER16_FRAGCOUNT = None # (!) forward: PLAYER16_FRAGCOUNT, real value is ''
    PLAYER1_FRAGCOUNT = None # (!) forward: PLAYER1_FRAGCOUNT, real value is ''
    PLAYER2_FRAGCOUNT = None # (!) forward: PLAYER2_FRAGCOUNT, real value is ''
    PLAYER3_FRAGCOUNT = None # (!) forward: PLAYER3_FRAGCOUNT, real value is ''
    PLAYER4_FRAGCOUNT = None # (!) forward: PLAYER4_FRAGCOUNT, real value is ''
    PLAYER5_FRAGCOUNT = None # (!) forward: PLAYER5_FRAGCOUNT, real value is ''
    PLAYER6_FRAGCOUNT = None # (!) forward: PLAYER6_FRAGCOUNT, real value is ''
    PLAYER7_FRAGCOUNT = None # (!) forward: PLAYER7_FRAGCOUNT, real value is ''
    PLAYER8_FRAGCOUNT = None # (!) forward: PLAYER8_FRAGCOUNT, real value is ''
    PLAYER9_FRAGCOUNT = None # (!) forward: PLAYER9_FRAGCOUNT, real value is ''
    PLAYER_COUNT = None # (!) forward: PLAYER_COUNT, real value is ''
    PLAYER_NUMBER = None # (!) forward: PLAYER_NUMBER, real value is ''
    POSITION_X = None # (!) forward: POSITION_X, real value is ''
    POSITION_Y = None # (!) forward: POSITION_Y, real value is ''
    POSITION_Z = None # (!) forward: POSITION_Z, real value is ''
    ROLL = None # (!) forward: ROLL, real value is ''
    SECRETCOUNT = None # (!) forward: SECRETCOUNT, real value is ''
    SELECTED_WEAPON = None # (!) forward: SELECTED_WEAPON, real value is ''
    SELECTED_WEAPON_AMMO = None # (!) forward: SELECTED_WEAPON_AMMO, real value is ''
    USER1 = None # (!) forward: USER1, real value is ''
    USER10 = None # (!) forward: USER10, real value is ''
    USER11 = None # (!) forward: USER11, real value is ''
    USER12 = None # (!) forward: USER12, real value is ''
    USER13 = None # (!) forward: USER13, real value is ''
    USER14 = None # (!) forward: USER14, real value is ''
    USER15 = None # (!) forward: USER15, real value is ''
    USER16 = None # (!) forward: USER16, real value is ''
    USER17 = None # (!) forward: USER17, real value is ''
    USER18 = None # (!) forward: USER18, real value is ''
    USER19 = None # (!) forward: USER19, real value is ''
    USER2 = None # (!) forward: USER2, real value is ''
    USER20 = None # (!) forward: USER20, real value is ''
    USER21 = None # (!) forward: USER21, real value is ''
    USER22 = None # (!) forward: USER22, real value is ''
    USER23 = None # (!) forward: USER23, real value is ''
    USER24 = None # (!) forward: USER24, real value is ''
    USER25 = None # (!) forward: USER25, real value is ''
    USER26 = None # (!) forward: USER26, real value is ''
    USER27 = None # (!) forward: USER27, real value is ''
    USER28 = None # (!) forward: USER28, real value is ''
    USER29 = None # (!) forward: USER29, real value is ''
    USER3 = None # (!) forward: USER3, real value is ''
    USER30 = None # (!) forward: USER30, real value is ''
    USER31 = None # (!) forward: USER31, real value is ''
    USER32 = None # (!) forward: USER32, real value is ''
    USER33 = None # (!) forward: USER33, real value is ''
    USER34 = None # (!) forward: USER34, real value is ''
    USER35 = None # (!) forward: USER35, real value is ''
    USER36 = None # (!) forward: USER36, real value is ''
    USER37 = None # (!) forward: USER37, real value is ''
    USER38 = None # (!) forward: USER38, real value is ''
    USER39 = None # (!) forward: USER39, real value is ''
    USER4 = None # (!) forward: USER4, real value is ''
    USER40 = None # (!) forward: USER40, real value is ''
    USER41 = None # (!) forward: USER41, real value is ''
    USER42 = None # (!) forward: USER42, real value is ''
    USER43 = None # (!) forward: USER43, real value is ''
    USER44 = None # (!) forward: USER44, real value is ''
    USER45 = None # (!) forward: USER45, real value is ''
    USER46 = None # (!) forward: USER46, real value is ''
    USER47 = None # (!) forward: USER47, real value is ''
    USER48 = None # (!) forward: USER48, real value is ''
    USER49 = None # (!) forward: USER49, real value is ''
    USER5 = None # (!) forward: USER5, real value is ''
    USER50 = None # (!) forward: USER50, real value is ''
    USER51 = None # (!) forward: USER51, real value is ''
    USER52 = None # (!) forward: USER52, real value is ''
    USER53 = None # (!) forward: USER53, real value is ''
    USER54 = None # (!) forward: USER54, real value is ''
    USER55 = None # (!) forward: USER55, real value is ''
    USER56 = None # (!) forward: USER56, real value is ''
    USER57 = None # (!) forward: USER57, real value is ''
    USER58 = None # (!) forward: USER58, real value is ''
    USER59 = None # (!) forward: USER59, real value is ''
    USER6 = None # (!) forward: USER6, real value is ''
    USER60 = None # (!) forward: USER60, real value is ''
    USER7 = None # (!) forward: USER7, real value is ''
    USER8 = None # (!) forward: USER8, real value is ''
    USER9 = None # (!) forward: USER9, real value is ''
    VELOCITY_X = None # (!) forward: VELOCITY_X, real value is ''
    VELOCITY_Y = None # (!) forward: VELOCITY_Y, real value is ''
    VELOCITY_Z = None # (!) forward: VELOCITY_Z, real value is ''
    WEAPON0 = None # (!) forward: WEAPON0, real value is ''
    WEAPON1 = None # (!) forward: WEAPON1, real value is ''
    WEAPON2 = None # (!) forward: WEAPON2, real value is ''
    WEAPON3 = None # (!) forward: WEAPON3, real value is ''
    WEAPON4 = None # (!) forward: WEAPON4, real value is ''
    WEAPON5 = None # (!) forward: WEAPON5, real value is ''
    WEAPON6 = None # (!) forward: WEAPON6, real value is ''
    WEAPON7 = None # (!) forward: WEAPON7, real value is ''
    WEAPON8 = None # (!) forward: WEAPON8, real value is ''
    WEAPON9 = None # (!) forward: WEAPON9, real value is ''
    __members__ = {
        'ALTATTACK_READY': '<failed to retrieve the value>',
        'AMMO0': '<failed to retrieve the value>',
        'AMMO1': '<failed to retrieve the value>',
        'AMMO2': '<failed to retrieve the value>',
        'AMMO3': '<failed to retrieve the value>',
        'AMMO4': '<failed to retrieve the value>',
        'AMMO5': '<failed to retrieve the value>',
        'AMMO6': '<failed to retrieve the value>',
        'AMMO7': '<failed to retrieve the value>',
        'AMMO8': '<failed to retrieve the value>',
        'AMMO9': '<failed to retrieve the value>',
        'ANGLE': '<failed to retrieve the value>',
        'ARMOR': '<failed to retrieve the value>',
        'ATTACK_READY': '<failed to retrieve the value>',
        'DEAD': '<failed to retrieve the value>',
        'DEATHCOUNT': '<failed to retrieve the value>',
        'FRAGCOUNT': '<failed to retrieve the value>',
        'HEALTH': '<failed to retrieve the value>',
        'ITEMCOUNT': '<failed to retrieve the value>',
        'KILLCOUNT': '<failed to retrieve the value>',
        'ON_GROUND': '<failed to retrieve the value>',
        'PITCH': '<failed to retrieve the value>',
        'PLAYER10_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER11_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER12_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER13_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER14_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER15_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER16_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER1_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER2_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER3_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER4_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER5_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER6_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER7_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER8_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER9_FRAGCOUNT': '<failed to retrieve the value>',
        'PLAYER_COUNT': '<failed to retrieve the value>',
        'PLAYER_NUMBER': '<failed to retrieve the value>',
        'POSITION_X': '<failed to retrieve the value>',
        'POSITION_Y': '<failed to retrieve the value>',
        'POSITION_Z': '<failed to retrieve the value>',
        'ROLL': '<failed to retrieve the value>',
        'SECRETCOUNT': '<failed to retrieve the value>',
        'SELECTED_WEAPON': '<failed to retrieve the value>',
        'SELECTED_WEAPON_AMMO': '<failed to retrieve the value>',
        'USER1': '<failed to retrieve the value>',
        'USER10': '<failed to retrieve the value>',
        'USER11': '<failed to retrieve the value>',
        'USER12': '<failed to retrieve the value>',
        'USER13': '<failed to retrieve the value>',
        'USER14': '<failed to retrieve the value>',
        'USER15': '<failed to retrieve the value>',
        'USER16': '<failed to retrieve the value>',
        'USER17': '<failed to retrieve the value>',
        'USER18': '<failed to retrieve the value>',
        'USER19': '<failed to retrieve the value>',
        'USER2': '<failed to retrieve the value>',
        'USER20': '<failed to retrieve the value>',
        'USER21': '<failed to retrieve the value>',
        'USER22': '<failed to retrieve the value>',
        'USER23': '<failed to retrieve the value>',
        'USER24': '<failed to retrieve the value>',
        'USER25': '<failed to retrieve the value>',
        'USER26': '<failed to retrieve the value>',
        'USER27': '<failed to retrieve the value>',
        'USER28': '<failed to retrieve the value>',
        'USER29': '<failed to retrieve the value>',
        'USER3': '<failed to retrieve the value>',
        'USER30': '<failed to retrieve the value>',
        'USER31': '<failed to retrieve the value>',
        'USER32': '<failed to retrieve the value>',
        'USER33': '<failed to retrieve the value>',
        'USER34': '<failed to retrieve the value>',
        'USER35': '<failed to retrieve the value>',
        'USER36': '<failed to retrieve the value>',
        'USER37': '<failed to retrieve the value>',
        'USER38': '<failed to retrieve the value>',
        'USER39': '<failed to retrieve the value>',
        'USER4': '<failed to retrieve the value>',
        'USER40': '<failed to retrieve the value>',
        'USER41': '<failed to retrieve the value>',
        'USER42': '<failed to retrieve the value>',
        'USER43': '<failed to retrieve the value>',
        'USER44': '<failed to retrieve the value>',
        'USER45': '<failed to retrieve the value>',
        'USER46': '<failed to retrieve the value>',
        'USER47': '<failed to retrieve the value>',
        'USER48': '<failed to retrieve the value>',
        'USER49': '<failed to retrieve the value>',
        'USER5': '<failed to retrieve the value>',
        'USER50': '<failed to retrieve the value>',
        'USER51': '<failed to retrieve the value>',
        'USER52': '<failed to retrieve the value>',
        'USER53': '<failed to retrieve the value>',
        'USER54': '<failed to retrieve the value>',
        'USER55': '<failed to retrieve the value>',
        'USER56': '<failed to retrieve the value>',
        'USER57': '<failed to retrieve the value>',
        'USER58': '<failed to retrieve the value>',
        'USER59': '<failed to retrieve the value>',
        'USER6': '<failed to retrieve the value>',
        'USER60': '<failed to retrieve the value>',
        'USER7': '<failed to retrieve the value>',
        'USER8': '<failed to retrieve the value>',
        'USER9': '<failed to retrieve the value>',
        'VELOCITY_X': '<failed to retrieve the value>',
        'VELOCITY_Y': '<failed to retrieve the value>',
        'VELOCITY_Z': '<failed to retrieve the value>',
        'WEAPON0': '<failed to retrieve the value>',
        'WEAPON1': '<failed to retrieve the value>',
        'WEAPON2': '<failed to retrieve the value>',
        'WEAPON3': '<failed to retrieve the value>',
        'WEAPON4': '<failed to retrieve the value>',
        'WEAPON5': '<failed to retrieve the value>',
        'WEAPON6': '<failed to retrieve the value>',
        'WEAPON7': '<failed to retrieve the value>',
        'WEAPON8': '<failed to retrieve the value>',
        'WEAPON9': '<failed to retrieve the value>',
    }


class Label(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    object_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object_position_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object_position_y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object_position_z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class MessageQueueException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Mode(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: vizdoom.vizdoom.Mode, arg0: vizdoom.vizdoom.Mode) -> bool
        
        2. __eq__(self: vizdoom.vizdoom.Mode, arg0: int) -> bool
        """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: vizdoom.vizdoom.Mode) -> tuple """
        return ()

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: vizdoom.vizdoom.Mode) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: vizdoom.vizdoom.Mode, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: vizdoom.vizdoom.Mode) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: vizdoom.vizdoom.Mode, arg0: vizdoom.vizdoom.Mode) -> bool
        
        2. __ne__(self: vizdoom.vizdoom.Mode, arg0: int) -> bool
        """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: vizdoom.vizdoom.Mode) -> str """
        return ""

    def __setstate__(self, arg0): # real signature unknown; restored from __doc__
        """ __setstate__(self: vizdoom.vizdoom.Mode, arg0: tuple) -> None """
        pass

    ASYNC_PLAYER = None # (!) real value is ''
    ASYNC_SPECTATOR = None # (!) real value is ''
    PLAYER = None # (!) real value is ''
    SPECTATOR = None # (!) real value is ''
    __members__ = {
        'ASYNC_PLAYER': '<failed to retrieve the value>',
        'ASYNC_SPECTATOR': '<failed to retrieve the value>',
        'PLAYER': '<failed to retrieve the value>',
        'SPECTATOR': '<failed to retrieve the value>',
    }


class ScreenFormat(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: vizdoom.vizdoom.ScreenFormat, arg0: vizdoom.vizdoom.ScreenFormat) -> bool
        
        2. __eq__(self: vizdoom.vizdoom.ScreenFormat, arg0: int) -> bool
        """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: vizdoom.vizdoom.ScreenFormat) -> tuple """
        return ()

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: vizdoom.vizdoom.ScreenFormat) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: vizdoom.vizdoom.ScreenFormat, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: vizdoom.vizdoom.ScreenFormat) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: vizdoom.vizdoom.ScreenFormat, arg0: vizdoom.vizdoom.ScreenFormat) -> bool
        
        2. __ne__(self: vizdoom.vizdoom.ScreenFormat, arg0: int) -> bool
        """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: vizdoom.vizdoom.ScreenFormat) -> str """
        return ""

    def __setstate__(self, arg0): # real signature unknown; restored from __doc__
        """ __setstate__(self: vizdoom.vizdoom.ScreenFormat, arg0: tuple) -> None """
        pass

    ABGR32 = None # (!) real value is ''
    ARGB32 = None # (!) real value is ''
    BGR24 = None # (!) real value is ''
    BGRA32 = None # (!) real value is ''
    CBCGCR = None # (!) real value is ''
    CRCGCB = None # (!) real value is ''
    DOOM_256_COLORS8 = None # (!) real value is ''
    GRAY8 = None # (!) real value is ''
    RGB24 = None # (!) real value is ''
    RGBA32 = None # (!) real value is ''
    __members__ = {
        'ABGR32': '<failed to retrieve the value>',
        'ARGB32': '<failed to retrieve the value>',
        'BGR24': '<failed to retrieve the value>',
        'BGRA32': '<failed to retrieve the value>',
        'CBCGCR': '<failed to retrieve the value>',
        'CRCGCB': '<failed to retrieve the value>',
        'DOOM_256_COLORS8': '<failed to retrieve the value>',
        'GRAY8': '<failed to retrieve the value>',
        'RGB24': '<failed to retrieve the value>',
        'RGBA32': '<failed to retrieve the value>',
    }


class ScreenResolution(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: vizdoom.vizdoom.ScreenResolution, arg0: vizdoom.vizdoom.ScreenResolution) -> bool
        
        2. __eq__(self: vizdoom.vizdoom.ScreenResolution, arg0: int) -> bool
        """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: vizdoom.vizdoom.ScreenResolution) -> tuple """
        return ()

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: vizdoom.vizdoom.ScreenResolution) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: vizdoom.vizdoom.ScreenResolution, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: vizdoom.vizdoom.ScreenResolution) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: vizdoom.vizdoom.ScreenResolution, arg0: vizdoom.vizdoom.ScreenResolution) -> bool
        
        2. __ne__(self: vizdoom.vizdoom.ScreenResolution, arg0: int) -> bool
        """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: vizdoom.vizdoom.ScreenResolution) -> str """
        return ""

    def __setstate__(self, arg0): # real signature unknown; restored from __doc__
        """ __setstate__(self: vizdoom.vizdoom.ScreenResolution, arg0: tuple) -> None """
        pass

    RES_1024X576 = None # (!) forward: RES_1024X576, real value is ''
    RES_1024X640 = None # (!) forward: RES_1024X640, real value is ''
    RES_1024X768 = None # (!) forward: RES_1024X768, real value is ''
    RES_1280X1024 = None # (!) forward: RES_1280X1024, real value is ''
    RES_1280X720 = None # (!) forward: RES_1280X720, real value is ''
    RES_1280X800 = None # (!) forward: RES_1280X800, real value is ''
    RES_1280X960 = None # (!) forward: RES_1280X960, real value is ''
    RES_1400X1050 = None # (!) forward: RES_1400X1050, real value is ''
    RES_1400X787 = None # (!) forward: RES_1400X787, real value is ''
    RES_1400X875 = None # (!) forward: RES_1400X875, real value is ''
    RES_1600X1000 = None # (!) forward: RES_1600X1000, real value is ''
    RES_1600X1200 = None # (!) forward: RES_1600X1200, real value is ''
    RES_1600X900 = None # (!) forward: RES_1600X900, real value is ''
    RES_160X120 = None # (!) forward: RES_160X120, real value is ''
    RES_1920X1080 = None # (!) forward: RES_1920X1080, real value is ''
    RES_200X125 = None # (!) forward: RES_200X125, real value is ''
    RES_200X150 = None # (!) forward: RES_200X150, real value is ''
    RES_256X144 = None # (!) forward: RES_256X144, real value is ''
    RES_256X160 = None # (!) forward: RES_256X160, real value is ''
    RES_256X192 = None # (!) forward: RES_256X192, real value is ''
    RES_320X180 = None # (!) forward: RES_320X180, real value is ''
    RES_320X200 = None # (!) forward: RES_320X200, real value is ''
    RES_320X240 = None # (!) forward: RES_320X240, real value is ''
    RES_320X256 = None # (!) forward: RES_320X256, real value is ''
    RES_400X225 = None # (!) forward: RES_400X225, real value is ''
    RES_400X250 = None # (!) forward: RES_400X250, real value is ''
    RES_400X300 = None # (!) forward: RES_400X300, real value is ''
    RES_512X288 = None # (!) forward: RES_512X288, real value is ''
    RES_512X320 = None # (!) forward: RES_512X320, real value is ''
    RES_512X384 = None # (!) forward: RES_512X384, real value is ''
    RES_640X360 = None # (!) forward: RES_640X360, real value is ''
    RES_640X400 = None # (!) forward: RES_640X400, real value is ''
    RES_640X480 = None # (!) forward: RES_640X480, real value is ''
    RES_800X450 = None # (!) forward: RES_800X450, real value is ''
    RES_800X500 = None # (!) forward: RES_800X500, real value is ''
    RES_800X600 = None # (!) forward: RES_800X600, real value is ''
    __members__ = {
        'RES_1024X576': '<failed to retrieve the value>',
        'RES_1024X640': '<failed to retrieve the value>',
        'RES_1024X768': '<failed to retrieve the value>',
        'RES_1280X1024': '<failed to retrieve the value>',
        'RES_1280X720': '<failed to retrieve the value>',
        'RES_1280X800': '<failed to retrieve the value>',
        'RES_1280X960': '<failed to retrieve the value>',
        'RES_1400X1050': '<failed to retrieve the value>',
        'RES_1400X787': '<failed to retrieve the value>',
        'RES_1400X875': '<failed to retrieve the value>',
        'RES_1600X1000': '<failed to retrieve the value>',
        'RES_1600X1200': '<failed to retrieve the value>',
        'RES_1600X900': '<failed to retrieve the value>',
        'RES_160X120': '<failed to retrieve the value>',
        'RES_1920X1080': '<failed to retrieve the value>',
        'RES_200X125': '<failed to retrieve the value>',
        'RES_200X150': '<failed to retrieve the value>',
        'RES_256X144': '<failed to retrieve the value>',
        'RES_256X160': '<failed to retrieve the value>',
        'RES_256X192': '<failed to retrieve the value>',
        'RES_320X180': '<failed to retrieve the value>',
        'RES_320X200': '<failed to retrieve the value>',
        'RES_320X240': '<failed to retrieve the value>',
        'RES_320X256': '<failed to retrieve the value>',
        'RES_400X225': '<failed to retrieve the value>',
        'RES_400X250': '<failed to retrieve the value>',
        'RES_400X300': '<failed to retrieve the value>',
        'RES_512X288': '<failed to retrieve the value>',
        'RES_512X320': '<failed to retrieve the value>',
        'RES_512X384': '<failed to retrieve the value>',
        'RES_640X360': '<failed to retrieve the value>',
        'RES_640X400': '<failed to retrieve the value>',
        'RES_640X480': '<failed to retrieve the value>',
        'RES_800X450': '<failed to retrieve the value>',
        'RES_800X500': '<failed to retrieve the value>',
        'RES_800X600': '<failed to retrieve the value>',
    }


class SharedMemoryException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SignalException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ViZDoomErrorException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ViZDoomIsNotRunningException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ViZDoomUnexpectedExitException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

ACTIVATE_SELECTED_ITEM = None # (!) real value is ''

ALTATTACK = None # (!) real value is ''

ALTATTACK_READY = None # (!) real value is ''

AMMO0 = None # (!) real value is ''

AMMO1 = None # (!) real value is ''

AMMO2 = None # (!) real value is ''

AMMO3 = None # (!) real value is ''

AMMO4 = None # (!) real value is ''

AMMO5 = None # (!) real value is ''

AMMO6 = None # (!) real value is ''

AMMO7 = None # (!) real value is ''

AMMO8 = None # (!) real value is ''

AMMO9 = None # (!) real value is ''

ANGLE = None # (!) real value is ''

ARMOR = None # (!) real value is ''

ATTACK = None # (!) real value is ''

ATTACK_READY = None # (!) real value is ''

CROUCH = None # (!) real value is ''

DEAD = None # (!) real value is ''

DEATHCOUNT = None # (!) real value is ''

DROP_SELECTED_ITEM = None # (!) real value is ''

DROP_SELECTED_WEAPON = None # (!) real value is ''

FRAGCOUNT = None # (!) real value is ''

HEALTH = None # (!) real value is ''

ITEMCOUNT = None # (!) real value is ''

JUMP = None # (!) real value is ''

KILLCOUNT = None # (!) real value is ''

LAND = None # (!) real value is ''

LOOK_DOWN = None # (!) real value is ''

LOOK_UP = None # (!) real value is ''

LOOK_UP_DOWN_DELTA = None # (!) real value is ''

MOVE_BACKWARD = None # (!) real value is ''

MOVE_DOWN = None # (!) real value is ''

MOVE_FORWARD = None # (!) real value is ''

MOVE_FORWARD_BACKWARD_DELTA = None # (!) real value is ''

MOVE_LEFT = None # (!) real value is ''

MOVE_LEFT_RIGHT_DELTA = None # (!) real value is ''

MOVE_RIGHT = None # (!) real value is ''

MOVE_UP = None # (!) real value is ''

MOVE_UP_DOWN_DELTA = None # (!) real value is ''

NORMAL = None # (!) real value is ''

OBJECTS = None # (!) real value is ''

OBJECTS_WITH_SIZE = None # (!) real value is ''

ON_GROUND = None # (!) real value is ''

PITCH = None # (!) real value is ''

PLAYER10_FRAGCOUNT = None # (!) real value is ''

PLAYER11_FRAGCOUNT = None # (!) real value is ''

PLAYER12_FRAGCOUNT = None # (!) real value is ''

PLAYER13_FRAGCOUNT = None # (!) real value is ''

PLAYER14_FRAGCOUNT = None # (!) real value is ''

PLAYER15_FRAGCOUNT = None # (!) real value is ''

PLAYER16_FRAGCOUNT = None # (!) real value is ''

PLAYER1_FRAGCOUNT = None # (!) real value is ''

PLAYER2_FRAGCOUNT = None # (!) real value is ''

PLAYER3_FRAGCOUNT = None # (!) real value is ''

PLAYER4_FRAGCOUNT = None # (!) real value is ''

PLAYER5_FRAGCOUNT = None # (!) real value is ''

PLAYER6_FRAGCOUNT = None # (!) real value is ''

PLAYER7_FRAGCOUNT = None # (!) real value is ''

PLAYER8_FRAGCOUNT = None # (!) real value is ''

PLAYER9_FRAGCOUNT = None # (!) real value is ''

PLAYER_COUNT = None # (!) real value is ''

PLAYER_NUMBER = None # (!) real value is ''

POSITION_X = None # (!) real value is ''

POSITION_Y = None # (!) real value is ''

POSITION_Z = None # (!) real value is ''

RELOAD = None # (!) real value is ''

RES_1024X576 = None # (!) real value is ''

RES_1024X640 = None # (!) real value is ''

RES_1024X768 = None # (!) real value is ''

RES_1280X1024 = None # (!) real value is ''

RES_1280X720 = None # (!) real value is ''

RES_1280X800 = None # (!) real value is ''

RES_1280X960 = None # (!) real value is ''

RES_1400X1050 = None # (!) real value is ''

RES_1400X787 = None # (!) real value is ''

RES_1400X875 = None # (!) real value is ''

RES_1600X1000 = None # (!) real value is ''

RES_1600X1200 = None # (!) real value is ''

RES_1600X900 = None # (!) real value is ''

RES_160X120 = None # (!) real value is ''

RES_1920X1080 = None # (!) real value is ''

RES_200X125 = None # (!) real value is ''

RES_200X150 = None # (!) real value is ''

RES_256X144 = None # (!) real value is ''

RES_256X160 = None # (!) real value is ''

RES_256X192 = None # (!) real value is ''

RES_320X180 = None # (!) real value is ''

RES_320X200 = None # (!) real value is ''

RES_320X240 = None # (!) real value is ''

RES_320X256 = None # (!) real value is ''

RES_400X225 = None # (!) real value is ''

RES_400X250 = None # (!) real value is ''

RES_400X300 = None # (!) real value is ''

RES_512X288 = None # (!) real value is ''

RES_512X320 = None # (!) real value is ''

RES_512X384 = None # (!) real value is ''

RES_640X360 = None # (!) real value is ''

RES_640X400 = None # (!) real value is ''

RES_640X480 = None # (!) real value is ''

RES_800X450 = None # (!) real value is ''

RES_800X500 = None # (!) real value is ''

RES_800X600 = None # (!) real value is ''

ROLL = None # (!) real value is ''

SECRETCOUNT = None # (!) real value is ''

SELECTED_WEAPON = None # (!) real value is ''

SELECTED_WEAPON_AMMO = None # (!) real value is ''

SELECT_NEXT_ITEM = None # (!) real value is ''

SELECT_NEXT_WEAPON = None # (!) real value is ''

SELECT_PREV_ITEM = None # (!) real value is ''

SELECT_PREV_WEAPON = None # (!) real value is ''

SELECT_WEAPON0 = None # (!) real value is ''

SELECT_WEAPON1 = None # (!) real value is ''

SELECT_WEAPON2 = None # (!) real value is ''

SELECT_WEAPON3 = None # (!) real value is ''

SELECT_WEAPON4 = None # (!) real value is ''

SELECT_WEAPON5 = None # (!) real value is ''

SELECT_WEAPON6 = None # (!) real value is ''

SELECT_WEAPON7 = None # (!) real value is ''

SELECT_WEAPON8 = None # (!) real value is ''

SELECT_WEAPON9 = None # (!) real value is ''

SPEED = None # (!) real value is ''

STRAFE = None # (!) real value is ''

TURN180 = None # (!) real value is ''

TURN_LEFT = None # (!) real value is ''

TURN_LEFT_RIGHT_DELTA = None # (!) real value is ''

TURN_RIGHT = None # (!) real value is ''

USE = None # (!) real value is ''

USER1 = None # (!) real value is ''

USER10 = None # (!) real value is ''

USER11 = None # (!) real value is ''

USER12 = None # (!) real value is ''

USER13 = None # (!) real value is ''

USER14 = None # (!) real value is ''

USER15 = None # (!) real value is ''

USER16 = None # (!) real value is ''

USER17 = None # (!) real value is ''

USER18 = None # (!) real value is ''

USER19 = None # (!) real value is ''

USER2 = None # (!) real value is ''

USER20 = None # (!) real value is ''

USER21 = None # (!) real value is ''

USER22 = None # (!) real value is ''

USER23 = None # (!) real value is ''

USER24 = None # (!) real value is ''

USER25 = None # (!) real value is ''

USER26 = None # (!) real value is ''

USER27 = None # (!) real value is ''

USER28 = None # (!) real value is ''

USER29 = None # (!) real value is ''

USER3 = None # (!) real value is ''

USER30 = None # (!) real value is ''

USER31 = None # (!) real value is ''

USER32 = None # (!) real value is ''

USER33 = None # (!) real value is ''

USER34 = None # (!) real value is ''

USER35 = None # (!) real value is ''

USER36 = None # (!) real value is ''

USER37 = None # (!) real value is ''

USER38 = None # (!) real value is ''

USER39 = None # (!) real value is ''

USER4 = None # (!) real value is ''

USER40 = None # (!) real value is ''

USER41 = None # (!) real value is ''

USER42 = None # (!) real value is ''

USER43 = None # (!) real value is ''

USER44 = None # (!) real value is ''

USER45 = None # (!) real value is ''

USER46 = None # (!) real value is ''

USER47 = None # (!) real value is ''

USER48 = None # (!) real value is ''

USER49 = None # (!) real value is ''

USER5 = None # (!) real value is ''

USER50 = None # (!) real value is ''

USER51 = None # (!) real value is ''

USER52 = None # (!) real value is ''

USER53 = None # (!) real value is ''

USER54 = None # (!) real value is ''

USER55 = None # (!) real value is ''

USER56 = None # (!) real value is ''

USER57 = None # (!) real value is ''

USER58 = None # (!) real value is ''

USER59 = None # (!) real value is ''

USER6 = None # (!) real value is ''

USER60 = None # (!) real value is ''

USER7 = None # (!) real value is ''

USER8 = None # (!) real value is ''

USER9 = None # (!) real value is ''

VELOCITY_X = None # (!) real value is ''

VELOCITY_Y = None # (!) real value is ''

VELOCITY_Z = None # (!) real value is ''

WEAPON0 = None # (!) real value is ''

WEAPON1 = None # (!) real value is ''

WEAPON2 = None # (!) real value is ''

WEAPON3 = None # (!) real value is ''

WEAPON4 = None # (!) real value is ''

WEAPON5 = None # (!) real value is ''

WEAPON6 = None # (!) real value is ''

WEAPON7 = None # (!) real value is ''

WEAPON8 = None # (!) real value is ''

WEAPON9 = None # (!) real value is ''

WHOLE = None # (!) real value is ''

ZOOM = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

