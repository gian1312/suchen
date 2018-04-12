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

import mazeexp as mx

from tensorforce.environments import Environment

class MazeExplorer(Environment):
    """
    MazeExplorer Integration: https://github.com/mryellow/maze_explorer.
    """

    def __init__(self, mode_id=0, visible=True):
        """
        Initialize MazeExplorer.

        Args:
            mode_id: Game mode ID. See https://github.com/mryellow/maze_explorer
            visible: Show output window
        """

        self.mode_id = int(mode_id)
        # Might raise gym.error.UnregisteredEnv or gym.error.DeprecatedEnv
        self.engine = mx.MazeExplorer(mode_id, visible)

    def __str__(self):
        print("MMMMMMMMAAAAAAAAAAAAAAAAAAAAAAAAZZZZZZZZZZZZZZZZEEEEEEEEEEEEEEEEEEE SSSSSSSSSSSEEEEEEEEEELLLF")
        print('MazeExplorer({})'.format(self.mode_id))
        print("MMMMMMMMAAAAAAAAAAAAAAAAAAAAAAAAZZZZZZZZZZZZZZZZEEEEEEEEEEEEEEEEEEE SSSSSSSSSSSEEEEEEEEEELLLF")
        return 'MazeExplorer({})'.format(self.mode_id)

    def close(self):
        self.engine = None

    def reset(self):
        # TODO: Reset to `ones`?
        return self.engine.reset()

    def execute(self, actions):
        print("Exeecuuuttetetet")
        print(actions)
        state, reward, terminal, _ = self.engine.act(actions)
        return state, terminal, reward

    @property
    def states(self):
        # Use `observation_chans` to multichannel with `item` sensors.
        if self.engine.observation_chans > 1:
            shape = (self.engine.observation_num, self.engine.observation_chans)
            print("SHAAAAAAAAAAAAAAAPPPPPEEEEEEEEEEEEEEEEEE")
            print(shape)
            print("SHAAAAAAAAAAAAAAAPPPPPEEEEEEEEEEEEEEEEEE")
        else:
            shape = (self.engine.observation_num,)
            print("SHAAAAAAAAAAAAAAAPPPPPEEEEEEEEEEEEEEEEEE")
            print(shape)
            print("SHAAAAAAAAAAAAAAAPPPPPEEEEEEEEEEEEEEEEEE")

        return dict(shape=shape, type='int')    #int oder float?

    @property
    def actions(self):
        print("actiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiionlist")
        print(dict(type='int', num_actions=self.engine.actions_num))
        print("actiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiionlist")
        return dict(type='int', num_actions=self.engine.actions_num)
