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
import numpy as np
import time, random
from abc import ABCMeta, abstractmethod
from vizdoom import *
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.io import imsave

from tensorforce.environments import Environment
import tensorforce.util

ACTION_SIZE = 3
RESEIZE_HEIGHT = 84
RESEIZE_WIDTH = 84
CHANNELS = 1
listactions1=list(range(0,ACTION_SIZE))
listactions2 = np.identity(ACTION_SIZE, dtype=float).tolist()
actiondict= dict(zip(listactions1, listactions2))


class VizdoomC(Environment):
    """
    Base environment class.
    """
    def __init__(self, mode_id =0, render=True):#, modeid = 0): #(self, render, worker_id, save_img)
        self.height = RESEIZE_HEIGHT
        self.mode_id = int(mode_id)
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
        self.env.set_screen_resolution(ScreenResolution.RES_640X480) # 160X120
        self.env.set_screen_format(ScreenFormat.GRAY8)
        self.env.set_render_hud(render)
        self.env.set_render_crosshair(render)
        self.env.set_render_weapon(render)
        self.env.set_render_decals(render)
        self.env.set_render_particles(render)
        self.env.add_available_button(Button.MOVE_LEFT)
        self.env.add_available_button(Button.MOVE_RIGHT)
        self.env.add_available_button(Button.ATTACK)
        #self.env.add_available_game_variable(GameVariable.POSITION_Z)
        self.env.add_available_game_variable(GameVariable.AMMO2)
        self.env.add_available_game_variable(GameVariable.POSITION_X)
        self.env.add_available_game_variable(GameVariable.POSITION_Y)
        self.env.set_episode_timeout(300)
        self.env.set_episode_start_time(10)
        self.env.set_window_visible(render)
        self.env.set_sound_enabled(True)
        self.env.set_living_reward(-0.01)
        self.env.set_mode(Mode.PLAYER)
        self.env.init()
        
        #print(dir(self))
        #self.actionslist = np.identity(ACTION_SIZE, dtype=int).tolist()
        #self.actionslist = ACTION_SIZE
        listactions1=list(range(0,ACTION_SIZE))
        listactions2 = np.identity(ACTION_SIZE, dtype=float).tolist()
        actiondict= dict(zip(listactions1, listactions2))

# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

        #print("List:")
        #print(np.identity(ACTION_SIZE, dtype=float).tolist()) # {'shape': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]], 'type': 'float'}
        #return
        #self.actionslist = [1,2,3]
        self.reset_environment()
    def __str__(self):
        return 'VizdomMode({})'.format(self.mode_id)
        #raise NotImplementedError
        #print("_str_ ist leer")


    def close(self):
        self.env=None

		
   
    def reset_environment(self): #Redundant??
        self.env.new_episode()
        s = self.env.get_state().screen_buffer
        s = self.process_image(s)
        self.current_state = np.stack((s, s, s, s), axis = 2)
        return self.current_state
    
    def reset(self):
        self.env.new_episode()
        s = self.env.get_state().screen_buffer
        s = self.process_image(s)
        self.current_state = np.stack((s, s, s, s), axis = 2)
        return self.current_state
    

    def seed(self, seed):
      
        seed = 15
        return seed

    def get_current_state(self): 
        return self.current_state
   
    def execute(self, actions):
        actions=int(actions)
        #print("exeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccuuuuuuuuuuuuuuuuuutttttttttttteeeeeeeeeeeeeeeee")
        #print(actions)
        #print(actiondict)
        #actions=(actions.tolist())
        #maxi=max(actions)
        #actions=[1 if x>=maxi else 0 for x in actions]
        action=actiondict[actions]
        '''
		if int(actions)==0:
           actions=[1.0,0.0,0.0]
        elif int(actions)==1:
           actions=[0.0,1.0,0.0]
        elif int(actions)==2:
           actions=[0.0,0.0,1.0]
        else:
           actions=[0.0,0.0,0.0]
        '''		   
        #actions=[round(elem,0) for elem in actions]
        #actions=[1,0,1]
        #print("Linoooox 134")
        #print(action)
        r = self.env.make_action(action) #hier hats änderungen self.env.make_action(actionlist(actions)) 
        d = self.env.is_episode_finished()

        if d == False:
            s = self.env.get_state().screen_buffer
            s = self.process_image(s)
            s_expanded = np.expand_dims(s, axis=2)
            self.current_state = np.append(self.current_state[:,:,1:], s_expanded, axis = 2)


        self.finished = d

        if self.save_img == True:
            self.save_image(self.current_state)

        return [self.current_state, d, r]
    
    
    def process_image (self, image):
        s = resize(image, (self.height, self.width))
        return s

    def help_message(self):
        pass

    @property
    def states(self):
    
        shape=(self.height, self.width,4) #self.actionslist nur platzhalter --> ändern
        return dict(shape=shape, type='float') #self.height, self.width    
    

    @property
    def actions(self):
        return dict(shape=1, type='int', num_actions=ACTION_SIZE)
        #return dict(shape=self.actionslist, type='bool')
        #return dict(type='int', shape=self.actionslist, min_value=0, max_value=1, num_actions=3)
  
