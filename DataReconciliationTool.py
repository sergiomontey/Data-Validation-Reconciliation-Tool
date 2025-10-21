"""
Data Validation & Reconciliation Tool
A comprehensive ETL validation and data reconciliation application
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text, MetaData, Table
from datetime import datetime, timedelta
import hashlib
import json
import os
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
import schedule
import time


class DataReconciliationTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Validation & Reconciliation Tool v1.0")
        self.root.geometry("1400x900")
        
        # Configuration
        self.config = self.load_config()
        self.connections = {}
        self.validation_rules = []
        self.scheduled_jobs = []
        self.reconciliation_history = []
        
        # Setup GUI
        self.setup_gui()
        self.setup_scheduler()
