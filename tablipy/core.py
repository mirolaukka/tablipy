from typing import Union, List


class Tablipy:
    def __init__(self, col_headers: List[str]):
        self.col_headers = col_headers
        self.cols = []
        self.rows = []
        self.table = [self.cols, self.rows]

    def get(self, column: Union[int, str] = None, row: int = None):
        """ 
            This should return either the column, row, or the cell @ column, row
        """

        if type(column) == str:  # Means they search by the column header
            pass

        elif type(column) == int:  # They searchc it by index
            pass

        elif column == None and row is not None:  # means they want to get row
            pass

        else:  # They search by using col and row
            pass

        pass

    def set(self, column: int = None, row: int = None, data=None):
        """
            This should set either column, row or the cell @ column,row to `data`

            TODO: Need to diffrenciate between setting a col or row and setting a specific cell. -> should accept different type of data.
            Setting a col, or row should take an array, and setting a specific cell should take a string
        """

        pass

    def print(self):
        """
            Pretty print the table
        """
        pass


class Cell:
    def __init__(self, col, row, data=None):
        self.coordinates = (col, row)
        self.data = data

    def get_data(self):
        return self.data

    def get_coordinates(self):
        return self.coordinates
