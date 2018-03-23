# Copyright 2017 reinforce.io. All Rights Reserved.

#

# Licensed under the Apache License, Version 2.0 (the "License");

# you may not use this file except in compliance with the License.

# You may obtain a copy of the License at

#

#     http://www.apache.org/licenses/LICENSE-2.0

#

# Unless required by applicable law or agreed to in writing, software

# distributed under the License is distributed on an "AS IS" BASIS,

# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

# See the License for the specific language governing permissions and

# limitations under the License.

# ==============================================================================





from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

import multiprocessing, threading

from MyEnvironment import *

from vizdoom import *

from skimage.transform import resize

from skimage.color import rgb2gray

from skimage.io import imsave


from tensorforce.environments import Environment

import tensorforce.util


ACTION_SIZE = 3



class VizdoomC(Environment):

    """

    Base environment class.

    """

    def __init__(self):#, modeid = 0): #(self, render, worker_id, save_img)

        self.height = RESEIZE_HEIGHT
        render=True #Dr. Gian
        
        #self.mode_id = int(modeid)

        self.width = RESEIZE_WIDTH

        self.channels = CHANNELS

        self.save_img = False #save_img 

        self.render = render #render

        self.env_id = 1 #worker_id

        self.num_img = 0

        #print("Info\n\n")
        #print(self.actions)

        self.env = DoomGame()

        self.env.set_doom_scenario_path("examples/basic.wad") #This corresponds to the simple task we will pose our agent

        self.env.set_doom_map("map01")

        self.env.set_screen_resolution(ScreenResolution.RES_160X120)

        self.env.set_screen_format(ScreenFormat.GRAY8)

        self.env.set_render_hud(render)

        self.env.set_render_crosshair(render)

        self.env.set_render_weapon(render)

        self.env.set_render_decals(render)

        self.env.set_render_particles(render)

        self.env.add_available_button(Button.MOVE_LEFT)

        self.env.add_available_button(Button.MOVE_RIGHT)

        self.env.add_available_button(Button.ATTACK)

        self.env.add_available_game_variable(GameVariable.AMMO2)

        self.env.add_available_game_variable(GameVariable.POSITION_X)

        self.env.add_available_game_variable(GameVariable.POSITION_Y)

        self.env.set_episode_timeout(300)

        self.env.set_episode_start_time(10)

        self.env.set_window_visible(render)

        self.env.set_sound_enabled(False)

        self.env.set_living_reward(-1)

        self.env.set_mode(Mode.PLAYER)

        self.env.init()
        
        #print(dir(self))

        #self.actionslist = np.identity(ACTION_SIZE, dtype=float).tolist()
        self.actionslist = [1,2,3]

        self.reset_environment()

    def __str__(self):

        raise NotImplementedError
        #print("_str_ ist leer")
        #return 'MazeExplorer({})'.format(self.mode_id)


    def close(self):

        raise NotImplementedError

    def reset_environment(self):
        self.reset()

    def reset(self):

        self.env.new_episode()

        s = self.env.get_state().screen_buffer

        s = self.process_image(s)

        self.current_state = np.stack((s, s, s, s), axis = 2)

        return self.current_state
    


    def seed(self, seed):

      

        seed = 15

        return seed


    def get_current_state(self): # Neu, wir wissen nicht von wo current state kommt. (aus Viz oder ENV)

        return self.current_state

   
    def execute(self, actionslist):

        r = self.env.make_action(self.actionslist[action]) / 100.0

        d = self.env.is_episode_finished()



        if d == False:

            s = self.env.get_state().screen_buffer

            s = self.process_image(s)

            s_expanded = np.expand_dims(s, axis=2)

            self.current_state = np.append(self.current_state[:,:,1:], s_expanded, axis = 2)



        self.finished = d



        if self.save_img == True:

            self.save_image(self.current_state)



        return [self.current_state, r, d]
    
    
    def process_image (self, image):
        s = resize(image, (self.height, self.width))
        return s


    def help_message(self):
        pass


    @property

    def states(self):
    
        shape=(self.height, self.width)

        return dict(shape=shape, type='float') #self.height, self.width    
    


    @property

    def actions(self):

        return dict(shape=self.actionslist, type='float')
     #   return dict(shape=self.actionslist, type='bool', min_value=0, max_value=1)
        #return dict(type='int', shape=self.actionslist, min_value=0, max_value=1, num_actions=3)
  
