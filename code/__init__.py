import os
import re

import kraft
import numpy as np
import pandas as pd
from get_difference import get_difference
from plot_peek import plot_peek
from read_statistic import read_statistic

SETTING = kraft.json.read("setting.json")
