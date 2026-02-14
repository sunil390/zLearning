"""
Issue Analyzer Module
Analyzes parsed FIXCAT messages to identify patterns, trends, and issues
"""

from typing import Dict, List, Set, Tuple
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from typing import Optional
import yaml

try:
    from ..parsers.fixcat_parser import FIXCATMessage
except ImportError:
    from parsers.fixcat_parser import FIXCATMessage


@dataclass
class Issue:
    """Represents an identified issue"""
    issue_id: str
    title: str
    severity: str
    category: str
    description: str
    occurrences: int = 1
    first_seen: Optional[datetime] = None
    last_seen: Optional[datetime] = None
    affected_jobs: Set[str] = field(default_factory=set)
    affected_programs: Set[str] = field(default_factory=set)
    message_ids: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    related_messages: List[FIXCATMessage] = field(default_factory=list)


class IssueAnalyzer:
    """Analyzes FIXCAT messages to identify issues and patterns"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path)
        self.issues: List[Issue] = []
        self.patterns = self.config.get('analysis', {}).get('patterns', {})
        self.rules = self.config.get('rules', {}).get('checks', [])
        self.ptf_mapping = self.config.get('ptf_mapping', {})
    
    def _load_config(self, config_path: Optional[str]) -> Dict:
        """Load configuration from YAML file"""
        if not config_path:
            return {}
        
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Warning: Could not load config: {e}")
            return {}
    
    def analyze(self, messages: List[FIXCATMessage]) -> List[Issue]:
        """Analyze messages and identify issues"""
        self.issues = []
        
        if not messages:
            return self.issues
        
        # Run various analysis checks
        self._analyze_abend_patterns(messages)
        self._analyze_storage_issues(messages)
        self._analyze_security_violations(messages)
        self._analyze_performance_issues(messages)
        self._analyze_data_integrity(messages)
        self._analyze_recurring_messages(messages)
        self._analyze_job_failures(messages)
        
        # Sort issues by severity and occurrence
        self.issues.sort(key=lambda x: (
            self._severity_weight(x.severity),
            -x.occurrences
        ))
        
        return self.issues
    
    def _severity_weight(self, severity: str) -> int:
        """Convert severity to numeric weight for sorting"""
        weights = {
            'CRITICAL': 0,
            'HIGH': 1,
            'MEDIUM': 2,
            'LOW': 3
        }
        return weights.get(severity.upper(), 4)
    
    def _analyze_abend_patterns(self, messages: List[FIXCATMessage]):
        """Analyze ABEND patterns"""
        abend_messages = [m for m in messages if m.abend_code]
        
        if not abend_messages:
            return
        
        # Group by ABEND code
        abend_groups = defaultdict(list)
        for msg in abend_messages:
            abend_groups[msg.abend_code].append(msg)
        
        # Check for frequent ABENDs
        for abend_code, msgs in abend_groups.items():
            if len(msgs) >= 3:  # Threshold for "frequent"
                issue = Issue(
                    issue_id=f"ABEND-{abend_code}",
                    title=f"Frequent ABEND {abend_code}",
                    severity="HIGH",
                    category="ABEND",
                    description=f"ABEND {abend_code} occurred {len(msgs)} times",
                    occurrences=len(msgs),
                    first_seen=min(m.timestamp for m in msgs),
                    last_seen=max(m.timestamp for m in msgs),
                    affected_jobs={m.job_name for m in msgs if m.job_name},
                    affected_programs={m.program_name for m in msgs if m.program_name},
                    message_ids=[m.message_id for m in msgs],
                    recommendations=self._get_abend_recommendations(abend_code),
                    related_messages=msgs[:5]  # Keep first 5 for reference
                )
                self.issues.append(issue)
    
    def _analyze_storage_issues(self, messages: List[FIXCATMessage]):
        """Analyze storage-related issues"""
        storage_codes = ['S80A', 'S878', 'SB37', 'SD37', 'SE37']
        storage_messages = [
            m for m in messages 
            if m.abend_code in storage_codes or 
            any(code in m.description.upper() for code in storage_codes)
        ]
        
        if storage_messages:
            issue = Issue(
                issue_id="STORAGE-001",
                title="Storage Management Issues Detected",
                severity="HIGH",
                category="STORAGE",
                description=f"Detected {len(storage_messages)} storage-related errors",
                occurrences=len(storage_messages),
                first_seen=min(m.timestamp for m in storage_messages),
                last_seen=max(m.timestamp for m in storage_messages),
                affected_jobs={m.job_name for m in storage_messages if m.job_name},
                recommendations=[
                    "Review space allocations for affected datasets",
                    "Consider implementing SMS storage management",
                    "Increase primary/secondary space allocations",
                    "Review dataset retention policies"
                ],
                related_messages=storage_messages[:5]
            )
            self.issues.append(issue)
    
    def _analyze_security_violations(self, messages: List[FIXCATMessage]):
        """Analyze security violations"""
        security_messages = [
            m for m in messages 
            if m.system_code == 'IRR' or 
            'RACF' in m.description.upper() or
            'UNAUTHORIZED' in m.description.upper()
        ]
        
        if security_messages:
            issue = Issue(
                issue_id="SECURITY-001",
                title="Security Violations Detected",
                severity="CRITICAL",
                category="SECURITY",
                description=f"Detected {len(security_messages)} security violations",
                occurrences=len(security_messages),
                first_seen=min(m.timestamp for m in security_messages),
                last_seen=max(m.timestamp for m in security_messages),
                affected_jobs={m.job_name for m in security_messages if m.job_name},
                recommendations=[
                    "Review RACF profiles and permissions",
                    "Audit user access rights",
                    "Check for unauthorized access attempts",
                    "Update security policies as needed"
                ],
                related_messages=security_messages[:5]
            )
            self.issues.append(issue)
    
    def _analyze_performance_issues(self, messages: List[FIXCATMessage]):
        """Analyze performance-related issues"""
        perf_keywords = ['TIMEOUT', 'DEGRADED', 'SLOW', 'S322']
        perf_messages = [
            m for m in messages 
            if any(kw in m.description.upper() for kw in perf_keywords) or
            m.abend_code == 'S322'
        ]
        
        if perf_messages:
            issue = Issue(
                issue_id="PERF-001",
                title="Performance Degradation Detected",
                severity="MEDIUM",
                category="PERFORMANCE",
                description=f"Detected {len(perf_messages)} performance-related issues",
                occurrences=len(perf_messages),
                first_seen=min(m.timestamp for m in perf_messages),
                last_seen=max(m.timestamp for m in perf_messages),
                affected_jobs={m.job_name for m in perf_messages if m.job_name},
                recommendations=[
                    "Review job execution times",
                    "Check system resource utilization",
                    "Consider workload balancing",
                    "Review time limit parameters"
                ],
                related_messages=perf_messages[:5]
            )
            self.issues.append(issue)
    
    def _analyze_data_integrity(self, messages: List[FIXCATMessage]):
        """Analyze data integrity issues"""
        data_codes = ['S0C7', 'IEC']
        data_messages = [
            m for m in messages 
            if m.abend_code == 'S0C7' or m.system_code == 'IEC'
        ]
        
        if data_messages:
            issue = Issue(
                issue_id="DATA-001",
                title="Data Integrity Issues Detected",
                severity="HIGH",
                category="DATA",
                description=f"Detected {len(data_messages)} data-related errors",
                occurrences=len(data_messages),
                first_seen=min(m.timestamp for m in data_messages),
                last_seen=max(m.timestamp for m in data_messages),
                affected_jobs={m.job_name for m in data_messages if m.job_name},
                recommendations=[
                    "Verify data initialization routines",
                    "Check for uninitialized numeric fields",
                    "Review data conversion logic",
                    "Validate input data sources"
                ],
                related_messages=data_messages[:5]
            )
            self.issues.append(issue)
    
    def _analyze_recurring_messages(self, messages: List[FIXCATMessage]):
        """Analyze recurring message patterns"""
        msg_counter = Counter(m.message_id for m in messages)
        
        for msg_id, count in msg_counter.most_common(10):
            if count >= 5:  # Threshold for recurring
                related = [m for m in messages if m.message_id == msg_id]
                
                issue = Issue(
                    issue_id=f"RECURRING-{msg_id}",
                    title=f"Recurring Message {msg_id}",
                    severity="MEDIUM",
                    category="PATTERN",
                    description=f"Message {msg_id} occurred {count} times",
                    occurrences=count,
                    first_seen=min(m.timestamp for m in related),
                    last_seen=max(m.timestamp for m in related),
                    affected_jobs={m.job_name for m in related if m.job_name},
                    recommendations=[
                        "Investigate root cause of recurring message",
                        "Review related system configuration",
                        "Consider implementing preventive measures"
                    ],
                    related_messages=related[:5]
                )
                self.issues.append(issue)
    
    def _analyze_job_failures(self, messages: List[FIXCATMessage]):
        """Analyze job failure patterns"""
        failure_keywords = ['FAILED', 'ABEND', 'ERROR', 'CANCELLED']
        failure_messages = [
            m for m in messages 
            if any(kw in m.description.upper() for kw in failure_keywords)
        ]
        
        # Group by job name
        job_failures = defaultdict(list)
        for msg in failure_messages:
            if msg.job_name:
                job_failures[msg.job_name].append(msg)
        
        # Report jobs with multiple failures
        for job_name, msgs in job_failures.items():
            if len(msgs) >= 2:
                issue = Issue(
                    issue_id=f"JOB-FAIL-{job_name}",
                    title=f"Multiple Failures in Job {job_name}",
                    severity="HIGH",
                    category="JOB",
                    description=f"Job {job_name} failed {len(msgs)} times",
                    occurrences=len(msgs),
                    first_seen=min(m.timestamp for m in msgs),
                    last_seen=max(m.timestamp for m in msgs),
                    affected_jobs={job_name},
                    recommendations=[
                        "Review job JCL and parameters",
                        "Check job dependencies",
                        "Verify input data availability",
                        "Review job scheduling"
                    ],
                    related_messages=msgs[:5]
                )
                self.issues.append(issue)
    
    def _get_abend_recommendations(self, abend_code: str) -> List[str]:
        """Get recommendations for specific ABEND code"""
        return self.ptf_mapping.get(abend_code, [
            f"Review IBM documentation for ABEND {abend_code}",
            "Check for applicable PTFs",
            "Analyze dump if available"
        ])
    
    def get_summary(self) -> Dict:
        """Get analysis summary"""
        return {
            'total_issues': len(self.issues),
            'by_severity': self._count_by_severity(),
            'by_category': self._count_by_category(),
            'top_issues': [
                {
                    'id': issue.issue_id,
                    'title': issue.title,
                    'severity': issue.severity,
                    'occurrences': issue.occurrences
                }
                for issue in self.issues[:5]
            ]
        }
    
    def _count_by_severity(self) -> Dict[str, int]:
        """Count issues by severity"""
        return dict(Counter(issue.severity for issue in self.issues))
    
    def _count_by_category(self) -> Dict[str, int]:
        """Count issues by category"""
        return dict(Counter(issue.category for issue in self.issues))