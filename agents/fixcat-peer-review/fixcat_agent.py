#!/usr/bin/env python3
"""
FIXCAT Peer Review Agent
Main entry point for the FIXCAT peer review agent
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from src.parsers import FIXCATParser
from src.analyzers import IssueAnalyzer
from src.rules import ReviewRulesEngine
from src.reporters import ReportGenerator


class FIXCATReviewer:
    """Main FIXCAT Peer Review Agent"""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize the FIXCAT reviewer"""
        self.config_path = config_path or 'config/default.yaml'
        self.parser = FIXCATParser()
        self.analyzer = IssueAnalyzer(self.config_path)
        self.rules_engine = ReviewRulesEngine()
        self.reporter = ReportGenerator()
    
    def analyze_file(self, input_path: str) -> dict:
        """Analyze a FIXCAT file"""
        print(f"Parsing FIXCAT data from: {input_path}")
        
        # Parse messages
        messages = self.parser.parse_file(input_path)
        print(f"Parsed {len(messages)} messages")
        
        if self.parser.parse_errors:
            print(f"Warning: {len(self.parser.parse_errors)} parse errors occurred")
        
        # Analyze issues
        print("Analyzing issues...")
        issues = self.analyzer.analyze(messages)
        print(f"Identified {len(issues)} issues")
        
        # Apply review rules
        print("Applying review rules...")
        rule_findings = self.rules_engine.execute_rules(messages)
        print(f"Rules identified {len(rule_findings)} additional findings")
        
        # Combine findings
        all_issues = issues + rule_findings
        
        # Remove duplicates based on issue_id
        unique_issues = {}
        for issue in all_issues:
            if issue.issue_id not in unique_issues:
                unique_issues[issue.issue_id] = issue
        
        final_issues = list(unique_issues.values())
        
        return {
            'messages': messages,
            'issues': final_issues,
            'statistics': self.parser.get_statistics(),
            'summary': self.analyzer.get_summary()
        }
    
    def generate_report(self, results: dict, output_path: str, format: str = 'html'):
        """Generate a peer review report"""
        print(f"Generating {format.upper()} report: {output_path}")
        
        metadata = {
            'input_file': results.get('input_file', 'Unknown'),
            'statistics': results.get('statistics', {}),
            'summary': results.get('summary', {})
        }
        
        success = self.reporter.generate_report(
            issues=results['issues'],
            messages=results['messages'],
            output_path=output_path,
            format=format,
            metadata=metadata
        )
        
        if success:
            print(f"Report generated successfully: {output_path}")
        else:
            print(f"Error generating report")
        
        return success
    
    def review(self, input_path: str, output_path: str, format: str = 'html'):
        """Complete review workflow"""
        # Analyze
        results = self.analyze_file(input_path)
        results['input_file'] = input_path
        
        # Generate report
        self.generate_report(results, output_path, format)
        
        # Print summary
        self._print_summary(results)
        
        return results
    
    def _print_summary(self, results: dict):
        """Print analysis summary to console"""
        print("\n" + "="*60)
        print("FIXCAT PEER REVIEW SUMMARY")
        print("="*60)
        
        summary = results.get('summary', {})
        print(f"\nTotal Issues: {summary.get('total_issues', 0)}")
        print(f"  - Critical: {summary.get('critical_issues', 0)}")
        print(f"  - High:     {summary.get('high_issues', 0)}")
        print(f"  - Medium:   {summary.get('medium_issues', 0)}")
        print(f"  - Low:      {summary.get('low_issues', 0)}")
        
        print(f"\nMessages Analyzed: {summary.get('total_messages', 0)}")
        
        # Top issues
        issues = results.get('issues', [])
        if issues:
            print("\nTop 5 Issues:")
            for i, issue in enumerate(issues[:5], 1):
                print(f"  {i}. [{issue.severity}] {issue.title}")
                print(f"     Occurrences: {issue.occurrences}")
        
        print("\n" + "="*60)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='FIXCAT Peer Review Agent - Automated mainframe error analysis'
    )
    
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Input FIXCAT/LOGREC file path'
    )
    
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Output report file path'
    )
    
    parser.add_argument(
        '--format', '-f',
        choices=['html', 'json', 'markdown'],
        default='html',
        help='Output report format (default: html)'
    )
    
    parser.add_argument(
        '--config', '-c',
        help='Configuration file path (default: config/default.yaml)'
    )
    
    parser.add_argument(
        '--input-dir',
        help='Input directory for batch processing'
    )
    
    parser.add_argument(
        '--output-dir',
        help='Output directory for batch processing'
    )
    
    args = parser.parse_args()
    
    # Initialize reviewer
    reviewer = FIXCATReviewer(config_path=args.config)
    
    # Batch processing
    if args.input_dir and args.output_dir:
        input_dir = Path(args.input_dir)
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"Batch processing files in: {input_dir}")
        
        for input_file in input_dir.glob('*.txt'):
            output_file = output_dir / f"{input_file.stem}_report.{args.format}"
            print(f"\nProcessing: {input_file.name}")
            
            try:
                reviewer.review(str(input_file), str(output_file), args.format)
            except Exception as e:
                print(f"Error processing {input_file.name}: {e}")
        
        print("\nBatch processing complete")
    
    # Single file processing
    else:
        try:
            reviewer.review(args.input, args.output, args.format)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()