"""
Review Rules Engine
Defines and executes peer review rules for FIXCAT analysis
"""

from typing import List, Dict, Callable, Any
from datetime import datetime, timedelta
from dataclasses import dataclass
from collections import defaultdict

try:
    from ..parsers.fixcat_parser import FIXCATMessage
    from ..analyzers.issue_analyzer import Issue
except ImportError:
    from parsers.fixcat_parser import FIXCATMessage
    from analyzers.issue_analyzer import Issue


@dataclass
class ReviewRule:
    """Represents a review rule"""
    name: str
    description: str
    severity: str
    category: str
    check_function: Callable
    threshold: int = 1
    timeframe_hours: int = 24
    enabled: bool = True


class ReviewRulesEngine:
    """Engine for executing peer review rules"""
    
    def __init__(self):
        self.rules: List[ReviewRule] = []
        self._initialize_default_rules()
    
    def _initialize_default_rules(self):
        """Initialize default review rules"""
        
        # Rule 1: Detect frequent ABENDs
        self.add_rule(ReviewRule(
            name="frequent_abends",
            description="Detect jobs with frequent ABEND occurrences",
            severity="HIGH",
            category="STABILITY",
            check_function=self._check_frequent_abends,
            threshold=3,
            timeframe_hours=24
        ))
        
        # Rule 2: Detect storage exhaustion patterns
        self.add_rule(ReviewRule(
            name="storage_exhaustion",
            description="Identify storage exhaustion issues",
            severity="HIGH",
            category="CAPACITY",
            check_function=self._check_storage_exhaustion,
            threshold=2,
            timeframe_hours=12
        ))
        
        # Rule 3: Security violation detection
        self.add_rule(ReviewRule(
            name="security_violations",
            description="Detect security and authorization violations",
            severity="CRITICAL",
            category="SECURITY",
            check_function=self._check_security_violations,
            threshold=1,
            timeframe_hours=24
        ))
        
        # Rule 4: Performance degradation
        self.add_rule(ReviewRule(
            name="performance_degradation",
            description="Identify performance issues and timeouts",
            severity="MEDIUM",
            category="PERFORMANCE",
            check_function=self._check_performance_issues,
            threshold=5,
            timeframe_hours=24
        ))
        
        # Rule 5: Data integrity issues
        self.add_rule(ReviewRule(
            name="data_integrity",
            description="Check for data corruption and integrity issues",
            severity="HIGH",
            category="DATA_QUALITY",
            check_function=self._check_data_integrity,
            threshold=2,
            timeframe_hours=24
        ))
        
        # Rule 6: Recurring error patterns
        self.add_rule(ReviewRule(
            name="recurring_errors",
            description="Identify recurring error patterns",
            severity="MEDIUM",
            category="PATTERN",
            check_function=self._check_recurring_errors,
            threshold=10,
            timeframe_hours=24
        ))
        
        # Rule 7: Job failure cascades
        self.add_rule(ReviewRule(
            name="job_cascades",
            description="Detect cascading job failures",
            severity="HIGH",
            category="DEPENDENCY",
            check_function=self._check_job_cascades,
            threshold=3,
            timeframe_hours=6
        ))
        
        # Rule 8: System resource contention
        self.add_rule(ReviewRule(
            name="resource_contention",
            description="Identify resource contention issues",
            severity="MEDIUM",
            category="RESOURCE",
            check_function=self._check_resource_contention,
            threshold=5,
            timeframe_hours=12
        ))
    
    def add_rule(self, rule: ReviewRule):
        """Add a custom review rule"""
        self.rules.append(rule)
    
    def execute_rules(self, messages: List[FIXCATMessage]) -> List[Issue]:
        """Execute all enabled rules against messages"""
        findings: List[Issue] = []
        
        for rule in self.rules:
            if not rule.enabled:
                continue
            
            try:
                rule_findings = rule.check_function(messages, rule)
                if rule_findings:
                    findings.extend(rule_findings)
            except Exception as e:
                print(f"Error executing rule {rule.name}: {e}")
        
        return findings
    
    def _check_frequent_abends(self, messages: List[FIXCATMessage], rule: ReviewRule) -> List[Issue]:
        """Check for frequent ABEND occurrences"""
        findings = []
        abend_messages = [m for m in messages if m.abend_code]
        
        # Group by job and ABEND code
        job_abends = defaultdict(lambda: defaultdict(list))
        for msg in abend_messages:
            if msg.job_name:
                job_abends[msg.job_name][msg.abend_code].append(msg)
        
        # Check threshold
        for job_name, abend_codes in job_abends.items():
            for abend_code, msgs in abend_codes.items():
                if len(msgs) >= rule.threshold:
                    findings.append(Issue(
                        issue_id=f"RULE-ABEND-{job_name}-{abend_code}",
                        title=f"Frequent ABEND {abend_code} in {job_name}",
                        severity=rule.severity,
                        category=rule.category,
                        description=f"Job {job_name} experienced ABEND {abend_code} {len(msgs)} times",
                        occurrences=len(msgs),
                        first_seen=min(m.timestamp for m in msgs),
                        last_seen=max(m.timestamp for m in msgs),
                        affected_jobs={job_name},
                        recommendations=[
                            f"Investigate root cause of ABEND {abend_code}",
                            "Review job JCL and program logic",
                            "Check for applicable PTFs",
                            "Consider implementing error handling"
                        ],
                        related_messages=msgs[:5]
                    ))
        
        return findings
    
    def _check_storage_exhaustion(self, messages: List[FIXCATMessage], rule: ReviewRule) -> List[Issue]:
        """Check for storage exhaustion issues"""
        findings = []
        storage_codes = ['SB37', 'SD37', 'SE37', 'S80A', 'S878']
        
        storage_messages = [
            m for m in messages 
            if m.abend_code in storage_codes
        ]
        
        if len(storage_messages) >= rule.threshold:
            findings.append(Issue(
                issue_id="RULE-STORAGE-001",
                title="Storage Exhaustion Pattern Detected",
                severity=rule.severity,
                category=rule.category,
                description=f"Detected {len(storage_messages)} storage-related failures",
                occurrences=len(storage_messages),
                first_seen=min(m.timestamp for m in storage_messages),
                last_seen=max(m.timestamp for m in storage_messages),
                affected_jobs={m.job_name for m in storage_messages if m.job_name},
                recommendations=[
                    "Review and increase space allocations",
                    "Implement SMS storage management",
                    "Review dataset retention policies",
                    "Consider compression for large datasets"
                ],
                related_messages=storage_messages[:5]
            ))
        
        return findings
    
    def _check_security_violations(self, messages: List[FIXCATMessage], rule: ReviewRule) -> List[Issue]:
        """Check for security violations"""
        findings = []
        
        security_messages = [
            m for m in messages 
            if m.system_code == 'IRR' or 
            'RACF' in m.description.upper() or
            'UNAUTHORIZED' in m.description.upper() or
            'ACCESS DENIED' in m.description.upper()
        ]
        
        if len(security_messages) >= rule.threshold:
            findings.append(Issue(
                issue_id="RULE-SECURITY-001",
                title="Security Violations Detected",
                severity=rule.severity,
                category=rule.category,
                description=f"Detected {len(security_messages)} security-related violations",
                occurrences=len(security_messages),
                first_seen=min(m.timestamp for m in security_messages),
                last_seen=max(m.timestamp for m in security_messages),
                affected_jobs={m.job_name for m in security_messages if m.job_name},
                recommendations=[
                    "Immediate security audit required",
                    "Review RACF profiles and permissions",
                    "Check for unauthorized access attempts",
                    "Update security policies",
                    "Consider implementing additional monitoring"
                ],
                related_messages=security_messages[:5]
            ))
        
        return findings
    
    def _check_performance_issues(self, messages: List[FIXCATMessage], rule: ReviewRule) -> List[Issue]:
        """Check for performance issues"""
        findings = []
        perf_keywords = ['TIMEOUT', 'SLOW', 'DEGRADED', 'WAIT']
        
        perf_messages = [
            m for m in messages 
            if any(kw in m.description.upper() for kw in perf_keywords) or
            m.abend_code == 'S322'
        ]
        
        if len(perf_messages) >= rule.threshold:
            findings.append(Issue(
                issue_id="RULE-PERF-001",
                title="Performance Degradation Pattern",
                severity=rule.severity,
                category=rule.category,
                description=f"Detected {len(perf_messages)} performance-related issues",
                occurrences=len(perf_messages),
                first_seen=min(m.timestamp for m in perf_messages),
                last_seen=max(m.timestamp for m in perf_messages),
                affected_jobs={m.job_name for m in perf_messages if m.job_name},
                recommendations=[
                    "Review system resource utilization",
                    "Analyze job execution times",
                    "Consider workload balancing",
                    "Review time limit parameters",
                    "Check for I/O bottlenecks"
                ],
                related_messages=perf_messages[:5]
            ))
        
        return findings
    
    def _check_data_integrity(self, messages: List[FIXCATMessage], rule: ReviewRule) -> List[Issue]:
        """Check for data integrity issues"""
        findings = []
        
        data_messages = [
            m for m in messages 
            if m.abend_code in ['S0C7', 'S0CB'] or
            m.system_code == 'IEC'
        ]
        
        if len(data_messages) >= rule.threshold:
            findings.append(Issue(
                issue_id="RULE-DATA-001",
                title="Data Integrity Issues Detected",
                severity=rule.severity,
                category=rule.category,
                description=f"Detected {len(data_messages)} data integrity issues",
                occurrences=len(data_messages),
                first_seen=min(m.timestamp for m in data_messages),
                last_seen=max(m.timestamp for m in data_messages),
                affected_jobs={m.job_name for m in data_messages if m.job_name},
                recommendations=[
                    "Verify data initialization routines",
                    "Check for uninitialized fields",
                    "Review data conversion logic",
                    "Validate input data sources",
                    "Implement data quality checks"
                ],
                related_messages=data_messages[:5]
            ))
        
        return findings
    
    def _check_recurring_errors(self, messages: List[FIXCATMessage], rule: ReviewRule) -> List[Issue]:
        """Check for recurring error patterns"""
        findings = []
        
        # Group by message ID
        msg_groups = defaultdict(list)
        for msg in messages:
            msg_groups[msg.message_id].append(msg)
        
        # Check for recurring patterns
        for msg_id, msgs in msg_groups.items():
            if len(msgs) >= rule.threshold:
                findings.append(Issue(
                    issue_id=f"RULE-RECURRING-{msg_id}",
                    title=f"Recurring Error Pattern: {msg_id}",
                    severity=rule.severity,
                    category=rule.category,
                    description=f"Message {msg_id} occurred {len(msgs)} times",
                    occurrences=len(msgs),
                    first_seen=min(m.timestamp for m in msgs),
                    last_seen=max(m.timestamp for m in msgs),
                    affected_jobs={m.job_name for m in msgs if m.job_name},
                    recommendations=[
                        "Investigate root cause of recurring message",
                        "Review system configuration",
                        "Consider implementing preventive measures",
                        "Check for environmental factors"
                    ],
                    related_messages=msgs[:5]
                ))
        
        return findings
    
    def _check_job_cascades(self, messages: List[FIXCATMessage], rule: ReviewRule) -> List[Issue]:
        """Check for cascading job failures"""
        findings = []
        
        # Sort messages by timestamp
        sorted_msgs = sorted(messages, key=lambda m: m.timestamp)
        
        # Look for multiple failures in short timeframe
        window_start = 0
        for i in range(len(sorted_msgs)):
            # Move window start forward
            while (sorted_msgs[i].timestamp - sorted_msgs[window_start].timestamp).total_seconds() > rule.timeframe_hours * 3600:
                window_start += 1
            
            # Check if threshold met in window
            window_msgs = sorted_msgs[window_start:i+1]
            failure_msgs = [m for m in window_msgs if m.abend_code or 'FAIL' in m.description.upper()]
            
            if len(failure_msgs) >= rule.threshold:
                unique_jobs = {m.job_name for m in failure_msgs if m.job_name}
                if len(unique_jobs) >= 2:  # Multiple jobs affected
                    findings.append(Issue(
                        issue_id=f"RULE-CASCADE-{i}",
                        title="Cascading Job Failures Detected",
                        severity=rule.severity,
                        category=rule.category,
                        description=f"{len(failure_msgs)} job failures in {rule.timeframe_hours} hours",
                        occurrences=len(failure_msgs),
                        first_seen=failure_msgs[0].timestamp,
                        last_seen=failure_msgs[-1].timestamp,
                        affected_jobs=unique_jobs,
                        recommendations=[
                            "Review job dependencies",
                            "Check for common resource issues",
                            "Verify job scheduling",
                            "Implement better error handling"
                        ],
                        related_messages=failure_msgs[:5]
                    ))
                    break  # Only report once
        
        return findings
    
    def _check_resource_contention(self, messages: List[FIXCATMessage], rule: ReviewRule) -> List[Issue]:
        """Check for resource contention issues"""
        findings = []
        contention_keywords = ['ENQUEUE', 'DEADLOCK', 'WAIT', 'CONTENTION', 'BUSY']
        
        contention_messages = [
            m for m in messages 
            if any(kw in m.description.upper() for kw in contention_keywords)
        ]
        
        if len(contention_messages) >= rule.threshold:
            findings.append(Issue(
                issue_id="RULE-RESOURCE-001",
                title="Resource Contention Detected",
                severity=rule.severity,
                category=rule.category,
                description=f"Detected {len(contention_messages)} resource contention issues",
                occurrences=len(contention_messages),
                first_seen=min(m.timestamp for m in contention_messages),
                last_seen=max(m.timestamp for m in contention_messages),
                affected_jobs={m.job_name for m in contention_messages if m.job_name},
                recommendations=[
                    "Review resource allocation",
                    "Check for deadlock conditions",
                    "Optimize job scheduling",
                    "Consider resource pooling",
                    "Review ENQ/DEQ usage"
                ],
                related_messages=contention_messages[:5]
            ))
        
        return findings
    
    def get_rule_summary(self) -> Dict[str, Any]:
        """Get summary of configured rules"""
        return {
            'total_rules': len(self.rules),
            'enabled_rules': sum(1 for r in self.rules if r.enabled),
            'rules_by_severity': self._count_rules_by_severity(),
            'rules_by_category': self._count_rules_by_category()
        }
    
    def _count_rules_by_severity(self) -> Dict[str, int]:
        """Count rules by severity"""
        counts = defaultdict(int)
        for rule in self.rules:
            if rule.enabled:
                counts[rule.severity] += 1
        return dict(counts)
    
    def _count_rules_by_category(self) -> Dict[str, int]:
        """Count rules by category"""
        counts = defaultdict(int)
        for rule in self.rules:
            if rule.enabled:
                counts[rule.category] += 1
        return dict(counts)