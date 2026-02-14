"""
Report Generator Module
Generates peer review reports in various formats
"""

import json
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    Environment = None

try:
    from ..parsers.fixcat_parser import FIXCATMessage
    from ..analyzers.issue_analyzer import Issue
except ImportError:
    from parsers.fixcat_parser import FIXCATMessage
    from analyzers.issue_analyzer import Issue


class ReportGenerator:
    """Generates peer review reports in multiple formats"""
    
    def __init__(self, template_dir: Optional[str] = None):
        self.template_dir = template_dir or str(Path(__file__).parent / 'templates')
        self.jinja_env = None
        
        if Environment:
            try:
                self.jinja_env = Environment(
                    loader=FileSystemLoader(self.template_dir),
                    autoescape=select_autoescape(['html', 'xml'])
                )
            except Exception as e:
                print(f"Warning: Could not initialize Jinja2: {e}")
    
    def generate_report(
        self,
        issues: List[Issue],
        messages: List[FIXCATMessage],
        output_path: str,
        format: str = 'html',
        metadata: Optional[Dict] = None
    ) -> bool:
        """Generate a peer review report"""
        
        if format == 'html':
            return self._generate_html_report(issues, messages, output_path, metadata)
        elif format == 'json':
            return self._generate_json_report(issues, messages, output_path, metadata)
        elif format == 'markdown':
            return self._generate_markdown_report(issues, messages, output_path, metadata)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _generate_html_report(
        self,
        issues: List[Issue],
        messages: List[FIXCATMessage],
        output_path: str,
        metadata: Optional[Dict]
    ) -> bool:
        """Generate HTML report"""
        
        # Prepare report data
        report_data = self._prepare_report_data(issues, messages, metadata)
        
        # Generate HTML
        html_content = self._render_html_template(report_data)
        
        # Write to file
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            return True
        except Exception as e:
            print(f"Error writing HTML report: {e}")
            return False
    
    def _generate_json_report(
        self,
        issues: List[Issue],
        messages: List[FIXCATMessage],
        output_path: str,
        metadata: Optional[Dict]
    ) -> bool:
        """Generate JSON report"""
        
        report_data = {
            'metadata': metadata or {},
            'summary': self._generate_summary(issues, messages),
            'issues': [self._issue_to_dict(issue) for issue in issues],
            'statistics': self._generate_statistics(issues, messages)
        }
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, default=str)
            return True
        except Exception as e:
            print(f"Error writing JSON report: {e}")
            return False
    
    def _generate_markdown_report(
        self,
        issues: List[Issue],
        messages: List[FIXCATMessage],
        output_path: str,
        metadata: Optional[Dict]
    ) -> bool:
        """Generate Markdown report"""
        
        md_lines = []
        
        # Header
        md_lines.append("# FIXCAT Peer Review Report")
        md_lines.append("")
        md_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md_lines.append("")
        
        # Executive Summary
        md_lines.append("## Executive Summary")
        md_lines.append("")
        summary = self._generate_summary(issues, messages)
        md_lines.append(f"- **Total Issues:** {summary['total_issues']}")
        md_lines.append(f"- **Critical Issues:** {summary['critical_issues']}")
        md_lines.append(f"- **High Priority Issues:** {summary['high_issues']}")
        md_lines.append(f"- **Messages Analyzed:** {summary['total_messages']}")
        md_lines.append("")
        
        # Severity Breakdown
        md_lines.append("## Severity Breakdown")
        md_lines.append("")
        md_lines.append("| Severity | Count |")
        md_lines.append("|----------|-------|")
        for severity, count in summary['severity_breakdown'].items():
            md_lines.append(f"| {severity} | {count} |")
        md_lines.append("")
        
        # Top Issues
        md_lines.append("## Top Issues")
        md_lines.append("")
        for i, issue in enumerate(issues[:10], 1):
            md_lines.append(f"### {i}. {issue.title}")
            md_lines.append("")
            md_lines.append(f"- **Severity:** {issue.severity}")
            md_lines.append(f"- **Category:** {issue.category}")
            md_lines.append(f"- **Occurrences:** {issue.occurrences}")
            md_lines.append(f"- **Description:** {issue.description}")
            md_lines.append("")
            
            if issue.recommendations:
                md_lines.append("**Recommendations:**")
                for rec in issue.recommendations:
                    md_lines.append(f"- {rec}")
                md_lines.append("")
        
        # Write to file
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(md_lines))
            return True
        except Exception as e:
            print(f"Error writing Markdown report: {e}")
            return False
    
    def _prepare_report_data(
        self,
        issues: List[Issue],
        messages: List[FIXCATMessage],
        metadata: Optional[Dict]
    ) -> Dict:
        """Prepare data for report generation"""
        
        return {
            'metadata': metadata or {},
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'summary': self._generate_summary(issues, messages),
            'issues': issues,
            'statistics': self._generate_statistics(issues, messages),
            'top_issues': issues[:10]
        }
    
    def _generate_summary(self, issues: List[Issue], messages: List[FIXCATMessage]) -> Dict:
        """Generate executive summary"""
        
        severity_breakdown = {}
        for issue in issues:
            severity_breakdown[issue.severity] = severity_breakdown.get(issue.severity, 0) + 1
        
        return {
            'total_issues': len(issues),
            'critical_issues': severity_breakdown.get('CRITICAL', 0),
            'high_issues': severity_breakdown.get('HIGH', 0),
            'medium_issues': severity_breakdown.get('MEDIUM', 0),
            'low_issues': severity_breakdown.get('LOW', 0),
            'total_messages': len(messages),
            'severity_breakdown': severity_breakdown
        }
    
    def _generate_statistics(self, issues: List[Issue], messages: List[FIXCATMessage]) -> Dict:
        """Generate detailed statistics"""
        
        # Category breakdown
        category_breakdown = {}
        for issue in issues:
            category_breakdown[issue.category] = category_breakdown.get(issue.category, 0) + 1
        
        # Affected jobs
        all_jobs = set()
        for issue in issues:
            all_jobs.update(issue.affected_jobs)
        
        # Message ID frequency
        msg_id_freq = {}
        for msg in messages:
            msg_id_freq[msg.message_id] = msg_id_freq.get(msg.message_id, 0) + 1
        
        top_msg_ids = sorted(msg_id_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        
        return {
            'category_breakdown': category_breakdown,
            'affected_jobs_count': len(all_jobs),
            'affected_jobs': list(all_jobs)[:20],  # Limit to 20
            'top_message_ids': [{'id': mid, 'count': count} for mid, count in top_msg_ids]
        }
    
    def _issue_to_dict(self, issue: Issue) -> Dict:
        """Convert Issue object to dictionary"""
        
        return {
            'issue_id': issue.issue_id,
            'title': issue.title,
            'severity': issue.severity,
            'category': issue.category,
            'description': issue.description,
            'occurrences': issue.occurrences,
            'first_seen': issue.first_seen.isoformat() if issue.first_seen else None,
            'last_seen': issue.last_seen.isoformat() if issue.last_seen else None,
            'affected_jobs': list(issue.affected_jobs),
            'affected_programs': list(issue.affected_programs),
            'recommendations': issue.recommendations
        }
    
    def _render_html_template(self, report_data: Dict) -> str:
        """Render HTML template"""
        
        if self.jinja_env:
            try:
                template = self.jinja_env.get_template('report.html')
                return template.render(**report_data)
            except Exception as e:
                print(f"Warning: Could not render template: {e}")
        
        # Fallback to basic HTML
        return self._generate_basic_html(report_data)
    
    def _generate_basic_html(self, report_data: Dict) -> str:
        """Generate basic HTML report without templates"""
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FIXCAT Peer Review Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .summary {{
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .issue {{
            background-color: white;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .issue.critical {{ border-left-color: #e74c3c; }}
        .issue.high {{ border-left-color: #e67e22; }}
        .issue.medium {{ border-left-color: #f39c12; }}
        .issue.low {{ border-left-color: #95a5a6; }}
        .severity {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 3px;
            font-weight: bold;
            font-size: 0.9em;
        }}
        .severity.critical {{ background-color: #e74c3c; color: white; }}
        .severity.high {{ background-color: #e67e22; color: white; }}
        .severity.medium {{ background-color: #f39c12; color: white; }}
        .severity.low {{ background-color: #95a5a6; color: white; }}
        .recommendations {{
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 3px;
            margin-top: 10px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        th, td {{
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #34495e;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>FIXCAT Peer Review Report</h1>
        <p>Generated: {report_data['generated_at']}</p>
    </div>
    
    <div class="summary">
        <h2>Executive Summary</h2>
        <table>
            <tr>
                <th>Metric</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Total Issues</td>
                <td>{report_data['summary']['total_issues']}</td>
            </tr>
            <tr>
                <td>Critical Issues</td>
                <td>{report_data['summary']['critical_issues']}</td>
            </tr>
            <tr>
                <td>High Priority Issues</td>
                <td>{report_data['summary']['high_issues']}</td>
            </tr>
            <tr>
                <td>Messages Analyzed</td>
                <td>{report_data['summary']['total_messages']}</td>
            </tr>
        </table>
    </div>
    
    <h2>Issues</h2>
"""
        
        for issue in report_data['top_issues']:
            severity_class = issue.severity.lower()
            html += f"""
    <div class="issue {severity_class}">
        <h3>{issue.title}</h3>
        <p><span class="severity {severity_class}">{issue.severity}</span> | Category: {issue.category} | Occurrences: {issue.occurrences}</p>
        <p>{issue.description}</p>
"""
            if issue.recommendations:
                html += """
        <div class="recommendations">
            <strong>Recommendations:</strong>
            <ul>
"""
                for rec in issue.recommendations:
                    html += f"                <li>{rec}</li>\n"
                html += """
            </ul>
        </div>
"""
            html += "    </div>\n"
        
        html += """
</body>
</html>
"""
        return html