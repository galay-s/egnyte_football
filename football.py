# coding=utf-8
import pandas as pd

from settings import FILE_NAME, FWIDTHS, INDEX_COL


def remove_dashes(val):
    """Removes dashes.
    There is line with '-' (dashes) in the file."""
    return int(val) if val.isdigit() else None


def get_team_name(df):
    """Returns the name of the team with the smallest difference in ‘for’ and ‘against’ goals."""
    return (df['F'] - df['A']).abs().idxmin()


if __name__ == '__main__':
    df = pd.read_fwf(
        FILE_NAME,
        widths=FWIDTHS,
        converters={'F': remove_dashes, 'A': remove_dashes},
        index_col=INDEX_COL
    )
    print "Team with the smallest difference in ‘for’ and ‘against’ goals is {}".format(get_team_name(df))
