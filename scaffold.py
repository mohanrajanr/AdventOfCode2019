import os
import argparse
from pathlib import Path


class ProblemScaffold(object):

    def __init__(self, problem_number=None):
        self.problem_number = problem_number

    def validate(self):
        assert type(self.problem_number) == int

    def create_data_directory(self):
        print("Creating Data Directory:{}".format(self.problem_number))
        Path('{}/data'.format(self.problem_number)).mkdir(parents=True)

    def create_log_directory(self):
        print("Creating Logs Directory:{}".format(self.problem_number))
        Path('{}/logs'.format(self.problem_number)).mkdir(parents=True)

    def create_directories(self):
        print("Creating Directory:{}".format(self.problem_number))

        self.create_data_directory()
        self.create_log_directory()

    def create_problem_file(self):
        print("Creating Problem File:{}".format(self.problem_number))
        Path('{}/{}.py'.format(self.problem_number, self.problem_number)).touch()

    def create_input_file(self):
        print("Creating Input File:{}".format(self.problem_number))
        Path('{}/data/input.txt'.format(self.problem_number)).touch()

    def create_test_file(self, number):
        print("Creating Test File:{}".format(self.problem_number))
        Path('{}/data/test{}.txt'.format(self.problem_number, number)).touch()

    def create_file(self):
        self.create_problem_file()
        self.create_input_file()
        self.create_test_file(1)

    def __call__(self, *args, **kwargs):
        # Validate the Input
        self.validate()

        # Create the Files Required
        self.create_directories()
        self.create_file()


def main():
    scaffold = ProblemScaffold()
    parser = argparse.ArgumentParser(prog="Problem Scaffold",
                                     description="Create Files & Folders for Problems")
    parser.add_argument('problem_number', type=int, help='Enter the Problem Name')

    # Get the Arguments and Start Scaffolding them.
    parser.parse_args(namespace=scaffold)
    scaffold()


if __name__ == '__main__':
    main()
