# ================== VK + Telegram Photo Bot GUI ==================
try:
    import tkinter as tk
    from tkinter import messagebox, font, scrolledtext, simpledialog
    _GUI_AVAILABLE = True
except (ImportError, Exception):
    tk = None
    messagebox = None
    font = None
    scrolledtext = None
    simpledialog = None
    _GUI_AVAILABLE = False
import threading
import time
import requests
import os
import re
import difflib
import datetime
import csv
import io
import json
import webbrowser
import platform
import traceback
import math
import sys
import asyncio
from rapidfuzz import fuzz
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes