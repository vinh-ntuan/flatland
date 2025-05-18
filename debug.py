#!/usr/bin/env python3
""" Test conditions: 
 - Each time stamp & train has maximal 1 action
 - TODO: If there's start and end, check
"""
from sys import stdin
import re

def main():
    lines = stdin.readlines()
    solutions = []
    for i in range(0, len(lines) - 1):
        if lines[i].startswith("Answer"):
            solutions.append(Solution.parse(lines[i+1]))
    for id, s in enumerate(solutions):
        print("---------")
        print(f"Solution {id+1}")
        print(s.pretty_string())
        


class Action:
    PATTERN = r"action\(train\((\d+)\),(\w+),(\d+)\)"
    def __init__(self, train, action, time):
        self.train_id = train
        self.type = action
        self.time = time

    def __repr__(self):
        return f"action(train({self.train_id}),{self.type},{self.time})"
    
    def parse(string):
        match = re.match(Action.PATTERN, string)

        if match:
            train = match.group(1)
            action = match.group(2)
            time = int(match.group(3))
            return Action(train, action, time)
        else:
            raise ValueError(f"Invalid action string: {string} or wrong pattern: {Action.PATTERN}")


class Solution:
    def __init__(self, train_ids, time_steps, actions : list[Action]):
        self.train_ids = train_ids
        self.actions = actions
        self.time_steps = time_steps


    def parse(string: str):
        actions = []
        time_steps = set()
        train_ids = set()
        atoms = string.split()
        for atom in atoms:
            if atom.startswith("action"):
                action = Action.parse(atom)
                actions.append(action)
                train_ids.add(action.train_id)
                time_steps.add(action.time)

        return Solution(sorted(train_ids), sorted(time_steps), actions)

    def pretty_string(self):
        ACTION_MAX_LENGTH = 17
        string = ""
        
        # print actions for each train_id, sorted on timestamp
        for id in self.train_ids:
            actions = [a for a in self.actions if a.train_id == id]
            actions.sort(key=lambda a: a.time)
            string += f"\nActions for train {id}: \n"

            for a in actions:
                string += f"{a.time}: {a.type} ".ljust(ACTION_MAX_LENGTH) # padding for easy read

        return string
        


        





if __name__ == "__main__":
    main()