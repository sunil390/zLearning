"""
Test script for FIXCAT Peer Review Agent
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parsers import FIXCATParser
from src.analyzers import IssueAnalyzer
from src.rules import ReviewRulesEngine
from src.reporters import ReportGenerator


def test_parser():
    """Test FIXCAT parser"""
    print("Testing FIXCAT Parser...")
    
    parser = FIXCATParser()
    sample_file = Path(__file__).parent.parent / 'examples' / 'sample_logrec.txt'
    
    if not sample_file.exists():
        print(f"  ❌ Sample file not found: {sample_file}")
        return False
    
    messages = parser.parse_file(str(sample_file))
    
    print(f"  ✓ Parsed {len(messages)} messages")
    print(f"  ✓ Parse errors: {len(parser.parse_errors)}")
    
    # Check statistics
    stats = parser.get_statistics()
    print(f"  ✓ Statistics: {stats}")
    
    if len(messages) == 0:
        print("  ❌ No messages parsed")
        return False
    
    print("  ✅ Parser test passed")
    return True


def test_analyzer():
    """Test issue analyzer"""
    print("\nTesting Issue Analyzer...")
    
    parser = FIXCATParser()
    sample_file = Path(__file__).parent.parent / 'examples' / 'sample_logrec.txt'
    messages = parser.parse_file(str(sample_file))
    
    config_file = Path(__file__).parent.parent / 'config' / 'default.yaml'
    analyzer = IssueAnalyzer(str(config_file))
    
    issues = analyzer.analyze(messages)
    
    print(f"  ✓ Identified {len(issues)} issues")
    
    # Check summary
    summary = analyzer.get_summary()
    print(f"  ✓ Summary: {summary}")
    
    if len(issues) > 0:
        print(f"  ✓ Top issue: {issues[0].title} ({issues[0].severity})")
    
    print("  ✅ Analyzer test passed")
    return True


def test_rules_engine():
    """Test review rules engine"""
    print("\nTesting Review Rules Engine...")
    
    parser = FIXCATParser()
    sample_file = Path(__file__).parent.parent / 'examples' / 'sample_logrec.txt'
    messages = parser.parse_file(str(sample_file))
    
    rules_engine = ReviewRulesEngine()
    
    print(f"  ✓ Loaded {len(rules_engine.rules)} rules")
    
    findings = rules_engine.execute_rules(messages)
    
    print(f"  ✓ Rules identified {len(findings)} findings")
    
    # Check rule summary
    summary = rules_engine.get_rule_summary()
    print(f"  ✓ Rule summary: {summary}")
    
    print("  ✅ Rules engine test passed")
    return True


def test_reporter():
    """Test report generator"""
    print("\nTesting Report Generator...")
    
    parser = FIXCATParser()
    sample_file = Path(__file__).parent.parent / 'examples' / 'sample_logrec.txt'
    messages = parser.parse_file(str(sample_file))
    
    config_file = Path(__file__).parent.parent / 'config' / 'default.yaml'
    analyzer = IssueAnalyzer(str(config_file))
    issues = analyzer.analyze(messages)
    
    reporter = ReportGenerator()
    
    # Test HTML report
    output_dir = Path(__file__).parent.parent / 'examples'
    html_output = output_dir / 'test_report.html'
    
    success = reporter.generate_report(
        issues=issues,
        messages=messages,
        output_path=str(html_output),
        format='html'
    )
    
    if success and html_output.exists():
        print(f"  ✓ HTML report generated: {html_output}")
        print(f"  ✓ Report size: {html_output.stat().st_size} bytes")
    else:
        print("  ❌ HTML report generation failed")
        return False
    
    # Test JSON report
    json_output = output_dir / 'test_report.json'
    success = reporter.generate_report(
        issues=issues,
        messages=messages,
        output_path=str(json_output),
        format='json'
    )
    
    if success and json_output.exists():
        print(f"  ✓ JSON report generated: {json_output}")
    else:
        print("  ❌ JSON report generation failed")
        return False
    
    # Test Markdown report
    md_output = output_dir / 'test_report.md'
    success = reporter.generate_report(
        issues=issues,
        messages=messages,
        output_path=str(md_output),
        format='markdown'
    )
    
    if success and md_output.exists():
        print(f"  ✓ Markdown report generated: {md_output}")
    else:
        print("  ❌ Markdown report generation failed")
        return False
    
    print("  ✅ Reporter test passed")
    return True


def test_full_workflow():
    """Test complete workflow"""
    print("\nTesting Full Workflow...")
    
    from fixcat_agent import FIXCATReviewer
    
    sample_file = Path(__file__).parent.parent / 'examples' / 'sample_logrec.txt'
    output_file = Path(__file__).parent.parent / 'examples' / 'workflow_report.html'
    
    reviewer = FIXCATReviewer()
    
    try:
        results = reviewer.review(
            str(sample_file),
            str(output_file),
            format='html'
        )
        
        print(f"  ✓ Workflow completed successfully")
        print(f"  ✓ Total issues: {len(results['issues'])}")
        print(f"  ✓ Report generated: {output_file}")
        
        print("  ✅ Full workflow test passed")
        return True
    
    except Exception as e:
        print(f"  ❌ Workflow failed: {e}")
        return False


def main():
    """Run all tests"""
    print("="*60)
    print("FIXCAT Peer Review Agent - Test Suite")
    print("="*60)
    
    tests = [
        test_parser,
        test_analyzer,
        test_rules_engine,
        test_reporter,
        test_full_workflow
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"  ❌ Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    print(f"Total tests: {len(results)}")
    print(f"Passed: {sum(results)}")
    print(f"Failed: {len(results) - sum(results)}")
    
    if all(results):
        print("\n✅ All tests passed!")
        return 0
    else:
        print("\n❌ Some tests failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())