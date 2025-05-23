import logging
import numpy as np
import pandas as pd
import traceback
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from typing import List

logging.basicConfig(level=logging.INFO)


def remove_columns_with_all_zeros(data: pd.DataFrame) -> pd.DataFrame:
    """Remove columns that contain all zeros from the input DataFrame.

    Parameters
    ----------
    data : pd.DataFrame
        The input DataFrame.

    Returns
    -------
    modified_df : pd.DataFrame
        The modified DataFrame with the columns that contain all zeros removed.

    Raises
    ------
    Exception
        If an error occurs during the execution of the function.
    """
    try:
        # Copy the input DataFrame to avoid modifying it directly
        modified_df = data.copy()

        # Find the columns that contain all zeros and remove them from the DataFrame
        all_zero_col_filter = (modified_df == 0).all(axis=0)
        modified_df = modified_df.loc[:, ~all_zero_col_filter]

        return modified_df
    except Exception as e:
        # Print the traceback if an exception occurs
        print(f"An error occurred: {e}")
        raise


def log_transformation(data: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Apply log(x + 1) transformation on selected columns of a given DataFrame.

    Parameters
    ----------
    data : pd.DataFrame
        The input DataFrame.
    columns : List[str]
        The list of column names to apply the log transformation.

    Returns
    -------
    pd.DataFrame
        The transformed DataFrame with log-transformed values in the selected columns.
    """
    transformed_data = data.copy()

    for col in columns:
        if col not in transformed_data.columns:
            logging.warning(f"Column {col} not present in the data.")
            continue

        transformed_data[col] = np.log1p(transformed_data[col])

    return transformed_data


def inverse_transform(data: pd.DataFrame, columns: List) -> pd.DataFrame:
    """Apply the inverse transformation by taking the reciprocal of specified columns.

    Parameters
    ----------
    data : pd.DataFrame
        The input DataFrame.
    columns : List
        The list of column names to apply the inverse transformation to.

    Returns
    -------
    pd.DataFrame
        The transformed DataFrame with inverse-transformed values in the specified columns.
    """

    transformed_df = data.copy()

    for column in columns:
        try:
            transformed_df[column] = -1 * transformed_df[column]

        except KeyError as e:
            logging.error(f"Column {e} not present in the data.")

        except Exception as e:  # noqa
            logging.error(traceback.print_exc())
            continue

    return transformed_df


def scale_columns(
    data: pd.DataFrame, columns: List[str], strategy: str
) -> pd.DataFrame:
    """Scale the specified columns in a Pandas DataFrame using the specified scaling strategy.

    Parameters
    ----------
    data : pd.DataFrame
        The input DataFrame.
    columns : List[str]
        The list of column names to be scaled.
    strategy : str
        The scaling strategy to be used. Available options are 'custom', 'MinMaxScaler', and 'StandardScaler'.

    Returns
    -------
    pd.DataFrame
        The DataFrame with the specified columns scaled according to the specified strategy.
    """

    scaled_df = data.copy()

    if strategy == "custom":
        for col in columns:
            scaled_df[col] = scaled_df[col] / scaled_df[col].max()

    elif strategy == "MinMaxScaler":
        scaler = MinMaxScaler()
        scaled_df[columns] = scaler.fit_transform(scaled_df[columns])

    elif strategy == "StandardScaler":
        scaler = StandardScaler()
        scaled_df[columns] = scaler.fit_transform(scaled_df[columns])

    else:
        raise ValueError(
            "Invalid scaling strategy. Available options are 'custom', 'MinMaxScaler', and 'StandardScaler'."
        )

    return scaled_df
