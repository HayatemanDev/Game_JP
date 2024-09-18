import PySimpleGUI as sg
import requests
import time
import json
import csv
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import warnings
import re
import os
import traceback
import numpy as np
from datetime import timedelta

# FutureWarning を抑制
warnings.simplefilter(action='ignore', category=FutureWarning)

def debug_print(window, message):
    window['OUTPUT'].print(f"DEBUG: {message}")
    window.refresh()

def 動画ID抽出(url):
    マッチ = re.search(r'videos/(\d+)', url)
    if マッチ:
        return マッチ.group(1)
    else:
        raise ValueError("無効なTwitch URLです。有効な動画URLを入力してください。")
