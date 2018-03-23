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



"""

Vizdoom Execution

"""



from __future__ import absolute_import

from __future__ import division

from __future__ import print_function



import argparse

import logging

import os

import time



from tensorforce import TensorForceError

import json

from tensorforce.agents import Agent

from tensorforce.execution import Runner

from viz_doom import VizdoomC





def main():

    parser = argparse.ArgumentParser()



    #parser.add_argument('--mode', help="ID of the game mode")

    #parser.add_argument('--hide', dest='hide', action='store_const', const=True, default=False, help="Hide output window")

   # parser.add_argument('-a', '--agent-config', help="Agent configuration file")
    
    parser.add_argument('-a', '--agent-config', default="configs/ppo.json", help="Agent configuration file")

   # parser.add_argument('-n', '--network-spec', default=None, help="Network specification file")

    parser.add_argument('-n', '--network-spec', default="configs/mlp2_network.json", help="Network specification file")

    parser.add_argument('-e', '--episodes', type=int, default=50000, help="Number of episodes")

    parser.add_argument('-t', '--max-timesteps', type=int, default=2000, help="Maximum number of timesteps per episode")

   # parser.add_argument('-s', '--save', help="Save agent to this dir")
    
    parser.add_argument('-s', '--save', default="bsp.txt" ,help="Save agent to this dir")

    parser.add_argument('-se', '--save-episodes', type=int, default=100, help="Save agent every x episodes")

    parser.add_argument('-l', '--load', help="Load agent from this dir")

    parser.add_argument('-D', '--debug', action='store_true', default=True, help="Show debug outputs")



    args = parser.parse_args()



    logger = logging.getLogger(__name__)

    logger.setLevel(logging.DEBUG)  # configurable!!!



    environment = VizdoomC() #(mode_id=args.mode, visible=not args.hide)


    if args.agent_config is not None:

        with open(args.agent_config, 'r') as fp:

            agent_config = json.load(fp=fp)

    else:

        raise TensorForceError("No agent configuration provided.")

    #network_spec = [dict(type='dense', size=32, activation='tanh'), dict(type='dense', size=32, activation='tanh')]
	

    if args.network_spec is not None:

        with open(args.network_spec, 'r') as fp:
	    
            network_spec = json.load(fp=fp)

    else:

        network_spec = None

        logger.info("No network configuration provided.")


    print("INFO vizdoomtest INFO INFO INFO INFO")
    print("Network")
    print(network_spec)
    print("environment actions")
    print(environment.actions)
    print("environment states")
    print(environment.states)
    print("INFO INFO INFO INFO INFO finished")

    agent = Agent.from_spec(

        #changed kwargs with spec
        spec=agent_config,

        kwargs=dict(

            states = environment.states,

            actions= environment.actions,

            network= network_spec

        )

    )



    if args.load:

        load_dir = os.path.dirname(args.load)

        if not os.path.isdir(load_dir):

            raise OSError("Could not load agent from {}: No such directory.".format(load_dir))

        agent.restore_model(args.load)



    if args.debug:

        logger.info("-" * 16)

        logger.info("Configuration:")

        logger.info(agent_config)



    if args.save:

        save_dir = os.path.dirname(args.save)

        if not os.path.isdir(save_dir):

            try:

                os.mkdir(save_dir, 0o755)

            except OSError:

                raise OSError("Cannot save agent to dir {} ()".format(save_dir))



    runner = Runner(

        agent=agent,

        environment=environment,

        repeat_actions=1

    )



    report_episodes = args.episodes // 1000

    if args.debug:

        report_episodes = 1



    def episode_finished(r):

        if r.episode % report_episodes == 0:

            sps = r.timestep / (time.time() - r.start_time)

            logger.info("Finished episode {ep} after {ts} timesteps. Steps Per Second {sps}".format(ep=r.episode, ts=r.timestep, sps=sps))

            logger.info("Episode reward: {}".format(r.episode_rewards[-1]))

            logger.info("Average of last 500 rewards: {}".format(sum(r.episode_rewards[-500:]) / 500))

            logger.info("Average of last 100 rewards: {}".format(sum(r.episode_rewards[-100:]) / 100))

        return True



    logger.info("Starting {agent} for Environment '{env}'".format(agent=agent, env=environment))

    runner.run(args.episodes, args.max_timesteps, episode_finished=episode_finished)

    runner.close()

    logger.info("Learning finished. Total episodes: {ep}".format(ep=runner.episode))



    environment.close()





if __name__ == '__main__':

    main()