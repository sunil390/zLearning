"""
FIXCAT Peer Review Agent
Main package initialization
"""

from .parsers import FIXCATParser, FIXCATMessage
from .analyzers import IssueAnalyzer, Issue
from .rules import ReviewRulesEngine, ReviewRule
from .reporters import ReportGenerator

__version__ = '1.0.0'
__all__ = [
    'FIXCATParser',
    'FIXCATMessage',
    'IssueAnalyzer',
    'Issue',
    'ReviewRulesEngine',
    'ReviewRule',
    'ReportGenerator'
]