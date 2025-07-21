def convert_to_clingo(env) -> str:
    """
    converts Flatland environment to clingo facts
    """
    # environment properties
    rail_map = env.rail.grid
    height, width, agents = env.height, env.width, env.agents
    clingo_str = f"% clingo representation of a Flatland environment\n% height: {height}, width: {width}, agents: {len(agents)}\n"
    clingo_str += f"\nglobal({env._max_episode_steps}).\n"

    # save start and end positions for each agent
    dir_map = {0: "n", 1: "e", 2: "s", 3: "w"}

    for agent_num, agent_info in enumerate(env.agents):
        init_y, init_x = agent_info.initial_position
        goal_y, goal_x = agent_info.target
        min_start, max_end = agent_info.earliest_departure, agent_info.latest_arrival
        speed = int(1 / agent_info.speed_counter.speed)  # inverse, e.g. 1/2 --> 2, 1/4 --> 4 etc.

        direction = dir_map[agent_info.initial_direction]
        clingo_str += f"\ntrain({agent_num}). "
        clingo_str += f"start({agent_num},({init_y},{init_x}),{min_start},{direction}). "
        clingo_str += f"end({agent_num},({goal_y},{goal_x}),{max_end}). "
        # clingo_str += f"speed({agent_num},{speed}).\n"

    clingo_str += "\n"

    # create an atom for each cell in the environment
    # row_num = len(rail_map) - 1
    for row, row_array in enumerate(rail_map):
        for col, cval in enumerate(row_array):
            clingo_str += f"cell(({row},{col}), {cval}).\n"
        # row_num -= 1
        clingo_str += "\n"

    #MOD create an atom for each station in the environment
    for station_num, station in enumerate(env.stations):
        station_y, station_x = station
        clingo_str += f"station({station_num}, ({station_y},{station_x}).\n"

    #TODO: dwell, headway, depot, waits, transfer
    return (clingo_str)
