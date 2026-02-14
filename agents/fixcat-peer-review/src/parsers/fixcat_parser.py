"""
FIXCAT Parser Module
Parses mainframe FIXCAT messages, LOGREC data, and system logs
"""

import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class FIXCATMessage:
    """Represents a parsed FIXCAT message"""
    timestamp: datetime
    message_id: str
    severity: str
    system_code: str
    abend_code: Optional[str] = None
    job_name: Optional[str] = None
    step_name: Optional[str] = None
    program_name: Optional[str] = None
    description: str = ""
    raw_message: str = ""
    line_number: int = 0
    additional_info: Dict = field(default_factory=dict)


class FIXCATParser:
    """Parser for mainframe FIXCAT messages and LOGREC data"""
    
    # Common mainframe message patterns
    MESSAGE_PATTERN = re.compile(
        r'(?P<msgid>[A-Z]{3}\d{4}[A-Z])\s+(?P<text>.*)',
        re.IGNORECASE
    )
    
    ABEND_PATTERN = re.compile(
        r'(?:ABEND|COMPLETION CODE|SYSTEM CODE)[:\s=]+(?P<code>S?\w{3,4})',
        re.IGNORECASE
    )
    
    JOB_PATTERN = re.compile(
        r'(?:JOB|JOBNAME)[:\s=]+(?P<jobname>\w+)',
        re.IGNORECASE
    )
    
    STEP_PATTERN = re.compile(
        r'(?:STEP|STEPNAME)[:\s=]+(?P<stepname>\w+)',
        re.IGNORECASE
    )
    
    PROGRAM_PATTERN = re.compile(
        r'(?:PROGRAM|PGM)[:\s=]+(?P<program>\w+)',
        re.IGNORECASE
    )
    
    TIMESTAMP_PATTERNS = [
        re.compile(r'(?P<timestamp>\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2})'),
        re.compile(r'(?P<timestamp>\d{2}\.\d{2}\.\d{2}\s+\d{2}:\d{2}:\d{2})'),
        re.compile(r'(?P<timestamp>\d{2}:\d{2}:\d{2}\.\d{2})'),
    ]
    
    # Severity mapping based on message ID prefix
    SEVERITY_MAP = {
        'IEA': 'HIGH',      # System management
        'IEF': 'MEDIUM',    # Job management
        'IEC': 'HIGH',      # Data management
        'IGD': 'MEDIUM',    # SMS
        'IKJ': 'LOW',       # TSO
        'IRR': 'CRITICAL',  # RACF
        'IXG': 'MEDIUM',    # Logger
        'CSV': 'HIGH',      # Contents supervision
    }
    
    def __init__(self):
        self.messages: List[FIXCATMessage] = []
        self.parse_errors: List[str] = []
    
    def parse_file(self, filepath: str) -> List[FIXCATMessage]:
        """Parse a FIXCAT/LOGREC file"""
        self.messages = []
        self.parse_errors = []
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                
            for line_num, line in enumerate(lines, 1):
                try:
                    msg = self.parse_line(line, line_num)
                    if msg:
                        self.messages.append(msg)
                except Exception as e:
                    self.parse_errors.append(f"Line {line_num}: {str(e)}")
        
        except Exception as e:
            self.parse_errors.append(f"File error: {str(e)}")
        
        return self.messages
    
    def parse_line(self, line: str, line_number: int = 0) -> Optional[FIXCATMessage]:
        """Parse a single line of FIXCAT data"""
        line = line.strip()
        if not line or line.startswith('*'):  # Skip empty lines and comments
            return None
        
        # Extract timestamp
        timestamp = self._extract_timestamp(line)
        
        # Extract message ID and text
        msg_match = self.MESSAGE_PATTERN.search(line)
        if not msg_match:
            return None
        
        message_id = msg_match.group('msgid')
        message_text = msg_match.group('text')
        
        # Determine severity
        severity = self._determine_severity(message_id, message_text)
        
        # Extract system code (first 3 chars of message ID)
        system_code = message_id[:3]
        
        # Extract ABEND code if present
        abend_code = self._extract_abend_code(line)
        
        # Extract job information
        job_name = self._extract_pattern(line, self.JOB_PATTERN, 'jobname')
        step_name = self._extract_pattern(line, self.STEP_PATTERN, 'stepname')
        program_name = self._extract_pattern(line, self.PROGRAM_PATTERN, 'program')
        
        # Create message object
        msg = FIXCATMessage(
            timestamp=timestamp,
            message_id=message_id,
            severity=severity,
            system_code=system_code,
            abend_code=abend_code,
            job_name=job_name,
            step_name=step_name,
            program_name=program_name,
            description=message_text,
            raw_message=line,
            line_number=line_number
        )
        
        return msg
    
    def _extract_timestamp(self, line: str) -> datetime:
        """Extract timestamp from line"""
        for pattern in self.TIMESTAMP_PATTERNS:
            match = pattern.search(line)
            if match:
                ts_str = match.group('timestamp')
                try:
                    # Try different timestamp formats
                    for fmt in ['%Y/%m/%d %H:%M:%S', '%y.%m.%d %H:%M:%S', '%H:%M:%S.%f']:
                        try:
                            return datetime.strptime(ts_str, fmt)
                        except ValueError:
                            continue
                except Exception:
                    pass
        
        # Default to current time if no timestamp found
        return datetime.now()
    
    def _extract_abend_code(self, line: str) -> Optional[str]:
        """Extract ABEND code from line"""
        match = self.ABEND_PATTERN.search(line)
        if match:
            code = match.group('code')
            # Normalize ABEND code format
            if not code.startswith('S'):
                code = 'S' + code
            return code.upper()
        return None
    
    def _extract_pattern(self, line: str, pattern: re.Pattern, group: str) -> Optional[str]:
        """Extract a pattern match from line"""
        match = pattern.search(line)
        return match.group(group) if match else None
    
    def _determine_severity(self, message_id: str, message_text: str) -> str:
        """Determine message severity"""
        # Check for critical keywords
        critical_keywords = ['ABEND', 'FAILURE', 'CRITICAL', 'WAIT STATE', 'LOOP']
        if any(kw in message_text.upper() for kw in critical_keywords):
            return 'CRITICAL'
        
        # Check severity map by system code
        system_code = message_id[:3]
        if system_code in self.SEVERITY_MAP:
            return self.SEVERITY_MAP[system_code]
        
        # Check message suffix (I=Info, W=Warning, E=Error, A=Action)
        suffix = message_id[-1]
        if suffix == 'I':
            return 'LOW'
        elif suffix == 'W':
            return 'MEDIUM'
        elif suffix in ['E', 'A']:
            return 'HIGH'
        
        return 'MEDIUM'  # Default
    
    def get_statistics(self) -> Dict:
        """Get parsing statistics"""
        return {
            'total_messages': len(self.messages),
            'parse_errors': len(self.parse_errors),
            'severity_breakdown': self._get_severity_breakdown(),
            'top_message_ids': self._get_top_message_ids(),
            'abend_count': sum(1 for m in self.messages if m.abend_code)
        }
    
    def _get_severity_breakdown(self) -> Dict[str, int]:
        """Get count of messages by severity"""
        breakdown = {}
        for msg in self.messages:
            breakdown[msg.severity] = breakdown.get(msg.severity, 0) + 1
        return breakdown
    
    def _get_top_message_ids(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """Get most frequent message IDs"""
        msg_counts = {}
        for msg in self.messages:
            msg_counts[msg.message_id] = msg_counts.get(msg.message_id, 0) + 1
        
        return sorted(msg_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]