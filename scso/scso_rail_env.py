from typing import Tuple, Dict

import numpy as np

from flatland.core.env_observation_builder import ObservationBuilder
from flatland.envs.agent_utils import EnvAgent
from flatland.envs.observations import GlobalObsForRailEnv
from flatland.envs.rail_env import RailEnv
from flatland.envs.timetable_generators import timetable_generator


class ScsoRailEnv(RailEnv):
    def __init__(self,
                 width,
                 height,
                 rail_generator=None,
                 line_generator=None,  # : line_gen.LineGenerator = line_gen.random_line_generator(),
                 number_of_agents=2,
                 obs_builder_object: ObservationBuilder = GlobalObsForRailEnv(),
                 malfunction_generator_and_process_data=None,  # mal_gen.no_malfunction_generator(),
                 malfunction_generator=None,
                 remove_agents_at_target=True,
                 random_seed=None,
                 record_steps=False,
                 ):
        super().__init__(width=width,
                       height=height,
                       rail_generator=rail_generator,
                       line_generator=line_generator,
                       number_of_agents=number_of_agents,
                       obs_builder_object=obs_builder_object,
                       malfunction_generator_and_process_data=malfunction_generator_and_process_data,
                       malfunction_generator=malfunction_generator,
                       remove_agents_at_target=remove_agents_at_target,
                       random_seed=random_seed,
                       record_steps=record_steps)
        self.agents_hints = {}



    def reset(self, regenerate_rail: bool = True, regenerate_schedule: bool = True, *,
              random_seed: int = None) -> Tuple[Dict, Dict]:
        """
        reset(regenerate_rail, regenerate_schedule, activate_agents, random_seed)

        The method resets the rail environment

        Parameters
        ----------
        regenerate_rail : bool, optional
            regenerate the rails
        regenerate_schedule : bool, optional
            regenerate the schedule and the static agents
        random_seed : int, optional
            random seed for environment

        Returns
        -------
        observation_dict: Dict
            Dictionary with an observation for each agent
        info_dict: Dict with agent specific information

        """

        if random_seed:
            self._seed(random_seed)

        optionals = {}
        if regenerate_rail or self.rail is None:

            if "__call__" in dir(self.rail_generator):
                rail, optionals = self.rail_generator(
                    self.width, self.height, self.number_of_agents, self.num_resets, self.np_random)
            elif "generate" in dir(self.rail_generator):
                rail, optionals = self.rail_generator.generate(
                    self.width, self.height, self.number_of_agents, self.num_resets, self.np_random)
            else:
                raise ValueError("Could not invoke __call__ or generate on rail_generator")

            self.rail = rail
            self.height, self.width = self.rail.grid.shape

            # Do a new set_env call on the obs_builder to ensure
            # that obs_builder specific instantiations are made according to the
            # specifications of the current environment : like width, height, etc
            self.obs_builder.set_env(self)

        if optionals and 'distance_map' in optionals:
            self.distance_map.set(optionals['distance_map'])

        if regenerate_schedule or regenerate_rail or self.get_num_agents() == 0:
            agents_hints = None
            if optionals and 'agents_hints' in optionals:
                agents_hints = optionals['agents_hints']

            line = self.line_generator(self.rail, self.number_of_agents, agents_hints,
                                       self.num_resets, self.np_random)
            self.agents = EnvAgent.from_line(line)

            # Reset distance map - basically initializing
            self.distance_map.reset(self.agents, self.rail)

            # NEW : Time Schedule Generation
            timetable = timetable_generator(self.agents, self.distance_map,
                                            agents_hints, self.np_random)

            self._max_episode_steps = timetable.max_episode_steps

            for agent_i, agent in enumerate(self.agents):
                agent.earliest_departure = timetable.earliest_departures[agent_i]
                agent.latest_arrival = timetable.latest_arrivals[agent_i]

            #MOD
            train_stations = agents_hints['train_stations']
            self.sync_stations = np.random.choice(train_stations, 1) #TODO remove start and end of lines, stations number
            self.agents_hints = optionals['agents_hints']
        else:
            self.distance_map.reset(self.agents, self.rail)

        # Reset agents to initial states
        self.reset_agents()

        self.num_resets += 1
        self._elapsed_steps = 0

        # Agent positions map
        self.agent_positions = np.zeros((self.height, self.width), dtype=int) - 1
        self._update_agent_positions_map(ignore_old_positions=False)

        self.dones = dict.fromkeys(list(range(self.get_num_agents())) + ["__all__"], False)

        # Reset the state of the observation builder with the new environment
        self.obs_builder.reset()

        # Empty the episode store of agent positions
        self.cur_episode = []

        info_dict = self.get_info_dict()
        # Return the new observation vectors for each agent
        observation_dict: Dict = self._get_observations()
        if hasattr(self, "renderer") and self.renderer is not None:
            self.renderer = None



        return observation_dict, info_dict
